from unittest import TestCase, mock

import mongomock
import yaml

from splunk_connect_for_snmp_mib_server.translator import Translator
import os
import logging

logger = logging.getLogger(__name__)


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
        with open("../config.yaml", "r") as yamlfile:
            server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)
        server_config["snmp"]["mibs"]["dir"] = "../mibs/pysnmp"
        self.my_translator = Translator(server_config)

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

        translated_var_binds = self.my_translator.format_trap_event(
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

        translated_var_binds = self.my_translator.format_trap_event(
            input_var_binds_list
        )

        untranslated = ""
        for i in range(0, len(input_var_binds_list)):
            oid_type = input_var_binds_list[i]["oid_type"]
            value_type = input_var_binds_list[i]["val_type"]
            oid = input_var_binds_list[i]["oid"]
            value = input_var_binds_list[i]["val"]
            current = f'oid-type{i+1}="{oid_type}" value{i+1}-type="{value_type}" {oid}="{value}" value{i+1}="{value}"'
            # these two additional spaces are not an error
            untranslated += f"{current}  "
            if i < len(input_var_binds_list) - 1:
                untranslated += "\n"

        assert untranslated == translated_var_binds
