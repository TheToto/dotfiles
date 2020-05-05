#!/bin/sh

export $(xpub)

su "${XUSER}" -s /bin/sh -c "/usr/bin/dunstify -u critical -r 5775 pam \"Reconnaissance de l'empreinte digitale en cours...\""
