import ipaddress

def get_ip_range(cidr):
    network = ipaddress.ip_network(cidr)
    return [str(ip) for ip in network]

# Example usage:
cidr = "192.168.1.0/24"
ip_range = get_ip_range(cidr)
print(ip_range)
