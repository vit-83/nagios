import netmiko
from netmiko import ConnectHandler


cmd = 'show inventory'
cisco_ios = {
        'device_type': 'cisco_ios',
        'ip': '10.2.246.5',
        'username': 'nagstat',
        'password': 'b@Rd&7M0n',
        'port': 22,
        'global_delay_factor': 4,
    }

net_connect = ConnectHandler(**cisco_ios)
cmdout = net_connect.send_command(cmd)
net_connect.disconnect()
print cmdout

