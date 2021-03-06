import sys
sys.path.append('../')
import yaml
# from splunk_connect_for_snmp_mib_server.mongo import OidsRepository
from splunk_connect_for_snmp_mib_server.translator import Translator
import os
import logging
logger = logging.getLogger(__name__)

def main():
    logger.debug("Start:....")
    # Read config file
    config_file = os.path.join(os.getcwd(), "..", "config.yaml")
    with open(config_file, "r") as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print(f"server_config: {server_config}")

    my_translator = Translator(server_config)

    var_binds_list = [
            {
                "oid": '1.3.6.1.2.1.1.3.0',
                "oid_type": "ObjectName",
                "val": "123",
                "val_type": "TimeTicks"
            },
            {
                "oid": '1.3.6.1.6.3.1.1.4.1.0',
                "oid_type": "ObjectName",
                "val": "1.3.6.1.4.1.1978.2.14.1.1.1",
                "val_type": "ObjectIdentifier"
            },
            {
                "oid": '1.3.6.1.6.3.1.1.4.1.0',
                "oid_type": "ObjectName",
                "val": "1.3.6.1.4.1.90000.1",
                "val_type": "ObjectIdentifier"
            }
        ]
    my_translator.format_trap_event(var_binds_list)

if __name__ == '__main__':
    main()

