#!/bin/sh

SNMPout=`python2.7 /root/vit/GetSnmpData.py $1 $2 $3 | tr -d "\n"`
WimaxDLCINR=$SNMPout
#SNMPout=`/usr/local/libexec/nagios/check_snmp -H $1 -o $3 -C snmp4lotus | cut -d' ' -f4 | tr -d "\n"`
if [ $WimaxDLCINR -lt 500 ]
then
	echo "CRITICAL - DL CINR = $WimaxDLCINR | value=$WimaxDLCINR"
	exit 2
else
        echo "OK - DL CINR = $WimaxDLCINR | value=$WimaxDLCINR"
	exit 0
fi

