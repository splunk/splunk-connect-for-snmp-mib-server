import sys
sys.path.append('../')
from flask_server.mongo import MibsRepository
import os


def main():
    # mongo_config = {'host': 'localhost', 'port': 27017, 'database': 'test', 'collection': 'mibs'}
    mongo_config = {'host': 'localhost', 'port': 27017, 'database': 'files', 'collection': 'mib_files'}
    mongo = MibsRepository(mongo_config)

    # mongo.clear()

    # # Upload 5 mib files in /mibs/test to mongo
    # mib_files_dir = os.path.join(os.getcwd(), "..", "mibs","pysnmp")
    # mongo.upload_files(mib_files_dir)

    # Search mib files based on oid
    # oid = "1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 1"
    oid = "1, 3, 6, 1, 4, 1, 1978, 2, 14, 1, 1, 1"
    filename = mongo.search_oid(oid)
    print(filename)
    
    # # Delete one specifc file
    # if filename:
    #     mongo.delete_mib(filename)
    #     print(mongo.search_oid(oid))

    # # Delete multiple files
    # filename_regex="A3COM"
    # mongo.delete_mib(filename_regex)


if __name__ == '__main__':
    main()