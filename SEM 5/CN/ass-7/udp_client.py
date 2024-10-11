import socket

def start_udp_client():
    host = '127.0.0.1'  # Server address (localhost)
    port = 65432        # Port used by the server
    buffer_size = 1024  # Buffer size for receiving data

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = input("Enter message to send: ")
        client_socket.sendto(message.encode(), (host, port))  # Send message to server
        data, server = client_socket.recvfrom(buffer_size)     # Receive response
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    start_udp_client()
