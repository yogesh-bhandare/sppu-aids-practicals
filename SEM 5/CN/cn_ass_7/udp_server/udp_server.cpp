#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>  // For sockaddr_in
#pragma comment(lib, "ws2_32.lib")  // Link with Winsock library

void start_udp_server() {
    const char* host = "127.0.0.1";  // Localhost
    const int port = 65432;          // Port to listen on
    const int buffer_size = 1024;    // Buffer size for receiving data
    WSADATA wsaData;
    SOCKET serverSocket;
    sockaddr_in serverAddr, clientAddr;
    char buffer[buffer_size] = { 0 };
    int clientAddrSize = sizeof(clientAddr);

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed.\n";
        return;
    }

    // Create socket
    serverSocket = socket(AF_INET, SOCK_DGRAM, 0);  // UDP socket
    if (serverSocket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed.\n";
        WSACleanup();
        return;
    }

    // Setup the server address
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;  // Bind to any available address
    serverAddr.sin_port = htons(port);

    // Bind the socket
    if (bind(serverSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Bind failed.\n";
        closesocket(serverSocket);
        WSACleanup();
        return;
    }

    std::cout << "UDP Server listening on " << host << ":" << port << "\n";

    // Receive data from client
    while (true) {
        int bytesReceived = recvfrom(serverSocket, buffer, buffer_size, 0,
            (sockaddr*)&clientAddr, &clientAddrSize);
        if (bytesReceived > 0) {
            std::cout << "Received from client: " << std::string(buffer, bytesReceived) << "\n";
            sendto(serverSocket, buffer, bytesReceived, 0,
                (sockaddr*)&clientAddr, clientAddrSize);  // Echo back the received data
        }
    }

    // Close socket
    closesocket(serverSocket);
    WSACleanup();
}

int main() {
    start_udp_server();
    return 0;
}
