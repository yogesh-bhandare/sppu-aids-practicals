import socket

def start_tcp_client():
    host = '127.0.0.1'  # Server address (localhost)
    port = 65432        # Port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input("Enter message to send: ")
        client_socket.sendall(message.encode())  # Send message to server
        data = client_socket.recv(1024)          # Receive response
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    start_tcp_client()
