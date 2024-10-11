import socket
import os

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on
    buffer_size = 1024  # Buffer size for receiving data

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server listening on {host}:{port}")

        while True:
            print("Waiting for file transfer...")
            filename, addr = server_socket.recvfrom(buffer_size)
            filename = filename.decode()
            print(f"Receiving file: {filename} from {addr}")

            with open(filename, 'wb') as file:
                while True:
                    data, addr = server_socket.recvfrom(buffer_size)
                    if not data:
                        break
                    file.write(data)

            print(f"File {filename} received successfully!")
            print("Waiting for next file...")

if __name__ == "__main__":
    start_server()
