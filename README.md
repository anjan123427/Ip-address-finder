# IP Address Range Tool

This tool provides a function to get the range of IP addresses in a given CIDR block.

## Usage

```python
import ipaddress

def get_ip_range(cidr):
    network = ipaddress.ip_network(cidr)
    return [str(ip) for ip in network]

# Example usage:
cidr = "192.168.1.0/24"
ip_range = get_ip_range(cidr)
print(ip_range)

