import socket

def start_client():
    host = '127.0.0.1'  # Server address (localhost)
    port = 65432        # Port used by the server

    filename = 'file_to_send.txt'  # Replace with the file you want to send

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(filename.encode())  # Send filename
        with open(filename, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)
        print(f"File {filename} sent successfully!")

if __name__ == "__main__":
    start_client()
