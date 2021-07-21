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

import pymongo

logger = logging.getLogger(__name__)


class MongoRepository:
    def __init__(self, mongo_config):
        self._client = pymongo.MongoClient(
            os.environ["MONGO_SERVICE_SERVICE_HOST"],
            int(os.environ["MONGO_SERVICE_SERVICE_PORT"]),
        )
        if os.environ.get("MONGO_USER"):
            self._client.admin.authenticate(
                os.environ["MONGO_USER"],
                os.environ["MONGO_PASS"],
                mechanism="SCRAM-SHA-1",
            )


class MibsRepository(MongoRepository):
    def __init__(self, mongo_config):
        super().__init__(mongo_config)
        self._mibs = self._client[mongo_config["database"]][mongo_config["collection"]]

    def upload_files(self, mib_files_dir):
        for filename in os.listdir(mib_files_dir):
            file_path = mib_files_dir + "/" + filename
            with open(file_path, "r") as mib_file:
                try:
                    self._mibs.insert_one(
                        dict(content=mib_file.read(), filename=filename, _id=filename)
                    )
                except Exception as e:
                    logger.error(
                        f"Error happened during insert mib files {filename} into mongo: {e}"
                    )

    def search_oid(self, oid):
        data = self._mibs.find({"content": {"$regex": oid}})
        if data:
            mib_list = []
            for item in data:
                mib_list.append(item["filename"])
            return mib_list
        else:
            return None

    def delete_mib(self, filename):
        self._mibs.delete_many({"filename": {"$regex": filename}})

    def clear(self):
        self._mibs.delete_many({})


class OidsRepository(MongoRepository):
    def __init__(self, mongo_config):
        super().__init__(mongo_config)
        self._oids = self._client[mongo_config["database"]][mongo_config["collection"]]

    def contains_oid(self, oid):
        return self._oids.count_documents({"oid": oid})

    def add_oid(self, oid):
        self._oids.insert_one({"oid": oid})

    def delete_oid(self, oid):
        self._oids.delete_many({"oid": oid})

    def clear(self):
        self._oids.remove()
