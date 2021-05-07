from pysnmp.smi import builder, view, compiler, rfc1902
import os
import json
import csv
import logging

from splunk_connect_for_snmp_mib_server.mongo import OidsRepository, MibsRepository

from pysmi import debug as pysmi_debug

pysmi_debug.setLogger(pysmi_debug.Debug("compiler"))

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

    # build a oids collection in mongo
    def build_oids_collection(self, oid_mongo_config):
        oids_collection = OidsRepository(oid_mongo_config)
        return oids_collection

    # build a mibs collection in mongo
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
                except Exception as e:
                    logger.error(f"Error happened during load module: {e}")
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

    # Check if the oid was translated properly
    def is_not_translated(self, org_val, trans_val):
        # if translated value equals to original value, it was not translated at all
        if org_val == trans_val:
            return True
        temp = trans_val.split(".")
        logger.debug(f"temp: {temp}")
        # if the second last number of the oid is numeric, it was not translated properly
        return len(temp) >= 2 and temp[-2].isnumeric()

    def write_mib_to_load_list(self, mib_name):
        mib_file_path = os.path.join(os.getcwd(), self._load_list)
        logger.debug(f"mib_file_path: {mib_file_path}")
        try:
            with open(mib_file_path, "a") as mib_list_file:
                writer = csv.writer(mib_list_file)
                writer.writerow([mib_name])
                logger.debug(f"[-] Wrote {mib_name} to mib list")
            mib_list_file.close()
        except Exception as e:
            logger.error(
                f"Error happened during write the mib into mib load list file: {e}"
            )

    # Find mib module based on the oid
    def find_mib_file(self, oid):
        value_tuple = str(oid).replace(".", ", ")
        mib_name = None

        try:
            mib_name = self._mongo_mibs_coll.search_oid(value_tuple)
        except Exception as e:
            logger.error(
                f"Error happened during search the oid in mongo mibs collection: {e}"
            )
        if not mib_name:
            logger.warning(
                f"Can NOT find the mib file for the oid-{oid} -- {value_tuple}"
            )
            logger.debug(f"Writing the oid-{oid} into mongo")
            try:
                self._mongo_oids_coll.add_oid(str(oid))
                logger.debug(
                    f"[-] The oid - {oid} was added into mongo oids collection"
                )
            except Exception as e:
                logger.error(
                    f"Error happened during add the oid - {oid} into mongo oids collection: {e}"
                )
            return
        mib_name = mib_name[:-3]
        logger.debug(f"mib_name: {mib_name}")
        # load the mib module
        self.load_extra_mib(mib_name, oid)

    # Load additional mib module
    def load_extra_mib(self, mib_module, oid):
        try:
            self._mib_builder.loadModules(mib_module)
            logger.debug(f"[-] Loaded module: {mib_module}")
            # add this mib module into mibs_list.csv if it was successfully loaded
            self.write_mib_to_load_list(mib_module)
        except Exception as e:
            logger.warning(
                f"Error happened during load mib module - {mib_module} for oid - {oid} : {e}"
            )
            logger.debug(f"Writing the oid-{oid} into mongo oids collection")
            try:
                self._mongo_oids_coll.add_oid(str(oid))
                logger.debug(
                    f"[-] The oid - {oid} was added into mongo oids collection"
                )
            except Exception as e:
                logger.error(
                    f"Error happened during add the oid - {oid} into mongo oids collection: {e}"
                )
            pass

    # Check if the oid is already in the mongodb
    def check_mongo(self, oid):
        # TODO remove #119-121 later
        no_mapping_mib = False
        try:
            result = self._mongo_oids_coll.contains_oid(str(oid))
            # if the oid was found in mongo, then the oid is verified that there is not mapping mib module for it
            no_mapping_mib = True if result != 0 else False
        except Exception as e:
            logger.error(
                f"Error happened when finding oid in mongo oids collection: {e}"
            )

        return no_mapping_mib

    # Translate SNMP PDU varBinds into MIB objects using MIB
    def mib_translator(self, var_bind):

        # Run var-binds through MIB resolver
        try:
            name = var_bind["oid"]
            val = var_bind["val"]
            translated_var_bind = rfc1902.ObjectType(
                rfc1902.ObjectIdentity(name), val
            ).resolveWithMib(self._mib_view_controller)

            logger.debug(f"* Translated PDU: {translated_var_bind.prettyPrint()}")
            trans_string = translated_var_bind.prettyPrint().replace(" = ", "=")
            trans_oid = trans_string.split("=")[0]
            trans_val = trans_string.split("=")[1]
            untranslated_val_type = var_bind["val_type"]

            try:
                # Check if oid exists in mongo oids collection and if oid was translated properly
                no_mapping_mib_oid = self.check_mongo(name)
                logger.debug(f"no_mapping_mib_oid: {no_mapping_mib_oid}")
                if not no_mapping_mib_oid and self.is_not_translated(name, trans_oid):
                    self.find_mib_file(name)

                # Check if value exists in mongo oids collection and if value was translated properly when value is OID type
                if (
                    untranslated_val_type == "ObjectIdentifier"
                    or untranslated_val_type == "ObjectIdentity"
                ):
                    no_mapping_mib_val = self.check_mongo(val)
                    logger.debug(f"no_mapping_mib_val: {no_mapping_mib_val}")
                    if not no_mapping_mib_val and self.is_not_translated(
                        val, trans_val
                    ):
                        self.find_mib_file(val)

                # Re-translated with the extra mibs
                translated_var_bind = rfc1902.ObjectType(
                    rfc1902.ObjectIdentity(name), val
                ).resolveWithMib(self._mib_view_controller)
                logger.debug(
                    f"* Re-Translated PDU: {translated_var_bind.prettyPrint()}"
                )

            except Exception as e:
                logger.debug(f"Error happened during translation checking: {e}")
                pass

            return translated_var_bind.prettyPrint().replace(" = ", "=")
        except Exception as e:
            logger.error(f"Error happened in translation: {e}")
        finally:
            pass

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
    def format_trap_event(self, var_binds):
        trap_event_string = ""
        offset = 0

        for var_bind in var_binds:
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
            original_oid = '{oid}="{value}"'.format(offset=offset, oid=oid, value=value)
            oid_type_string = 'oid-type{offset}="{oid_type}"'.format(
                offset=offset, oid_type=name_type
            )
            translated_mib_string = self.mib_translator(var_bind)
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
                        offset=offset,
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
        logger.debug(f"--- Trap Event String ---")
        logger.debug(trap_event_string)
        return trap_event_string

    # Format and translate the metric data
    def format_metric_data(self, var_bind):
        """
        format one varBind object into metric format
        @param var_bind: single varBind object
        """
        metric_data = {}

        oid = var_bind["oid"]
        value = var_bind["val"]
        val_type = var_bind["val_type"]

        # mib translation for oid (val keep same for original, mib translation, custom translation)
        translated_mib_string = self.mib_translator(var_bind)
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
        ] = f'sc4snmp.{translated_oid.replace(".","_").replace("::", ".")}'
        metric_data["_value"] = translated_val
        metric_data["metric_type"] = val_type
        if custom_translated_oid:
            metric_data["custom_metric_name"] = custom_translated_oid
        logger.debug(f"metric_data: {json.dumps(metric_data)}")
        return json.dumps(metric_data)
