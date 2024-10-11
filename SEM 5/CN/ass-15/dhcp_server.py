from scapy.all import *
import random
import time

# Define the DHCP server's IP and the range of IP addresses
DHCP_SERVER_IP = "192.168.1.100"  # Change to your server's IP
IP_POOL = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]  # Available IP addresses
leased_ips = []  # To keep track of leased IPs

def dhcp_serve(packet):
    # Check if it's a DHCP Discover packet
    if packet[DHCP].options[0][1] == 1:  # DHCP Discover
        print("Received DHCP Discover")
        
        # Select an available IP address from the pool
        ip_address = None
        for ip in IP_POOL:
            if ip not in leased_ips:
                ip_address = ip
                leased_ips.append(ip)
                break

        if ip_address:
            print(f"Offering IP Address: {ip_address}")
            offer = (
                Ether(dst="ff:ff:ff:ff:ff:ff") /
                IP(src=DHCP_SERVER_IP, dst="255.255.255.255") /
                UDP(sport=67, dport=68) /
                BOOTP(op=2, yiaddr=ip_address, siaddr=DHCP_SERVER_IP, xid=packet[BOOTP].xid) /
                DHCP(options=[("message-type", "offer"),
                              ("server_id", DHCP_SERVER_IP),
                              ("lease_time", 3600),  # 1 hour
                              ("subnet_mask", "255.255.255.0"),
                              ("router", DHCP_SERVER_IP),
                              ("end")])
            )
            sendp(offer, iface="eth0")  # Change to your interface
            print("Sent DHCP Offer")

    # Handle DHCP Request
    elif packet[DHCP].options[0][1] == 3:  # DHCP Request
        requested_ip = packet[DHCP].options[2][1]  # Requested IP address
        print(f"Received DHCP Request for IP: {requested_ip}")

        if requested_ip in leased_ips:
            ack = (
                Ether(dst="ff:ff:ff:ff:ff:ff") /
                IP(src=DHCP_SERVER_IP, dst="255.255.255.255") /
                UDP(sport=67, dport=68) /
                BOOTP(op=2, yiaddr=requested_ip, siaddr=DHCP_SERVER_IP, xid=packet[BOOTP].xid) /
                DHCP(options=[("message-type", "ack"),
                              ("server_id", DHCP_SERVER_IP),
                              ("lease_time", 3600),
                              ("subnet_mask", "255.255.255.0"),
                              ("router", DHCP_SERVER_IP),
                              ("end")])
            )
            sendp(ack, iface="eth0")  # Change to your interface
            print(f"Sent DHCP ACK for IP: {requested_ip}")

def main():
    print("DHCP Server is running...")
    sniff(filter="udp and (port 67 or port 68)", prn=dhcp_serve, store=0)

if __name__ == "__main__":
    main()
