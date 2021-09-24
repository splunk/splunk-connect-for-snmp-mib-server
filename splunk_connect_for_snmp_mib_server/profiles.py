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

from yaml.parser import ParserError

import yaml

logger = logging.getLogger(__name__)

def merge_profiles(directory, root_name):
    result = {}
    merged_profiles = {}
    for root, directories, files in os.walk(directory, topdown=False):
        for name in sorted(files):
            with open(os.path.join(root, name), "r") as stream:
                try:
                    data = yaml.safe_load(stream)
                    merged_profiles.update(data[root_name])
                except ParserError as pe:
                    logger.warning(f"Error while parsing file {os.path.join(root, name)} : {pe}")

    result[root_name] = merged_profiles
    return result
