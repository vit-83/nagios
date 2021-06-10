#!/bin/sh

#for filename in `ls -1 /usr/local/etc/nagios/routers/ | grep -v old` 
#do
#	grep  address /usr/local/etc/nagios/routers/$filename | grep -vxE '[[:blank:]]*([#;].*)?' | cut -f4
#done

for filename in `ls -1 /usr/local/etc/nagios/switches/ | grep -v old`
do
        grep address /usr/local/etc/nagios/switches/$filename | grep -vxE '[[:blank:]]*([#;].*)?' | cut -f4
done

