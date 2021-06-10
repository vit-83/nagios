#!/usr/local/bin/python


import sys
#import datetime
import os
import pexpect
import traceback
import subprocess
import re
import random


prim_ip = sys.argv[1]
sec_ip = sys.argv[2]
state = sys.argv[3]
#interface = sys.argv[2]
#comm = 'sh int {0} | inc 1 min.+bytes'.format(interface)
if state == "DOWN":
    comm1 = 'clear crypto ikev1 sa {0}'.format(prim_ip)
    comm2 = 'clear crypto ipsec sa peer {0}'.format(prim_ip)
elif state == "UP":
    comm1 = 'clear crypto ikev1 sa {0}'.format(sec_ip)
    comm2 = 'clear crypto ipsec sa peer {0}'.format(sec_ip)
else:
    sys.exit(0)

r = random.randint(0,1000)
ip = "10.2.254.2"
#ip = "10.2.246.2"

user = "nagstat"
secret = "b@Rd&7M0n"
enable_pw = "b@Rd&7M0n"

log_f="/tmp/exp_log.{0}_{1}".format(ip,r)

def check_ip(ip):
    limbo = open(os.devnull, "wb")
    result = subprocess.Popen(["ping", "-c", "2", "-t", "1000", ip],
        stdout=limbo, stderr=limbo).wait()
    return result

# def command_execute()

result = check_ip(ip)
if result:
    sys.exit(0)
else:
#    print "First command - {0}".format(comm1)
#    print "Second command - {0}".format(comm2)
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
#            print "Couldn't log on to the device"
            sys.exit(0)
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
#        child.sendline('conf t')
#        child.expect('#')
        child.sendline(comm1)
        child.expect('#')
        child.sendline(comm2)
        child.expect('#')
        child.sendline('quit')
    except (pexpect.EOF, pexpect.TIMEOUT) as e:
#        print e
        exp_log.close()
        os.remove(log_f)
#        print "UNKNOWN - Error in connection or  execution command"
        sys.exit(0)
exp_log.close()
os.remove(log_f)
