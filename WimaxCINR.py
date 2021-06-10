#CINR
from pysnmp.hlapi import *
import sys


SNMP_HOST = sys.argv[1]
SNMP_COMMUNITY = sys.argv[2]
SNMP_MIB = sys.argv[3]

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(SNMP_COMMUNITY),
           UdpTransportTarget((SNMP_HOST, 161)),
           ContextData(),
           ObjectType(ObjectIdentity(SNMP_MIB)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
        for varBind in varBinds:
                for line in varBind:
                        value = line

value = float(value)/100

DLCINR = value

if DLCINR < 15:
        print "CRITICAL - DL CINR =", DLCINR," | value=",DLCINR

else:
    print "OK - DL CINR =", DLCINR," | value=",DLCINR
 
