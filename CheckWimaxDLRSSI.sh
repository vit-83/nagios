#!/bin/sh

SNMPout=`python2.7 /root/vit/GetSnmpData.py $1 $2 $3 | tr -d "\n"`
WimaxDLRSSI=$SNMPout

if [ $WimaxDLRSSI -lt -8500 ]
then
	echo "CRITICAL - DL RSSI = $WimaxDLRSSI | value=$WimaxDLRSSI"
	exit 2
else
        echo "OK - DL RSSI = $WimaxDLRSSI | value=$WimaxDLRSSI"
	exit 0
fi

