import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            filename = conn.recv(1024).decode()  # Receive filename
            print(f"Receiving file: {filename}")
            with open(filename, 'wb') as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
            print(f"File {filename} received successfully!")

if __name__ == "__main__":
    start_server()
