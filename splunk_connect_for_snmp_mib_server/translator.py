#   ##########################################################################
#   Copyright 2021 Splunk Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#   ##########################################################################
import csv
import json
import logging
import os

from pysnmp.smi import builder, compiler, rfc1902, view

from splunk_connect_for_snmp_mib_server.mongo import MibsRepository, OidsRepository

logger = logging.getLogger(__name__)


class Translator:
    def __init__(self, server_config):
        self._server_config = server_config
        self._custom_translation_table = self.get_custom_translation_table()
        self._load_list = server_config["snmp"]["mibs"]["load_list"]
        self._mib_builder, self._mib_view_controller = self.build_mib_compiler()

        self._mongo_oids_coll = self.build_oids_collection(
            server_config["mongo"]["oid"]
        )
        self._mongo_mibs_coll = self.build_mibs_collection(
            server_config["mongo"]["mib"]
        )
        # Execute the 1st translation to force mibs to be ready to use
        self.first_mib_translation_trigger()

    # build a oids collection in mongodb
    def build_oids_collection(self, oid_mongo_config):
        oids_collection = OidsRepository(oid_mongo_config)
        return oids_collection

    # build a mibs collection in mongodb
    def build_mibs_collection(self, mib_mongo_config):
        mibs_collection = MibsRepository(mib_mongo_config)
        return mibs_collection

    def build_mib_compiler(self):
        # Assemble MIB browser
        snmp_config = self._server_config["snmp"]
        mib_builder = builder.MibBuilder()
        mib_view_controller = view.MibViewController(mib_builder)
        compiler.addMibCompiler(mib_builder, sources=[os.environ["MIBS_FILES_URL"]])

        # Optionally set an alternative path to compiled MIBs
        logger.debug("Setting MIB sources...")
        mib_builder.addMibSources(builder.DirMibSource(snmp_config["mibs"]["dir"]))
        logger.debug(mib_builder.getMibSources())
        logger.debug("done")

        mib_file_path = os.path.join(os.getcwd(), self._load_list)
        logger.debug(f"mib_file_path {mib_file_path}")
        with open(mib_file_path) as mib_files:
            reader = csv.reader(mib_files)
            cnt = 0
            for row in reader:
                module = row[0]
                try:
                    mib_builder.loadModules(module)
                    cnt += 1
                    logger.debug(f"[-] {cnt} Loaded module: {module}")
                except Exception:
                    logger.exception("Error happened during load module")
                    pass

        logger.debug("compiler is loaded")

        return mib_builder, mib_view_controller

    def first_mib_translation_trigger(self):
        # This is a test TRAP PDU
        var_binds_list = [
            {
                "oid": "1.3.6.1.2.1.1.3.0",
                "oid_type": "ObjectName",
                "val": "123",
                "val_type": "TimeTicks",
            },
            {
                "oid": "1.3.6.1.6.3.1.1.4.1.0",
                "oid_type": "ObjectName",
                "val": "1.3.6.1.6.3.1.1.5.2",
                "val_type": "ObjectIdentifier",
            },
        ]

        for var_bind in var_binds_list:
            self.mib_translator(var_bind)
        logger.debug("mib_translator is ready to use!")

    def write_mib_to_load_list(self, mib_name):
        mib_file_path = os.path.join(os.getcwd(), self._load_list)
        logger.debug(f"mib_file_path: {mib_file_path}")
        try:
            with open(mib_file_path, "a") as mib_list_file:
                writer = csv.writer(mib_list_file)
                writer.writerow([mib_name])
                logger.debug(f"[-] Wrote {mib_name} to mib list")
            mib_list_file.close()
        except Exception:
            logger.exception(
                f"Error happened during write the mib - {mib_name} into mib load list file"
            )

    # Find mib module based on the oid
    def find_mib_file(self, oid):
        logger.debug(f"Searching for {oid}")
        value_tuple = str(oid).replace(".", ", ")
        mib_list = None

        oid_without_index = ".".join(oid.split(".")[:-1])
        changed_oid_without_index = str(oid_without_index).replace(".", ", ")
        mib_list_without_index = None

        try:
            # Find mib module for OID without index (remove the last part of OID)
            # Handle the scenario that tries to translate an OID which has index append at the end.
            # e.g 1.3.6.1.2.1.25.1.6.0, where 0 is index and it's not part of the OID object
            # So we cannot find mapping MIBs for it
            # Instead, 1.3.6.1.2.1.25.1.6 is actually the OID that needed to be used for searching MIBs
            # Therefore, we should remove index (0) and search the real oid (1.3.6.1.2.1.25.1.6) to detect the MIBs

            mib_list = self._mongo_mibs_coll.search_oid(value_tuple)
            mib_list_without_index = self._mongo_mibs_coll.search_oid(
                changed_oid_without_index
            )
        except Exception:
            logger.exception(
                f"Error happened during search for the oids - {oid},"
                f" {changed_oid_without_index} in mongo mibs collection"
            )
        self.add_oid_to_db(mib_list, oid)
        self.add_oid_to_db(mib_list_without_index, changed_oid_without_index)
        if mib_list:
            self.load_extra_mibs(mib_list, oid)
        if mib_list_without_index:
            self.load_extra_mibs(mib_list_without_index, changed_oid_without_index)

    def add_oid_to_db(self, mib_list, oid):
        if not mib_list:
            try:
                if self._mongo_oids_coll.contains_oid(str(oid)) == 0:
                    logger.info(f"Adding oid {oid} as it is not in the db")
                    self._mongo_oids_coll.add_oid(str(oid))
            except Exception:
                logger.exception(
                    f"Error happened during add the oid - {oid} into mongo oids collection"
                )

    def load_extra_mibs(self, mib_list, oid):
        for mib_name in mib_list:
            mib_name = mib_name[:-3]
            self.load_extra_mib(mib_name, oid)
            logger.info(f"[-] The mib for mib_name - {mib_name} was loaded")

    # Load additional mib module
    def load_extra_mib(self, mib_module, oid):
        try:
            self._mib_builder.loadModules(mib_module)
            # add this mib module into mibs_list.csv if it was successfully loaded
            self.write_mib_to_load_list(mib_module)
        except Exception as e:
            logger.warning(
                f"Error happened during loading of the mib module - {mib_module} for oid - {oid} : {e}"
            )
            logger.debug(f"Writing the oid-{oid} into mongo oids collection")
            try:
                if self._mongo_oids_coll.contains_oid(str(oid)) == 0:
                    self._mongo_oids_coll.add_oid(str(oid))
                    logger.debug(
                        f"[-] The oid - {oid} was added into mongo oids collection"
                    )
            except Exception:
                logger.exception(
                    f"Error happened during add the oid - {oid} into mongo oids collection"
                )
            pass

    # Translate SNMP PDU varBinds into MIB objects using MIB
    def mib_translator(self, var_bind):
        try:
            name = var_bind["oid"]
            val = var_bind["val"]
            translated_var_bind = rfc1902.ObjectType(
                rfc1902.ObjectIdentity(name), val
            ).resolveWithMib(self._mib_view_controller)
        except Exception as e:
            logger.exception("Error happened in translation")
            if "not OBJECT-TYPE" in str(e):
                logger.debug("[-] Trying to lazy load MIBs")
                self.find_mib_file(name)
                try:
                    translated_var_bind = rfc1902.ObjectType(
                        rfc1902.ObjectIdentity(name), val
                    ).resolveWithMib(self._mib_view_controller)
                    logger.debug(
                        f"* Re-Translated PDU: {translated_var_bind.prettyPrint()}"
                    )

                except Exception as e:
                    logger.debug(f"Error happened during translation checking: {e}")
                    return None
            else:
                return None

        index_result = self.parse_index(translated_var_bind)
        return translated_var_bind.prettyPrint().replace(" = ", "="), index_result

    def parse_index(self, translated_var_bind):
        object_identity, object_value = translated_var_bind
        index_tuple = object_identity.getMibSymbol()[2]
        family = object_identity.getMibSymbol()[0]
        label_index = -1
        label = object_identity.getLabel()[label_index]
        index_row = self._mib_view_controller.mibBuilder.mibSymbols[family].get(label)
        index_result = dict()

        while (
            abs(label_index) < len(object_identity.getLabel())
            and type(index_row).__name__ == "MibTableColumn"
        ):
            label_index = label_index - 1
            label = object_identity.getLabel()[label_index]
            index_row = self._mib_view_controller.mibBuilder.mibSymbols[family].get(
                label
            )

        if index_row and type(index_row).__name__ == "MibTableRow":
            index_tuple = [v.prettyPrint() for v in index_tuple]
            index_names = [v[2] for v in index_row.getIndexNames()]
            index_result = dict(zip(index_names, index_tuple))

        return index_result

    # Translate SNMP PDU varBinds into MIB objects using custom translation table
    def custom_translator(self, oid):
        return self._custom_translation_table.get(oid, None)

    # Read the custom mib translation table into memory
    def get_custom_translation_table(self):
        translation_table = {}
        logger.debug(f"cwd {os.getcwd()}")
        file_path = os.path.join(os.getcwd(), "lookups/custom_mib_string_table.csv")
        logger.debug(f"file_path {file_path}")
        with open(file_path) as files:
            reader = csv.reader(files)
            next(reader)  # skip header
            for row in reader:
                translation_table[row[0]] = row[1]
        return translation_table

    # Format and translate the trap events
    def format_text_event(self, var_binds: list):
        trap_event_string = ""
        offset = 0

        for var_bind in var_binds:
            if not all(
                key in var_bind for key in ["oid", "oid_type", "val", "val_type"]
            ):
                logger.error(
                    f"Error in the following var_bind: {var_bind} (missing keys)"
                )
                continue

            oid = var_bind["oid"]
            value = var_bind["val"]
            name_type = var_bind["oid_type"]
            val_type = var_bind["val_type"]

            # custom translation
            custom_translated_oid = self.custom_translator(oid)
            custom_translated_value = value
            # translate value ONLY when it is oid
            if val_type == "ObjectIdentifier":
                custom_translated_value = self.custom_translator(value)

            offset += 1
            original_oid = '{oid}="{value}"'.format(oid=oid, value=value)
            oid_type_string = 'oid-type{offset}="{oid_type}"'.format(
                offset=offset, oid_type=name_type
            )
            translated_mib_string, parsed_index = self.mib_translator(var_bind)
            if translated_mib_string:
                translated_mib_string = '{translated_oid}="{translated_value}"'.format(
                    translated_oid=translated_mib_string.split("=")[0],
                    translated_value=translated_mib_string.split("=")[1],
                )
            else:
                translated_mib_string = ""

            if custom_translated_oid:
                custom_translated_mib_string = (
                    '{custom_translated_oid}="{custom_translated_value}"'.format(
                        custom_translated_oid=custom_translated_oid,
                        custom_translated_value=custom_translated_value,
                    )
                )
            else:
                custom_translated_mib_string = ""

            original_value = 'value{offset}="{value}"'.format(
                offset=offset, value=value
            )
            val_type_string = 'value{offset}-type="{val_type}"'.format(
                offset=offset, val_type=val_type
            )
            trap_event_string += " ".join(
                [
                    oid_type_string,
                    val_type_string,
                    original_oid,
                    original_value,
                    translated_mib_string,
                    custom_translated_mib_string,
                    #
                ]
            )
            trap_event_string += "\n"

        trap_event_string = trap_event_string.rstrip("\n")  # remove trailing newline
        logger.debug("--- Trap Event String ---")
        logger.debug(trap_event_string)
        return trap_event_string

    # Format and translate the metric data
    def format_metric_data(self, var_bind, index=0):
        """
        format one varBind object into metric format
        :param var_bind: varBind list, usually it contains only one element
        :param index: index of the element we want to process
        :return: translated data dictionary
        """
        var_bind = var_bind[index]
        metric_data = {}

        oid = var_bind["oid"]
        value = var_bind["val"]
        val_type = var_bind["val_type"]

        # mib translation for oid (val keep same for original, mib translation, custom translation)
        translated_mib_string, parsed_index = self.mib_translator(var_bind)
        if translated_mib_string:
            translated_oid = translated_mib_string.split("=")[0]
            translated_val = translated_mib_string.split("=")[1]
        else:
            translated_oid = oid
            translated_val = value

        # custom translation for oid
        custom_translated_oid = self.custom_translator(oid)

        # Construct metric data
        # .. Prefix the metric_name for UX in analytics workspace
        # .. Splunk uses . rather than :: for hierarchy.
        # .. if the metric name contains a . replace with _
        metric_data[
            "metric_name"
        ] = f'sc4snmp.{translated_oid.replace(".", "_").replace("::", ".")}'
        metric_data["_value"] = translated_val
        metric_data["metric_type"] = val_type
        if custom_translated_oid:
            metric_data["custom_metric_name"] = custom_translated_oid
        if parsed_index:
            metric_data["parsed_index"] = parsed_index
        logger.debug(f"metric_data: {json.dumps(metric_data)}")
        return metric_data

    def format_multimetric_data(self, varbinds: list) -> dict:
        """
        If field 'return_multimetric' was set to 'True', mib_server returns dictionary containing metric structure,
        non-metric structure and metric name. For example:

        {'metric_name': 'sc4snmp.IF-MIB.ifDescr_1',
        'metric': '{"metric_name": "sc4snmp.IF-MIB.ifDescr_1", "_value": "lo", "metric_type": "OctetString"}',
        'non_metric': 'oid-type1="ObjectIdentity" value1-type="OctetString" 1.3.6.1.2.1.2.2.1.2.1="lo"
        value1="lo" IF-MIB::ifDescr.1="lo" '}

        :param varbinds: list of varbinds
        :return: dictionary of the above structure
        """
        result_dict = self.format_metric_data(varbinds)
        result_string = self.format_text_event(varbinds)
        result = {
            "metric_name": result_dict["metric_name"],
            "metric": json.dumps(result_dict),
            "non_metric": result_string,
        }
        return result
