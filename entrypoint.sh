#!/usr/bin/env bash
#
# Copyright 2021 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# These path variables allow for a singl

# SIGTERM-handler
term_handler() {
# SIGTERM on valid PID; return exit code 0 (clean exit)
  if [ $pid -ne 0 ]; then
    echo Terminating ...
    kill -SIGTERM ${pid}
    wait ${pid}
    exit $?
  fi
# 128 + 15 -- SIGTERM on non-existent process (will cause service failure)
  exit 143
}

# SIGHUP-handler
hup_handler() {
  if [ $pid -ne 0 ]; then
    echo Reloading ...
    kill -SIGHUP ${pid}
  fi
}

# SIGQUIT-handler
quit_handler() {
  if [ $pid -ne 0 ]; then
    echo Quitting ...
    kill -SIGQUIT ${pid}
    wait ${pid}
  fi
}

trap 'kill ${!}; hup_handler' SIGHUP
trap 'kill ${!}; term_handler' SIGTERM
trap 'kill ${!}; quit_handler' SIGQUIT



echo starting sc4-snmp-mib-server
sc4snmp-mib-server $@ &
pid="$!"
sleep 2
if ! ps -p $pid > /dev/null
then
   echo "failed to start; exiting..."
   if [ "${DEBUG_CONTAINER}" != "yes" ]
   then
     wait ${pid}
     exit $?
  else
    tail -f /dev/null
  fi
   # Do something knowing the pid exists, i.e. the process with $PID is running
fi

# Wait forever
wait ${pid}
exit $?