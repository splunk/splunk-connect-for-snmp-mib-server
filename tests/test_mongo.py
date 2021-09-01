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
import sys

sys.path.append("../")
import os  # noqa: E402

from splunk_connect_for_snmp_mib_server.mongo import MibsRepository  # noqa: E402


def main():
    mongo_config = {
        "host": "localhost",
        "port": 27017,
        "database": "test",
        "collection": "mibs",
    }
    mongo = MibsRepository(mongo_config)

    mongo.clear()

    # Upload  mib files in /mibs/test to mongo
    mib_files_dir = os.path.join(os.getcwd(), "..", "mibs", "test")
    mongo.upload_files(mib_files_dir)

    # Search mib files based on oid
    oid = "1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 1"
    filename = mongo.search_oid(oid)
    print(filename)

    # Delete one specifc file
    if filename:
        mongo.delete_mib(filename)
        print(mongo.search_oid(oid))

    # Delete multiple files
    filename_regex = "A3COM"
    mongo.delete_mib(filename_regex)


if __name__ == "__main__":
    main()
