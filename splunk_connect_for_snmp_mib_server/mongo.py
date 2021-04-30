from pymongo import MongoClient
import os
import logging

logger = logging.getLogger(__name__)


class MibsRepository:
    def __init__(self, mongo_config):
        """
        Create a collection in mongodb to store mib files
        """
        self._client = MongoClient(
            os.environ["MONGO_SERVICE_SERVICE_HOST"],
            int(os.environ["MONGO_SERVICE_SERVICE_PORT"]),
        )
        if os.environ.get("MONGO_USER"):
            self._client.admin.authenticate(
                os.environ["MONGO_USER"],
                os.environ["MONGO_PASS"],
                mechanism="SCRAM-SHA-1",
            )
        self._mibs = self._client[mongo_config["database"]][mongo_config["collection"]]

    def upload_files(self, mib_files_dir):
        """
        Upload mib files from dir to mongo
        @param mib_files_dir: the path of the mib files directory
        """
        # TODO check duplicate before insert, using filename as PK
        for filename in os.listdir(mib_files_dir):
            file_path = mib_files_dir + "/" + filename
            # print(file_path)
            with open(file_path, "r") as mib_file:
                # TODO add try catch, insert only if PK doesn't exit
                try:
                    self._mibs.insert_one(
                        dict(content=mib_file.read(), filename=filename, _id=filename)
                    )
                except Exception as e:
                    logger.error(
                        f"Error happened during insert mib files {filename} into mongo: {e}"
                    )

    def search_oid(self, oid):
        """
        Search mib file based on oid
        @param oid: oid, format: "1, 3, 6, 1, 4, 1, 2356, 11, 0, 0, 10000"
        @return mib filename
        """
        data = self._mibs.find_one({"content": {"$regex": oid}})
        if data:
            return data["filename"]
        else:
            return None

    def delete_mib(self, filename):
        """
        Delete mib files based on filename
        @param filename: mib filename
        """
        self._mibs.delete_many({"filename": {"$regex": filename}})

    def clear(self):
        """
        Clear the collection
        """
        self._mibs.remove()


class OidsRepository:
    def __init__(self, mongo_config):
        self._client = MongoClient(
            os.environ["MONGO_SERVICE_SERVICE_HOST"],
            int(os.environ["MONGO_SERVICE_SERVICE_PORT"]),
        )
        if os.environ.get("MONGO_USER"):
            self._client.admin.authenticate(
                os.environ["MONGO_USER"],
                os.environ["MONGO_PASS"]
            )
        self._oids = self._client[mongo_config["database"]][mongo_config["collection"]]

    def contains_oid(self, oid):
        return self._oids.find({"oid": oid}).count()

    def add_oid(self, oid):
        self._oids.insert_one({"oid": oid})

    def delete_oid(self, oid):
        self._oids.delete_many({"oid": oid})

    def clear(self):
        self._oids.remove()
