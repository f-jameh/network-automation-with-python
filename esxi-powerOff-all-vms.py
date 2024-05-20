# in the name of GOD

import paramiko
import re
import time

# create an object for ssh
ssh_client = paramiko.SSHClient()

# determine authentication policy (suitable for linux)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# give the object hostname/username/password.
# in this example hostname is 'vms.fartakec.com', username is 'root' and password is 'P@ssw0rd'
ssh_client.connect(hostname='vms.fartakec.com', username='root', password='P@ssw0rd')

# give the command to execute in target os (3 variable is required to put result on it)
stdin, stdout, stderr = ssh_client.exec_command('esxcli vm process list')

# above line can be written by a variable too:
# command = 'esxcli vm process list'
# stdin, stdout, stderr = ssh_client.exec_command(command)


# show result by reading stdout and convert it to assci (decode)
output = stdout.read().decode()
print (output)

# separate all World ID of vms from output and put it into a list
world_ids = re.findall(r"World ID: (\d+)", output)
print (world_ids)

# shutdown all Vms by a loop
for vm in world_ids:
    print ('shuting down ' , vm)
    stdin, stdout,stderr = ssh_client.exec_command(f'esxcli vm process kill --type=soft --world-id={vm}')
    print (stdin)
    print (stdout.read().decode())
    time.sleep(5)
else:
    print('all vms are powerd-off')
    time.sleep(1)
    #shutdown host:
    stdin, stdout, stderr = ssh_client.exec_command('esxcli system maintenanceMode set -e true')
    print(stdin)
    print('out:\n')
    print(stdout.read().decode())
    time.sleep(1)
    stdin, stdout, stderr = ssh_client.exec_command('/sbin/shutdown.sh && /sbin/poweroff')
    print(stdin)
    print('out:\n')
    print(stdout.read().decode())
