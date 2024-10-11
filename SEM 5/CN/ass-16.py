import socket

def dns_lookup():
    print("DNS Lookup Tool")
    print("1. Lookup URL from IP address")
    print("2. Lookup IP address from URL")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        ip_address = input("Enter the IP address: ")
        try:
            url = socket.gethostbyaddr(ip_address)[0]
            print(f"The URL for IP address {ip_address} is: {url}")
        except socket.herror:
            print("No URL found for the given IP address.")
    
    elif choice == '2':
        url = input("Enter the URL: ")
        try:
            ip_address = socket.gethostbyname(url)
            print(f"The IP address for URL {url} is: {ip_address}")
        except socket.gaierror:
            print("Invalid URL or could not resolve the URL.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    dns_lookup()
