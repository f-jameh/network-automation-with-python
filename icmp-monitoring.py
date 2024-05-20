# In the name of God

import subprocess
import time

time_interval = 2

# List of IP addresses to ping
ip1 = '10.10.10.1'
ip2 = '172.16.1.170'
ip3 = '172.16.2.1'
ip4 = '4.2.2.4'
ip5 = '1.1.1.1'

ip_addresses = [ip1, ip2, ip3, ip4, ip5]
print('Monitoring starts')

# while True:
#     for ip in ip_addresses:
#         # Ping the IP address (using '-c 1' for Linux/Mac or '-n 1' for Windows)
#         result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, text=True)
#         if '1 received' not in result.stdout:  # Check if the ping was successful
#             print(f"Alert: {ip} is not responding to ping.")
#     time.sleep(time_interval)  # Wait for seconds before the next round of pings

################## optional: show a massage when all hosts are available too #####
while True:
    all_hosts_up = True  # Assume all hosts are up initially
    for ip in ip_addresses:
        # Ping the IP address (using '-c 1' for Linux/Mac or '-n 1' for Windows)
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, text=True)
        if '1 received' not in result.stdout:  # Check if the ping was successful
            print(f"Alert: {ip} is not responding to ping.")
            all_hosts_up = False
    if all_hosts_up:
        print("All hosts are available.")
    time.sleep(time_interval)  # Wait for 5 seconds before the next round of pings
