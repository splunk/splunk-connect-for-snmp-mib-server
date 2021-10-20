#   ########################################################################
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
#   ########################################################################
import logging
import os
from unittest import TestCase, mock

import mongomock
from pysnmp.hlapi import (
    CommunityData,
    ContextData,
    SnmpEngine,
    UdpTransportTarget,
    getCmd,
)
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType

from splunk_connect_for_snmp_mib_server.snmp_mib_server import upload_mibs
from splunk_connect_for_snmp_mib_server.translator import Translator

logger = logging.getLogger(__name__)


# This sample function was used to generate test data.
# I took the content of https://raw.githubusercontent.com/etingof/snmpsim/master/data/recorded/linux-full-walk.snmprec
# and sorted by data type. This should give us some real data we can use to test our MIB-server translation
# process. This was the input data we use in our test "test_translate_all_snmp_simulator_data_types"
def prepare_test_data():
    for oid in (
        "1.3.6.1.2.1.2.2.1.4.1",
        "1.3.6.1.2.1.1.6.0",
        "1.3.6.1.2.1.2.2.1.6.2",
        "1.3.6.1.2.1.1.9.1.2.7",
        "1.3.6.1.2.1.6.13.1.4.195.218.254.105.51684.194.67.10.226.22",
        "1.3.6.1.2.1.25.3.2.1.6.1025",
        "1.3.6.1.2.1.31.1.1.1.15.2",
        "1.3.6.1.2.1.1.3.0",
        "1.3.6.1.4.1.2021.10.1.6.1",
        "1.3.6.1.2.1.31.1.1.1.10.1",
    ):
        g = getCmd(
            SnmpEngine(),
            CommunityData("public"),
            UdpTransportTarget(("localhost", 1611)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)),
        )
        error_indication, error_status, error_index, var_binds = next(g)
        for name, value in var_binds:
            class_name = value.__class__.__name__
            # normal_value = value
            str_value = str(value).replace("\n", "")
            pretty_value = value.prettyPrint()
            print(
                f"{str(name)}|{class_name}|{str_value}|{pretty_value}|{pretty_value == str_value}"
            )


class TranslatorTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env_patcher = mock.patch.dict(
            os.environ,
            {
                "MIBS_FILES_URL": "http://0.0.0.0:5000/files/asn1/@mib@",
                "MONGO_SERVICE_SERVICE_HOST": "localhost",
                "MONGO_SERVICE_SERVICE_PORT": "27017",
            },
        )
        cls.env_patcher.start()
        super().setUpClass()

    @mongomock.patch()
    def setUp(self):
        server_config = {
            "snmp": {
                "mibs": {
                    "dir": "./mibs/pysnmp",
                    "load_list": "lookups/mibs_list.csv",
                    "mibs_path": "./mibs",
                }
            },
            "mongo": {
                "oid": {"database": "mib_server", "collection": "oids"},
                "mib": {"database": "files", "collection": "mib_files"},
            },
        }
        # server_config["snmp"]["mibs"]["dir"] = "../mibs/pysnmp"
        self.my_translator = Translator(server_config)
        upload_mibs(server_config)

    @mongomock.patch()
    def test_format_trap(self):
        input_var_binds_list = [
            {
                "oid": "1.3.6.1.2.1.1.3.0",
                "oid_type": "ObjectName",
                "val": "123",
                "val_type": "TimeTicks",
            },
            {
                "oid": "1.3.6.1.6.3.1.1.4.1.0",
                "oid_type": "ObjectName",
                "val": "1.3.6.1.4.1.1978.2.14.1.1.1",
                "val_type": "ObjectIdentifier",
            },
        ]

        translated_var_binds = self.my_translator.format_text_event(
            input_var_binds_list
        )
        assert len(translated_var_binds) > 0
        assert translated_var_binds.find("SNMPv2-MIB::sysUpTime.0") >= 0
        assert translated_var_binds.find("SNMPv2-MIB::snmpTrapOID.0") >= 0

    @mongomock.patch()
    def test_format_trap_non_existing_oid(self):
        input_var_binds_list = [
            {
                "oid": "1.3.6.1.2.1111.111.111.111.444.555.555.555",
                "oid_type": "ObjectName",
                "val": "123",
                "val_type": "TimeTicks",
            },
            {
                "oid": "1.3222.6333.1444.65555.343434343.3434343.3.1.1.4.1.0",
                "oid_type": "ObjectName",
                "val": "1.3.6.1.4.1.1978.2.14.1.1.1",
                "val_type": "ObjectIdentifier",
            },
        ]

        translated_var_binds = self.my_translator.format_text_event(
            input_var_binds_list
        )

        untranslated = ""
        for i in range(0, len(input_var_binds_list)):
            oid_type = input_var_binds_list[i]["oid_type"]
            value_type = input_var_binds_list[i]["val_type"]
            oid = input_var_binds_list[i]["oid"]
            value = input_var_binds_list[i]["val"]
            current = (
                f'oid-type{i + 1}="{oid_type}"'
                f' value{i + 1}-type="{value_type}" {oid}="{value}" value{i + 1}="{value}"'
            )
            # these two additional spaces are not an error
            untranslated += f"{current}  "
            if i < len(input_var_binds_list) - 1:
                untranslated += "\n"

        assert untranslated == translated_var_binds

    @mongomock.patch()
    def test_format_trap_invalid_input(self):
        input_var_binds_invalids = [
            {
                # MISSING OID
                # "oid": "1.3.6.1.2.1.1.3.0",
                "oid_type": "ObjectName",
                "val": "123",
                "val_type": "TimeTicks",
            },
            {
                "oid": "1.3.6.1.2.1.1.3.0",
                # MISSING OID_TYPE
                # "oid_type": "ObjectName",
                "val": "123",
                "val_type": "TimeTicks",
            },
            {
                "oid": "1.3.6.1.2.1.1.3.0",
                "oid_type": "ObjectName",
                # MISSING VAL
                # "val": "123",
                "val_type": "TimeTicks",
            },
            {
                "oid": "1.3.6.1.2.1.1.3.0",
                "oid_type": "ObjectName",
                "val": "123",
                # MISSING VAL_TYPE
                # "val_type": "TimeTicks",
            },
        ]

        translated_var_binds = self.my_translator.format_text_event(
            input_var_binds_invalids
        )
        assert len(translated_var_binds) == 0

    @mongomock.patch()
    def test_format_metric(self):
        input_var_binds = [
            {
                "oid": "1.3.6.1.2.1.1.3.0",
                "val": "123",
                "val_type": "TimeTicks",
            }
        ]
        translated_dict = self.my_translator.format_metric_data(input_var_binds)
        for required_key in ["metric_name", "_value", "metric_type"]:
            assert required_key in translated_dict
        assert translated_dict["metric_name"] == "sc4snmp.SNMPv2-MIB.sysUpTime_0"
        input_var_bind = input_var_binds[0]
        assert translated_dict["_value"] == input_var_bind["val"]
        assert translated_dict["metric_type"] == input_var_bind["val_type"]

    @mongomock.patch()
    def test_format_non_existing_metric(self):
        input_var_binds = [
            {
                "oid": "1.3.6666.16666.26666.16666.1.3.0",
                "val": "123",
                "val_type": "TimeTicks",
            }
        ]
        translated_dict = self.my_translator.format_metric_data(input_var_binds)
        for required_key in ["metric_name", "_value", "metric_type"]:
            assert required_key in translated_dict
        input_var_bind = input_var_binds[0]
        assert translated_dict["_value"] == input_var_bind["val"]
        assert translated_dict["metric_type"] == input_var_bind["val_type"]
        untranslated_oid = input_var_bind["oid"].replace(".", "_")
        assert translated_dict["metric_name"] == f"sc4snmp.{untranslated_oid}"

    @mongomock.patch()
    def test_translate_all_snmp_simulator_data_types(self):
        oids = (
            "1.3.6.1.2.1.2.2.1.4.1",
            "1.3.6.1.2.1.1.6.0",
            "1.3.6.1.2.1.2.2.1.6.2",
            "1.3.6.1.2.1.1.9.1.2.7",
            "1.3.6.1.2.1.6.13.1.4.195.218.254.105.51684.194.67.10.226.22",
            "1.3.6.1.2.1.25.3.2.1.6.1025",
            "1.3.6.1.2.1.31.1.1.1.15.2",
            "1.3.6.1.2.1.1.3.0",
            "1.3.6.1.4.1.2021.10.1.6.1",
            "1.3.6.1.2.1.31.1.1.1.10.1",
        )
        str_values = (
            "16436",
            "San Francisco, California, United States",
            "0x00127962f940",
            "1.3.6.1.2.1.50",
            "194.67.10.226",
            "0",
            "100",
            "147870473",
            "0x9f78043eeb851f",
            "381059068",
        )
        value_types = (
            "Integer",
            "DisplayString",
            "OctetString",
            "ObjectIdentity",
            "IpAddress",
            "Counter32",
            "Gauge32",
            "TimeTicks",
            "Opaque",
            "Counter64",
        )

        expected_translations = (
            "sc4snmp.IF-MIB.ifMtu_1",
            "sc4snmp.SNMPv2-MIB.sysLocation_0",
            "sc4snmp.IF-MIB.ifPhysAddress_2",
            "sc4snmp.SNMPv2-MIB.sysORID_7",
            "sc4snmp.TCP-MIB.tcpConnRemAddress_195_218_254_105_51684_194_67_10_226_22",
            "sc4snmp.HOST-RESOURCES-MIB.hrDeviceErrors_1025",
            "sc4snmp.IF-MIB.ifHighSpeed_2",
            "sc4snmp.SNMPv2-MIB.sysUpTime_0",
            "sc4snmp.1_3_6_1_4_1_2021_10_1_6_1",
            "sc4snmp.IF-MIB.ifHCOutOctets_1",
        )
        assert (
            len(oids) == len(str_values)
            and len(str_values) == len(value_types)
            and len(value_types) == len(expected_translations)
        )
        for index in range(0, len(oids)):
            input_var_binds_colons = [
                {
                    "oid": oids[index],
                    "val": str_values[index],
                    "val_type": value_types[index],
                }
            ]
            translated_metrics = self.my_translator.format_metric_data(
                input_var_binds_colons
            )
            assert translated_metrics["metric_name"] == expected_translations[index]

    @mongomock.patch()
    def test_more_mib_files(self):
        input_var_binds = [
            {
                "oid": "1.3.6.1.4.1.41456.1.2.1.1.42",
                "val": "0",
                "val_type": "Integer",
            },
            {
                "oid": "1.3.6.1.4.1.48328.3.9.1.1",
                "val": "sample",
                "val_type": "DisplayString",
            },
            {
                "oid": "1.3.6.1.2.1.25.1.6.0",
                "val": "165",
                "val_type": "Gauge32",
            },
        ]
        expected_values = [
            "sc4snmp.VMSTORE-MIB.mirrorLatency",
            "sc4snmp.VERITAS-APPLIANCE-MONITORING-MIB.vrtssystemName",
            "sc4snmp.HOST-RESOURCES-MIB.hrSystemProcesses_0",
        ]

        for i in range(0, len(input_var_binds)):
            translated_dict = self.my_translator.format_metric_data(input_var_binds, i)
            assert translated_dict["metric_name"] == expected_values[i]
