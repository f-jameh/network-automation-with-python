# in the name of GOD

import paramiko

host='test.fartakec.com'     #hostname or ip address
user= 'user'            # username of host
password= 'P@ssw0rd'    # password of host
command='ls -alh > f1'  # command to be executed on host (combining of some commands is possible)


# create an object for ssh
ssh_client = paramiko.SSHClient()

# determine authentication policy
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# give the object hostname/username/passwor (in case of using password)
ssh_client.connect(hostname=host, username=user, password=password)

# # give the object hostname/username/path to rsa id key (in case of using rsa_authentication)
# ssh_client.connect(hostname=host, username='root', key_filename='d:\id_rsa.pub')


# execute command
stdin, stdout, stderr = ssh_client.exec_command(command)
output = stdout.read().decode()
print(output)
