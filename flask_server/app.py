from flask import Flask, request, abort, jsonify, send_from_directory
from flask_autoindex import AutoIndex
import os
import yaml 
import sys
sys.path.append('../')
from flask_server.mongo import MibsRepository, OidsRepository
from flask_server.translator import Translator


print(os.path.join(os.getcwd(), "..", "mibs"))
ppath = os.path.join(os.getcwd(), "..", "mibs")


# Read config file
config_file = os.path.join(os.getcwd(), "..", "config.yaml")
with open(config_file, "r") as yamlfile:
    server_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

#Init Translator
snmp_translator = Translator(server_config)

# Init Mongo Client
# mongo_config = {'host': 'localhost', 'port': 27017, 'database': 'files', 'collection': 'mib_files'}
# mib_mongo_config = server_config["mongo"]["mib"]
# oid_mongo_config = server_config["mongo"]["oid"]

# mib_collection = MibsRepository(mib_mongo_config)
# oid_collection = OidsRepository(oid_mongo_config)
# print(f"========={mib_collection} -- {oid_collection}========")




app = Flask(__name__)
# AutoIndex(app, browse_root=ppath) 

files_index = AutoIndex(app, ppath, add_url_rules=False)

@app.route('/')
def hello():
    return "Hello, This is SNMP MIB server!"

@app.route('/test')
def test():
    name = request.args.get('name')
    return f"This is {name}'s test"

# Custom indexing
@app.route('/files/')
@app.route('/files/<path:path>')
def autoindex(path='.'):
    print(f"path: {path}")
    # if '/' in path and '.' in path.split('/')[-1]:
    #     filename = path.split('/')[-1]
    #     print(f"filename: {filename}")
    #     dirpath = os.path.join(ppath, path.split('/')[-2])
    #     print(f"dirpath: {dirpath}")
    #     return files_index.render_autoindex(path),send_from_directory(dirpath, filename, as_attachment=True)
    return files_index.render_autoindex(path)

# # Search mib files based on oid
# @app.route('/search/mib', methods=['GET'])
# def search_mib_file():
#     oid = request.args.get('oid')
#     return mib_collection.search_oid(oid)

# Translate oid
@app.route('/translation', methods=['POST'])
def translator():
    # how to keep the var_bins as a var_binds object
    print(request.json)
    var_binds = request.json.get('var_binds')
    print(f"type of var_binds: {type(var_binds)}")
    print(f"var_binds: {var_binds}")
    return snmp_translator.format_trap_event(var_binds)



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)