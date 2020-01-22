#!/bin/sh
set -e
if [ "$1" = "unitd" ]; then
    /usr/sbin/unitd --modules /usr/lib/unit/modules --control unix:/run/control.unit.sock &&
    curl -X PUT -d @/unit_files/config.json --unix-socket /run/control.unit.sock http://localhost/config/ &&
    kill -TERM `/bin/cat /run/unit.pid` &&
    while [ -S /var/run/control.unit.sock ]; do echo "$0: Waiting for control socket to be removed..."; /bin/sleep 0.1; done &&
    echo "$0: Unit initial configuration complete; ready for start up..."
else
    echo "Configuration is not applied"
fi
exec "$@"