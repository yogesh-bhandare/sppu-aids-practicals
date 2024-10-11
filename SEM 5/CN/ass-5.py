import ipaddress

def subnet_calculator(network, new_prefix):
    try:
        # Create the network object
        ip_network = ipaddress.ip_network(network, strict=False)
        print(f"\nOriginal Network: {ip_network}")
        print(f"Subnet Mask: {ip_network.netmask}")
        print(f"Total IP addresses: {ip_network.num_addresses}")

        # Subnetting the network
        subnets = list(ip_network.subnets(new_prefix=new_prefix))
        print(f"\nDividing network into subnets with /{new_prefix} prefix...")
        print(f"Number of subnets: {len(subnets)}")

        # Display subnet information
        for idx, subnet in enumerate(subnets, 1):
            first_ip = list(subnet.hosts())[0]
            last_ip = list(subnet.hosts())[-1]
            print(f"\nSubnet {idx}:")
            print(f"  Network Address: {subnet.network_address}")
            print(f"  Subnet Mask: {subnet.netmask}")
            print(f"  First Usable IP: {first_ip}")
            print(f"  Last Usable IP: {last_ip}")
            print(f"  Total Usable IPs: {subnet.num_addresses - 2}")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    # Original network (e.g., 192.168.1.0/24)
    network = "192.168.1.0/24"

    # New prefix (e.g., /26)
    new_prefix = 26

    # Call the subnet calculator function
    subnet_calculator(network, new_prefix)
