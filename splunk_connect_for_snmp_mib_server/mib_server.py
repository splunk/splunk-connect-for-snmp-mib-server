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

from checksumdir import dirhash

import requests

from flask import Flask, request
from flask_autoindex import AutoIndex

from splunk_connect_for_snmp_mib_server.profiles import merge_profiles
from splunk_connect_for_snmp_mib_server.translator import Translator

logger = logging.getLogger(__name__)


class MibServer:
    def __init__(self, args, server_config):
        self._args = args
        self._server_config = server_config
        self._translator = Translator(server_config)
        self._flask_app = self.build_flask_app()
        self.data_format = {
            "METRIC": self._translator.format_metric_data,
            "TEXT": self._translator.format_text_event,
            "MULTIMETRIC": self._translator.format_multimetric_data,
        }

    def build_flask_app(self):
        app = Flask(__name__)
        mibs_path = self._server_config["snmp"]["mibs"]["mibs_path"]
        profiles_path = self._server_config["snmp"]["mibs"]["profiles_path"]
        files_index = AutoIndex(app, mibs_path, add_url_rules=False)

        @app.route("/")
        def hello():
            return "Hello, This is SNMP MIB server!"

        # Custom indexing
        @app.route("/files/")
        @app.route("/files/<path:path>")
        def autoindex(path="."):
            logger.debug(f"path: {path}")
            return files_index.render_autoindex(path)

        # Translate oid
        @app.route("/translation", methods=["POST"])
        def translator():
            logger.debug(request.json)
            var_binds = request.json.get("var_binds")
            data_format = request.args.get("data_format")
            logger.debug(
                f"type of var_binds: {type(var_binds)}\n"
                f"var_binds: {var_binds}\n"
                f"requested data format: {str(data_format)}"
            )
            if data_format in self.data_format:
                method = self.data_format.get(data_format)
                result = method(var_binds)
            else:
                result = self._translator.format_text_event(var_binds)
            return result

        @app.route("/profiles", methods=["GET"])
        def get_profiles():
            return merge_profiles(profiles_path, "profiles")

        return app

    def run_mib_server(self):
        # poetry run fails when debug=True
        self._flask_app.run(host="0.0.0.0", port=self._args.port)

    def notify_startup(self):
        profiles_hash = dirhash("profiles")
        params = {"profiles_hash": profiles_hash}
        requests.get(os.environ["SCHEDULER_REFRESH_URI"], params=params)
