# in the name of God

# import libraries
import hashlib
import time

# Create a infinite loop for constant control
while True:
    real_digest = '8dc78af2b85e97660d6d8f0305ae0b005b138e3c'   #this is a variable for real fi>
    file_path = '/home/farhad/111.txt'                         #file path/name to verify
    file = open (file_path , 'rb').read()                      #opening file in binary
    calculated_digest = hashlib.sha1(file).hexdigest()         #hash calculating

    if calculated_digest == real_digest:
         print('file is ok!')
    else:
         print('danger!!! you are hacked')
    # create 2 sec pause between each check
    time.sleep(2)

