import socket
import os

def start_client():
    host = '127.0.0.1'  # Server address (localhost)
    port = 65432        # Port used by the server
    buffer_size = 1024  # Buffer size for sending data

    filename = input("Enter the file name to send (script.txt, audio.mp3, video.mp4): ")

    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"File {filename} not found!")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(filename.encode(), (host, port))  # Send filename

        with open(filename, 'rb') as file:
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                client_socket.sendto(data, (host, port))

        print(f"File {filename} sent successfully!")

if __name__ == "__main__":
    start_client()
