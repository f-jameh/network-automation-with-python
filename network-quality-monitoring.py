# In the name of God

import subprocess
import time
import matplotlib.pyplot as plt

# Configuration
host = '4.2.2.4'  # Google's DNS server, change as needed
duration = 10  # Total time to run the pings in seconds
interval = 1   # Time between pings in seconds
timeout = 2    # Ping timeout in seconds

response_times = []

start_time = time.time()

while time.time() - start_time < duration:
    # Run the ping command
    result = subprocess.run(['ping', '-c', '1', '-W', str(timeout), host], stdout=subprocess.PIPE, text=True)
    output = result.stdout
    
    # Extract the time from the output
    if 'time=' in output:
        time_ms = float(output.split('time=')[1].split(' ')[0])
        response_times.append(time_ms)
    else:
        response_times.append(None)  # None or a high value to indicate timeout/no response
    
    time.sleep(interval)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(response_times, marker='o', linestyle='-', color='b')
plt.title(f"Ping Response Times Over {duration} Seconds of {host}")
plt.xlabel('Ping Number')
plt.ylabel('Response Time (ms)')
plt.grid(True)
plt.show()
