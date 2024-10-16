#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <sys/types.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

void start_client() {
    const char* host = "127.0.0.1";  // Server address
    int port = 65432;                // Server port
    int buffer_size = 1024;          // Buffer size

    // Initialize Winsock
    WSADATA wsaData;
    WSAStartup(MAKEWORD(2, 2), &wsaData);

    // Create a UDP socket
    SOCKET client_socket = socket(AF_INET, SOCK_DGRAM, 0);
    if (client_socket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed!" << std::endl;
        WSACleanup();
        return;
    }

    sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(port);
    inet_pton(AF_INET, host, &server_address.sin_addr);

    // Get the file path from the user
    std::string filepath;
    std::cout << "Enter the full file path to send (e.g., C:/path/to/file.txt): ";
    std::cin >> filepath;

    // Check if the file exists
    std::ifstream file(filepath, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "File " << filepath << " not found!" << std::endl;
        closesocket(client_socket);
        WSACleanup();
        return;
    }

    // Send the filename (extracting just the filename from the path)
    std::string filename = filepath.substr(filepath.find_last_of("/\\") + 1);
    sendto(client_socket, filename.c_str(), filename.length(), 0, (sockaddr*)&server_address, sizeof(server_address));

    // Send the file data
    char buffer[1024];
    while (file.read(buffer, sizeof(buffer))) {
        sendto(client_socket, buffer, sizeof(buffer), 0, (sockaddr*)&server_address, sizeof(server_address));
    }
    if (file.gcount() > 0) {
        sendto(client_socket, buffer, file.gcount(), 0, (sockaddr*)&server_address, sizeof(server_address));
    }

    std::cout << "File " << filename << " sent successfully!" << std::endl;

    file.close();
    closesocket(client_socket);
    WSACleanup();
}

int main() {
    start_client();
    return 0;
}
