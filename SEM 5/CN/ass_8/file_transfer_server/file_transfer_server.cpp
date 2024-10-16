#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <fstream>
#pragma comment(lib, "ws2_32.lib")  // Link with Winsock library

void start_server() {
    const char* host = "127.0.0.1";  // Localhost
    const int port = 65432;          // Port to listen on
    WSADATA wsaData;
    SOCKET serverSocket, clientSocket;
    sockaddr_in serverAddr, clientAddr;
    int clientAddrSize = sizeof(clientAddr);
    char buffer[1024] = { 0 };

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed.\n";
        return;
    }

    // Create socket
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);  // TCP socket
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

    // Start listening for connections
    if (listen(serverSocket, SOMAXCONN) == SOCKET_ERROR) {
        std::cerr << "Listen failed.\n";
        closesocket(serverSocket);
        WSACleanup();
        return;
    }

    std::cout << "Server listening on " << host << ":" << port << "\n";

    // Accept client connection
    clientSocket = accept(serverSocket, (sockaddr*)&clientAddr, &clientAddrSize);
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "Accept failed.\n";
        closesocket(serverSocket);
        WSACleanup();
        return;
    }

    std::cout << "Client connected.\n";

    // Receive the filename
    int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);
    if (bytesReceived <= 0) {
        std::cerr << "Failed to receive filename.\n";
        closesocket(clientSocket);
        closesocket(serverSocket);
        WSACleanup();
        return;
    }

    std::string filename(buffer, bytesReceived);
    std::cout << "Receiving file: " << filename << "\n";

    // Open file to save received data
    std::ofstream file(filename, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << filename << "\n";
        closesocket(clientSocket);
        closesocket(serverSocket);
        WSACleanup();
        return;
    }

    // Receive the file data and write to the file
    while ((bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0)) > 0) {
        file.write(buffer, bytesReceived);
    }

    std::cout << "File " << filename << " received successfully!\n";

    // Close sockets and cleanup
    closesocket(clientSocket);
    closesocket(serverSocket);
    WSACleanup();
}

int main() {
    start_server();
    return 0;
}
