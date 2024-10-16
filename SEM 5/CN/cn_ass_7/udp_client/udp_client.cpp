#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>  // For sockaddr_in and InetPtonA
#include <string>      // For std::string and std::getline
#pragma comment(lib, "ws2_32.lib")  // Link with Winsock library

void start_udp_client() {
    const char* host = "127.0.0.1";  // Server address (localhost)
    const int port = 65432;          // Port used by the server
    const int buffer_size = 1024;    // Buffer size for receiving data
    WSADATA wsaData;
    SOCKET clientSocket;
    char buffer[buffer_size] = { 0 };

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed.\n";
        return;
    }

    // Create socket
    clientSocket = socket(AF_INET, SOCK_DGRAM, 0);  // UDP socket
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed.\n";
        WSACleanup();
        return;
    }

    // Setup the server address
    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(port);

    // Use InetPtonA for compatibility
    if (InetPtonA(AF_INET, host, &serverAddr.sin_addr) <= 0) {
        std::cerr << "Invalid address/ Address not supported.\n";
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    // Send message to server
    std::string message;
    std::cout << "Enter message to send: ";
    std::getline(std::cin, message);  // Use std::getline to read input
    sendto(clientSocket, message.c_str(), static_cast<int>(message.length()), 0,
        (sockaddr*)&serverAddr, sizeof(serverAddr));

    // Receive response from server
    int serverAddrSize = sizeof(serverAddr);
    int bytesReceived = recvfrom(clientSocket, buffer, buffer_size, 0,
        (sockaddr*)&serverAddr, &serverAddrSize);
    if (bytesReceived > 0) {
        std::cout << "Received from server: " << std::string(buffer, bytesReceived) << "\n";
    }

    // Close socket
    closesocket(clientSocket);
    WSACleanup();
}

int main() {
    start_udp_client();
    return 0;
}
