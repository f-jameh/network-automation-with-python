# in the name of GOD

import paramiko
import time

# put all vms world_ids that must be powered-on in a list
world_ids = [36,37,38]

# create an object for ssh
ssh_client = paramiko.SSHClient()

# determine authentication policy
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# an public/private rsa key must be created in advanced by: # ssh-keygen -t rsa , and store in a path, here:/tmp/rsa.
# the public key of this key_pair must be copied in authorized_keys in target and private is used below:
# in case of encrypted private key, the password of it must be given after the key as an string (here is '1234')

# give the private key of rsa public that had been copied to target previously
key = paramiko.RSAKey.from_private_key_file('/tmp/rsa/id_rsa', '1234')

# give the object hostname/username/key_file.
# in this example hostname is'vms.fartakec.com' and username is 'root'
ssh_client.connect(hostname='vms.fartakec.com', username='root', pkey=key)

############ or give private_key directly ########################
#ssh_client.connect(hostname='10.10.10.20', username='root', key_filename='/tmp/rsa/id_rsa')
########### this line can be replaced by 2 above lines ###########

# powerOn all Vms by a loop
for vm in world_ids:
    print ('power on ' , vm)
    vm = str(vm)
    stdin, stdout, stderr = ssh_client.exec_command('vim-cmd  vmsvc/power.on ' + vm)
    output = stdout.read().decode()
    print(output)
    time.sleep(1)
else:
    print('all vms are powerd-on')
