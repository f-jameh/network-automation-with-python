# In the name of God

from scapy.all import ARP, Ether, srp

# enter ip range for searching
target_ip = "10.10.10.0/24"

# Create ARP request
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# Print available hosts
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
for client in clients:
    print(f"IP Address: {client['ip']} | MAC Address: {client['mac']}")
