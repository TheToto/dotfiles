#!/bin/sh

export $(xpub)

su "${XUSER}" -s /bin/sh -c "/usr/bin/dunstify -C 5775"
