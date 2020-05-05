#/bin/sh

files="/etc/NetworkManager/dispatcher.d/98-thetoto.sh
       /etc/pam.d/fprint-auth
       /etc/pulse/client.conf
       /etc/udev/rules.d/98-thetoto.rules
       /etc/mpd.conf
       /etc/environment"

SCRIPT_PATH=$(realpath "$0")
DIR_PATH=$(dirname "$SCRIPT_PATH")

for file in $files; do
    mkdir -p $(dirname "$DIR_PATH$file") && cp "$file" "$DIR_PATH$file"
done
