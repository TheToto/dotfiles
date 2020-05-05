#!/bin/sh
export $(xpub)

interface=$1
state=$2

function notif() {
    su ${XUSER} -c "notify-send $2 \"$1\""
}



if [ "$state" == "up" ] || [ "$state" == "down" ]; then
    notif "$*"
else
    notif "$*"
fi
