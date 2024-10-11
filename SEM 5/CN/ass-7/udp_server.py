import socket

def start_udp_server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on
    buffer_size = 1024  # Buffer size for receiving data

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP Server listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(buffer_size)
            print(f"Received from {addr}: {data.decode()}")
            server_socket.sendto(data, addr)  # Echo back the received data

if __name__ == "__main__":
    start_udp_server()
