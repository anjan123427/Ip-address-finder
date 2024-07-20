import ipaddress
import sys

if len(sys.argv) != 2:
    print("Usage: python3 get_ip_range.py <CIDR>")
    sys.exit(1)

cidr = sys.argv[1]
network = ipaddress.ip_network(cidr)

for ip in network:
    print(ip)
