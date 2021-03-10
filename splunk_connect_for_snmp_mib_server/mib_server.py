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
        ppath = os.environ['MIBS_SERVER_URL']
        files_index = AutoIndex(app, ppath, add_url_rules=False)

        @app.route('/')
        def hello():
            return "Hello, This is SNMP MIB server!"

        # Custom indexing
        @app.route('/files/')
        @app.route('/files/<path:path>')
        def autoindex(path='.'):
            logger.debug(f"path: {path}")
            return files_index.render_autoindex(path)

        # Translate oid
        @app.route('/translation', methods=['POST'])
        def translator():
            logger.debug(request.json)
            var_binds = request.json.get('var_binds')
            metric = request.args.get("metric")
            logger.debug(f"type of var_binds: {type(var_binds)}")
            logger.debug(f"var_binds: {var_binds}")
            logger.debug(f"type of metric: {str(metric)} -- metric: {metric}")
            if metric == "True":
                # TODO
                # If metric is true, var_binds just has one 
                var_bind = var_binds[0]
                result = self._translator.format_metric_data(var_bind)                
            else:
                result = self._translator.format_trap_event(var_binds)
            return result
        
        return app
    
    def run_mib_server(self):
        # TODO poetry run fails when debug=True
        self._flask_app.run(host="0.0.0.0",port=self._args.port)

