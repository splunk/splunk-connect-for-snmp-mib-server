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
    def test_format_trap(self):
        with open("../config.yaml", "r") as yamlfile:
            server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)
        server_config["snmp"]["mibs"]["dir"] = "../mibs/pysnmp"

        my_translator = Translator(server_config)

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

        translated_var_binds = my_translator.format_trap_event(input_var_binds_list)
        assert len(translated_var_binds) > 0
        assert translated_var_binds.find("SNMPv2-MIB::sysUpTime.0") >= 0
        assert translated_var_binds.find("SNMPv2-MIB::snmpTrapOID.0") >= 0
