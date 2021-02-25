from flask import Flask, request, abort, jsonify, send_from_directory
from flask_autoindex import AutoIndex
import os
import yaml 
from splunk_connect_for_snmp_mib_server.mongo import MibsRepository, OidsRepository
from splunk_connect_for_snmp_mib_server.translator import Translator
import logging

logger = logging.getLogger(__name__)

class MibServer:
    def __init__(self, args, server_config):
        self._args = args
        self._server_config = server_config
        self._translator = Translator(server_config)
        self._flask_app = self.build_flask_app()
    
    def build_flask_app(self):    
        app = Flask(__name__)

        ppath = self._server_config["snmp"]["mibs"]["mibs_path"]

        files_index = AutoIndex(app, ppath, add_url_rules=False)

        @app.route('/')
        def hello():
            return "Hello, This is SNMP MIB server!"

        # Custom indexing
        @app.route('/files/')
        @app.route('/files/<path:path>')
        def autoindex(path='.'):
            print(f"path: {path}")
            return files_index.render_autoindex(path)

        # Translate oid
        @app.route('/translation', methods=['POST'])
        def translator():
            print(request.json)
            var_binds = request.json.get('var_binds')
            print(f"type of var_binds: {type(var_binds)}")
            print(f"var_binds: {var_binds}")
            return self._translator.format_trap_event(var_binds)
        
        return app
    
    def run_mib_server(self):
        # TODO poetry run fails when debug=True
        self._flask_app.run(host="0.0.0.0",port=self._args.port)

