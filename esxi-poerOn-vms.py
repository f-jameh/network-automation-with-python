# in the name of GOD

import paramiko
import time

# put all vms world_ids that must be powered-on in a list
world_ids = [264,265,275,276,278,279,280]

# create an object for ssh
ssh_client = paramiko.SSHClient()

# determine authentication policy (suitable for linux)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# give the object hostname/username/password
# in this example hostname is 'vms.fartakec.com', username is 'root' and password is 'P@ssw0rd'
ssh_client.connect(hostname='vms.fartakec.com', username='root', password='P@ssw0rd')


# powerOn all Vms by a loop
for vm in world_ids:
    print ('power on ' , vm)
    vm = str(vm)    
    stdin, stdout, stderr = ssh_client.exec_command('vim-cmd  vmsvc/power.on ' + vm')
    output = stdout.read().decode()
    print(output)
    time.sleep(1)
else:
    print('all vms are powerd-on')
