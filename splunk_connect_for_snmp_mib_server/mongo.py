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
import re
import time

import pymongo

logger = logging.getLogger(__name__)


class MongoRepository:
    def __init__(self):
        self._client = pymongo.MongoClient(os.environ["MONGO_URI"])
        if os.environ.get("MONGO_USER"):
            self._client.admin.authenticate(
                os.environ["MONGO_USER"],
                os.environ["MONGO_PASS"],
                mechanism="SCRAM-SHA-1",
            )


class MibsRepository(MongoRepository):
    oid_regex = re.compile(r"\(((?:1, 3, 6, 1, )(?:\d+,?\s?)+)\)")

    def __init__(self, mongo_config):
        super().__init__()
        self._mibs = self._client[mongo_config["database"]][mongo_config["collection"]]

    def upload_files(self, mib_files_dir):
        tic = time.perf_counter()
        for filename in os.listdir(mib_files_dir):
            file_path = mib_files_dir + "/" + filename
            with open(file_path, "r") as mib_file:
                try:
                    read_file = mib_file.read()
                    self._mibs.insert_one(
                        dict(
                            content=read_file,
                            filename=filename,
                            _id=filename,
                            mibs=self.parse_iods(read_file),
                        )
                    )
                    self.parse_iods(read_file)
                except Exception:
                    logger.exception(
                        "Error happened during insert mib files %s into mongo", filename
                    )
        toc = time.perf_counter()
        logger.info(f"Uploading files took - {toc - tic:0.4f} seconds")

    @staticmethod
    def parse_iods(read_file):
        return re.findall(MibsRepository.oid_regex, read_file)

    def create_index_on_oids(self):
        tic = time.perf_counter()
        try:
            self._mibs.create_index("mibs", name="oid_index")
        except Exception:
            logger.exception(
                "Failed to create the index, searches will be performed without it"
            )
            return
        toc = time.perf_counter()
        logger.info(f"Creating index took - {toc - tic:0.4f} seconds")

    def search_oid(self, oid):
        data = self.perform_search(oid)
        if data:
            mib_list = []
            for item in data:
                mib_list.append(item["filename"])
            return mib_list
        else:
            return None

    def perform_search(self, oid):
        tic = time.perf_counter()
        data = list(self._mibs.find({"mibs": oid}))
        toc = time.perf_counter()
        logger.debug(
            f"We searched for oid - {oid} and it took - {toc - tic:0.7f} seconds"
        )
        return data

    def delete_mib(self, filename):
        self._mibs.delete_many({"filename": {"$regex": filename}})

    def clear(self):
        tic = time.perf_counter()
        self._mibs.drop()
        toc = time.perf_counter()
        logger.info(f"Cleaning took - {toc - tic:0.4f} seconds")


class OidsRepository(MongoRepository):
    def __init__(self, mongo_config):
        super().__init__()
        self._oids = self._client[mongo_config["database"]][mongo_config["collection"]]

    def contains_oid(self, oid):
        return self._oids.count_documents({"oid": oid})

    def add_oid(self, oid):
        self._oids.insert_one({"oid": oid})

    def delete_oid(self, oid):
        self._oids.delete_many({"oid": oid})

    def clear(self):
        self._oids.remove()
