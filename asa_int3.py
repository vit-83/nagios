#!/usr/local/bin/python

##
##  Arguments:	1 - ip address; 2 - interface; 3 - bandwidth in bits/s; 
##		4 - warning in %; 5 - critical in %
##

import sys
#import datetime
import os
import pexpect
import traceback
import subprocess
import re
import random

status = { 'OK' : 0 , 'WARNING' : 1, 'CRITICAL' : 2 , 'UNKNOWN' : 3}

band = int(sys.argv[3])
warn = (int(sys.argv[4]))
warn = warn * band / 100
crit = (int(sys.argv[5]))
crit = crit * band / 100
#print "band {0} warn {1} crit {2}".format(band,warn,crit)

ip = sys.argv[1]
interface = sys.argv[2]
comm = 'sh int {0} | inc 1 min.+bytes'.format(interface)
r = random.randint(0,100)
#ip = "10.2.246.2"

user = "nagstat"
secret = ""
enable_pw = ""

#port = "fa0/0"
#port_ip = "192.168.6.10 255.255.255.0"
#verbose = 1
log_f="/tmp/exp_log.{0}_{1}".format(ip,r)

def check_ip(ip):
    limbo = open(os.devnull, "wb")
    result = subprocess.Popen(["ping", "-c", "2", "-t", "1000", ip],
        stdout=limbo, stderr=limbo).wait()
    return result

# def command_execute()

result = check_ip(ip)
if result:
    print "CRITICAL - HOST not respond"
    sys.exit(status['CRITICAL'])
else:
    exp_log = open(log_f, "w")
    try:
        try:
            child = pexpect.spawn('ssh %s@%s -oStrictHostKeyChecking=no' % (user, ip))
            child.logfile = exp_log
            child.timeout = 15
            child.expect('assword:')
        except pexpect.TIMEOUT:
#            raise OurException("Couldn't log on to the switch")
            exp_log.close()
            os.remove(log_f)
            print "Couldn't log on to the device"
            sys.exit(status['UNKNOWN'])
        child.sendline(secret)
        i=child.expect(['>', '#'])
        if i==0:
            child.sendline('terminal length 0')
            child.expect('>')
            child.sendline('enable')
            child.expect('assword:')
            child.sendline(enable_pw)
            child.expect('#')
        if i==1:
            child.sendline('terminal length 0')
            child.expect('#')
#        child.sendline('sh int fa0/0 | inc _rate_')
        child.sendline(comm)
#        child.expect('end')
        child.expect('#')
        child.sendline('quit')
    except (pexpect.EOF, pexpect.TIMEOUT) as e:
#        print e
        exp_log.close()
        os.remove(log_f)
        print "UNKNOWN - Error in connection or  execution command"
        sys.exit(status['UNKNOWN'])
exp_log.close()

exp_log = open(log_f, "r")
pattern = re.compile("(\d+) bytes")
matches = []
for line in exp_log:
    matches += pattern.findall(line)
exp_log.close()
os.remove(log_f)

in_rate = int(matches[0])*8
out_rate = int(matches[1])*8


if (in_rate >= crit) or (out_rate >= crit):
    print "STATUS CRITICAL - IN rate {0} bps, OUT rate {1} bps | in={0} out={1}".format(in_rate,out_rate)
    sys.exit(status['CRITICAL'])

if (in_rate >= warn) or (out_rate >= warn):
    print "STATUS WARNING - IN rate {0} bps, OUT rate {1} bps | in={0} out={1}".format(in_rate,out_rate)
    sys.exit(status['WARNING'])

print "STATUS OK - IN rate {0} bps, OUT rate {1} bps | in={0} out={1}".format(in_rate,out_rate)
sys.exit(status['OK'])
