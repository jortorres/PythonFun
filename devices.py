import subprocess
import ipaddress

def ping_sweep(network):
    # Convert network to an IP network object
    net = ipaddress.ip_network(network, strict=False)
    active_ips = []

    # Iterate through all IPs in the network
    for ip in net.hosts():
        ip_str = str(ip)
        try:
            # Use subprocess to ping each IP
            output = subprocess.check_output(['ping', '-c', '1', '-t', '1', ip_str],
                                             stderr=subprocess.STDOUT,
                                             universal_newlines=True)

            # Check if the word 'icmp_seq' exists in the output, indicating a successful ping
            if "icmp_seq" in output:
                print(f"{ip_str} is active")
                active_ips.append(ip_str)
        except subprocess.CalledProcessError:
            # Ignore failed pings
            pass

    return active_ips

# Example usage
network = '192.168.1.0/24'  # Replace with your network range
active_ips = ping_sweep(network)
print("Active devices on the network:", active_ips)
