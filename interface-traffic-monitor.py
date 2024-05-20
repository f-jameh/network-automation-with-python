# In the name of God

import psutil
import time
import matplotlib.pyplot as plt

# Initial setup
interface = 'wlp1s0'  # Change this to your interface
duration = 10  # Monitoring time in seconds
interval = 5  # Interval between checks in seconds
times = []
sent_rates = []
recv_rates = []

def get_net_io(interface):
    stats = psutil.net_io_counters(pernic=True)
    io_stats = stats.get(interface, stats.get(interface))  # Adjust the default interface as needed
    return (io_stats.bytes_sent, io_stats.bytes_recv)

# Initial data for comparison
initial_sent, initial_recv = get_net_io(interface)

start_time = time.time()

# Collect data
while (time.time() - start_time) < duration:
    time.sleep(interval)
    current_sent, current_recv = get_net_io(interface)
    
    # Calculate the send and receive rates (kilobits per second)
    sent_rate = ((current_sent - initial_sent) * 8) / interval / 1000
    recv_rate = ((current_recv - initial_recv) * 8) / interval / 1000
    
    # Update initial values for the next interval
    initial_sent, initial_recv = current_sent, current_recv

    # Store rates for plotting
    sent_rates.append(sent_rate)
    recv_rates.append(recv_rate)
    times.append(time.time() - start_time)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(times, sent_rates, label='Upload (kilobits per second)')
plt.plot(times, recv_rates, label='Download (kilobits per second)')
plt.xlabel('Time (seconds)')
plt.ylabel('Bandwidth (kilobits per second)')
plt.title('Bandwidth Usage Over Time')
plt.legend()
plt.grid(True)
plt.show()
