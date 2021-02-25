#!/usr/bin/env bash

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