import socket

def start_client():
    host = '127.0.0.1'  # Server address (localhost)
    port = 65432        # Port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
        client_socket.sendall(b"Hello from the client!")

if __name__ == "__main__":
    start_client()
