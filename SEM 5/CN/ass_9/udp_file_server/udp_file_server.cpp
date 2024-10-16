#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <sys/types.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "Ws2_32.lib")

#define BUFFER_SIZE 1024

void start_server() {
    const char* host = "127.0.0.1";  // Localhost
    int port = 65432;                // Port to listen on

    // Initialize Winsock
    WSADATA wsaData;
    int result = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (result != 0) {
        std::cerr << "WSAStartup failed with error: " << result << std::endl;
        return;
    }

    // Create a UDP socket
    SOCKET server_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (server_socket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed with error: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return;
    }

    // Set up the server address
    sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Bind the socket to the address
    result = bind(server_socket, (sockaddr*)&server_addr, sizeof(server_addr));
    if (result == SOCKET_ERROR) {
        std::cerr << "Bind failed with error: " << WSAGetLastError() << std::endl;
        closesocket(server_socket);
        WSACleanup();
        return;
    }

    std::cout << "Server listening on " << host << ":" << port << std::endl;

    char buffer[BUFFER_SIZE];
    sockaddr_in client_addr;
    int client_addr_size = sizeof(client_addr);

    while (true) {
        std::cout << "Waiting for file transfer..." << std::endl;

        // Receive the filename
        int bytes_received = recvfrom(server_socket, buffer, BUFFER_SIZE, 0, (sockaddr*)&client_addr, &client_addr_size);
        if (bytes_received == SOCKET_ERROR) {
            std::cerr << "recvfrom failed with error: " << WSAGetLastError() << std::endl;
            break;
        }

        std::string filename(buffer, bytes_received);
        std::cout << "Receiving file: " << filename << " from client" << std::endl;

        std::ofstream file(filename, std::ios::binary);
        if (!file.is_open()) {
            std::cerr << "Error opening file: " << filename << std::endl;
            break;
        }

        // Receive the file data
        while (true) {
            bytes_received = recvfrom(server_socket, buffer, BUFFER_SIZE, 0, (sockaddr*)&client_addr, &client_addr_size);
            if (bytes_received == SOCKET_ERROR) {
                std::cerr << "recvfrom failed with error: " << WSAGetLastError() << std::endl;
                break;
            }
            if (bytes_received == 0) {
                break;
            }
            file.write(buffer, bytes_received);
        }

        std::cout << "File " << filename << " received successfully!" << std::endl;
        file.close();
    }

    // Clean up
    closesocket(server_socket);
    WSACleanup();
}

int main() {
    start_server();
    return 0;
}
