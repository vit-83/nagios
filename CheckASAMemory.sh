#!/bin/sh

FreeMem=`/usr/local/libexec/nagios/check_snmp -H $1 -o $2 -C XzOg52%$ | cut -d' ' -f4 | tr -d "\n"`

if [ "$FreeMem" -lt "$3" ] 
then
	echo "CRITICAL - Free Memory = $FreeMem bytes | value=$FreeMem"
	exit 2
else
        echo "OK - Free Memory = $FreeMem bytes | value=$FreeMem"
	exit 0
fi

