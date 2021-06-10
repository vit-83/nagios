#!/bin/sh

SNMPout=`/usr/local/libexec/nagios/check_snmp -H $1 -o $2 -C snmp4lotus | cut -d' ' -f4 | tr -d "\n"`
DiskUsage="$((SNMPout * 4096))"

SNMPout=`/usr/local/libexec/nagios/check_snmp -H $1 -o $3 -C snmp4lotus | cut -d' ' -f4 | tr -d "\n"`
DiskSum="$((SNMPout * 4096))"

DiskFree="$((DiskSum - DiskUsage))"


if [ $DiskFree -lt 21474836480 ]
then
	echo "CRITICAL - Disk Free = $DiskFree bytes | value=$DiskFree"
	exit 2
else
        echo "OK - Disk Free = $DiskFree bytes | value=$DiskFree"
	exit 0
fi

