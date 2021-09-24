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

from unittest import TestCase

from splunk_connect_for_snmp_mib_server.profiles import merge_profiles


class ProfileLoaderTest(TestCase):
    def test_multiple_files_merging(self):
        merged_profiles = merge_profiles("tests/profiles/two_profiles", "profiles")[
            "profiles"
        ]

        assert len(merged_profiles.keys()) == 4
        assert "basev1" in merged_profiles.keys()
        assert "basev2" in merged_profiles.keys()
        assert "basev1l2" in merged_profiles.keys()
        assert "basev2l2" in merged_profiles.keys()

    def test_one_file(self):
        merged_profiles = merge_profiles("tests/profiles/one_profile", "profiles")[
            "profiles"
        ]

        assert len(merged_profiles.keys()) == 2
        assert "basev1" in merged_profiles.keys()
        assert "basev1l2" in merged_profiles.keys()

    def test_same_name_profiles_were_overwritten_in_alphabetical_order(self):
        merged_profiles = merge_profiles("tests/profiles/same_name_profiles", "profiles")[
            "profiles"
        ]

        assert len(merged_profiles.keys()) == 2
        assert "basev1" in merged_profiles.keys()
        assert "basev1l2" in merged_profiles.keys()

        assert merged_profiles["basev1"]["frequency"] == 60
        assert merged_profiles["basev1l2"]["frequency"] == 120

    def test_malformed_file_is_ignored(self):
        merged_profiles = merge_profiles(
            "tests/profiles/malformed_profile", "profiles"
        )["profiles"]

        assert len(merged_profiles.keys()) == 2
        assert "basev2" in merged_profiles.keys()
        assert "basev2l2" in merged_profiles.keys()
