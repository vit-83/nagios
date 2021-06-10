#!/bin/sh

SNMPCommunity="XzOg52%$" 
SNMPWriteCommunity="XzOg52%$"
LicenceLevel="full"
SNMPVersion="2c"
SNMPRetry="2"
SNMPTimeOut="10"


for filename in `ls -1 /usr/local/etc/nagios/switches/ | grep -v old`
do
        IP=`grep address /usr/local/etc/nagios/switches/$filename | grep -vxE '[[:blank:]]*([#;].*)?' | cut -f4 | tr -d '\n'`
	ImportData="$IP,$LicenceLevel,$SNMPVersion,$SNMPCommunity,$SNMPWriteCommunity,$SNMPRetry,$SNMPTimeOut"
	echo $ImportData
done

