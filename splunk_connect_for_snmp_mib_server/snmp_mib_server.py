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
import argparse
import yaml
from splunk_connect_for_snmp_mib_server.mongo import MibsRepository
from splunk_connect_for_snmp_mib_server.mib_server import MibServer
import logging

logger = logging.getLogger(__name__)


def upload_mibs(server_config):
    mibs_mongo_config = server_config["mongo"]["mib"]
    mib_files_dir = server_config["snmp"]["mibs"]["dir"]
    mibs_collection = MibsRepository(mibs_mongo_config)
    # TODO do we need to clean up before loading
    # Clean up
    mibs_collection.clear()
    # Upload all mib files in specific dir into mongo
    mibs_collection.upload_files(mib_files_dir)
    logger.debug("Uploaded all mib files into mongo!")


def main():
    logger.info(f"Startup Config")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--loglevel",
        default="info",
        help="Provide logging level. Example --loglevel debug, default=warning",
    )
    parser.add_argument(
        "-p", "--port", default=5000, help="Port to accept connections on", type=int
    )
    parser.add_argument(
        "--hec_threads", default=10, help="Max http worker thread count", type=int
    )
    parser.add_argument("-c", "--config", default="config.yaml", help="Config File")
    args = parser.parse_args()
    log_level = args.loglevel.upper()
    config_file = args.config

    logging.getLogger().setLevel(log_level)
    logger.info(f"Log Level is {log_level}")
    logger.info(f"Config file is {config_file}")
    logger.info("Completed Argument parsing")

    with open(config_file, "r") as yamlfile:
        server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

    upload_mibs(server_config)
    mib_server = MibServer(args, server_config)
    mib_server.run_mib_server()


if __name__ == "__main__":
    main()
