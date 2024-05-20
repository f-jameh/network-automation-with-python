# in the name of God

# import library
from netmiko import ConnectHandler, file_transfer #file_transfer only for scp
import datetime                                   #for create backup file name
# create a dictionary for target device
device1 = {
    "device_type": "cisco_ios",
    "host": "10.34.0.1",        #hostname or ip address of device
    "username": "user1",        #username for ssh
    "password": "******",       #password of the user
    "port": 22,                 #optional, to determine the port, default is 22
    "session_log": "log.txt"    #optional, Enable session logging for troubleshooting

}

####### optional: ssh using ssh_key########
key_file = "~/.ssh/test_rsa"    #address to public key
device1 = {
    "device_type": "cisco_ios",
    "host": "device1.test.com",
    "username": "user1",
    "use_keys": True,
    "key_file": key_file,
}
###########################################

# show prompt with context manager (automatically 'disconnect()')
with ConnectHandler(**device1) as net_connect:
    print(net_connect.find_prompt())


# connect to multiple device
# create a dictionary for each device
cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.test.com",
    "username": "pyclass",
    "password": "*****",
}

cisco2 = {
    "device_type": "cisco_ios",
    "host": "cisco2.test.com",
    "username": "pyclass",
    "password": "*****",
}

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "ns1.test.com",
    "username": "pyclass",
    "password": "*****",
}

srx1 = {
    "device_type": "juniper_junos",
    "host": "juniper1.test.com",
    "username": "user",
    "password": "*****",
}

# create a list for all devices
ip_list = [cisco1,cisco2,nxos1,srx1
           ]
for device in (cisco1, cisco2, nxos1, srx1):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()

# read ips from a text file(each ip is written in one line without any extra characters)
filename = "ip_list"    # Define the path to the file


with open(filename, 'r') as file:   # Open the file and read the IP addresses
    for line in file:
        ip = line.strip()  # Remove any whitespace or newline characters
        print('connectiing to ' ,  ip)  # optional: Display the IP addres
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": "pyclass",
            "password": "*****",
        }
    # show prompt with context manager
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
        
# read ips from a csv file:
import pandas as pd
df = pd.read_csv('Desktop/ips.csv')
for i in df.iloc[:,1]: # consumed ip addresses are stored in second column
    ip = i
    print(f'connectiing to {ip}')
    device = {
           "device_type": "cisco_ios",
           "host": ip,
           "username": "farhad",
           "password": "1234",
       }
    with ConnectHandler(**device) as net_connect:
       print(net_connect.find_prompt())

# execute commands in linux and in basic-environment in cisco (e.g: show)

# Show command that we execute
command = "show ip int brief"

with ConnectHandler(**device1) as net_connect:
    output = net_connect.send_command(command)

print()
print(output)
print()

# change config in cisco (automatically wr)

commands = ["interface loopback 1","ip addr 1.1.1.1 255.0.0.0"]

with ConnectHandler(**device1) as net_connect:
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

print()
print(output)
print()

# change configs from a file

# create a file with set of configs to apply, and an variable for config-file name/path:
cfg_file = "cisco-config.txt"

# create an object for conncting to device with ConnectHandler
with ConnectHandler(**device1) as net_connect:
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()

print()
print(output)
print()

# backup startup config to a file
command = "show startup-config"

with ConnectHandler(**device1) as net_connect:
    backupname = net_connect.find_prompt().strip('#') + '_' + str(datetime.date.today())
    output = net_connect.send_command(command)

# Write the output to a file
with open(backupname, 'w') as file:
    file.write(output)

print("Running configuration has been saved to" , backupname) #optional





########################## scp with netmiko

# scp parameters
source_file = "test1.txt"
dest_file = "test1.txt"
direction = "put"
file_system = "flash:"

ssh_conn = ConnectHandler(**device1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,    # Force an overwrite of the file if it already exists
)

print(transfer_dict)



###########################################################################
# optional: connect without with and diteclty

# create an object for ConnectHandler
net_connect = ConnectHandler(**device1)

# show prompt without with
print(net_connect.find_prompt())
device1.disconnect()

# enable mode (in cisco) without with
net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()

# change config 
net_connect.enable()
print(net_connect.find_prompt())
net_connect.send_config_set(commands)
net_connect.disconnect()
###########################################################################

# appendix: config file sample. (below content must be saved in separate file)
# configure terminal 
# ip access-list standard snmp-service
#   remark zabbix
#   permit 10.34.176.250
#   permit 10.34.176.251
#   permit 10.34.176.252
  
# snmp-server view ro_view iso included
# snmp-server view rw_view iso included

# snmp-server group ro_group v3 priv read ro_view access snmp-service
# snmp-server group rw_group v3 priv read rw_view access snmp-service

# snmp-server user zabbix-ro ro_group v3 auth sha P@ssw0rd priv aes 128 P@ssw0rd access snmp-service
# snmp-server user zabbix-rw rw_group v3 auth sha P@ssw0rd priv aes 128 P@ssw0rd access snmp-service











