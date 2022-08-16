
#importing netmiko and getpass
from netmiko import Netmiko
from getpass import getpass

##info required to connect to cisco device
cisco1 = {
    'host': 'cisco1.twb-tech.com', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'cisco_ios',
}


## creating a Netmiko object with the informationprovided in cisco1
#net_connect = Netmiko(**cisco1)

##saving 'show ip int brief' in side the variable command
command = 'show ip int brief'

print()
##shows the prompt sw1> 
print(net_connect.find_prompt())

#saves the result of the send_command method into output
output = net_connect.send_command(command)


net_connect.disconnect()
print(output)
print()



##########################################################################
##########################################################################

# #!/usr/bin/env python
# from netmiko import Netmiko
# from getpass import getpass

# cisco1 = {
#     'host': 'cisco1.twb-tech.com', 
#     'username': 'pyclass', 
#     'password': getpass(), 
#     'device_type': 'cisco_ios_telnet',
# }

# net_connect = Netmiko(**cisco1)
# print(net_connect.send_command("show ip arp"))
# net_connect.disconnect()


# ##########################################################################
# ##########################################################################

#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

device = {
    'host': 'srx1.twb-tech.com', 
    'username': 'pyclass', 
    'password': getpass(), 
    'device_type': 'juniper_junos',
}

#command to send to the jupiter divice 
#sets syslog archive size to 240k
commands = [
    'set system syslog archive size 240k files 3 '
]

net_connect = Netmiko(**device)

print()
print(net_connect.find_prompt())
output = net_connect.send_config_set(commands, exit_config_mode=False)
##The commit configuration mode command enables you to save the device configuration 
# changes to the configuration database and to activate the configuration on the device
output += net_connect.commit(and_quit=True)
print(output)
print()

net_connect.disconnect()