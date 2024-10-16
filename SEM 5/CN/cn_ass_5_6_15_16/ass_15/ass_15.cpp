#include <winsock2.h>
#include <ws2tcpip.h>  // For inet_pton
#include <iostream>

#pragma comment(lib, "ws2_32.lib") // Winsock library

#define DHCP_SERVER_PORT 67  // Standard DHCP server port
#define DHCP_CLIENT_PORT 68  // Standard DHCP client port
#define BUFFER_SIZE 1024     // Buffer size for DHCP communication

void simulateDHCPClient() {
    WSADATA wsaData;
    SOCKET clientSocket;
    struct sockaddr_in serverAddr, clientAddr;
    char buffer[BUFFER_SIZE];

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "Winsock initialization failed!" << std::endl;
        return;
    }

    // Create a socket for the DHCP client
    clientSocket = socket(AF_INET, SOCK_DGRAM, 0); // UDP socket for DHCP
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed!" << std::endl;
        WSACleanup();
        return;
    }

    // Set up the client address structure
    clientAddr.sin_family = AF_INET;
    clientAddr.sin_port = htons(DHCP_CLIENT_PORT); // Client port 68
    clientAddr.sin_addr.s_addr = INADDR_ANY;       // Use any local address

    // Bind the client socket
    if (bind(clientSocket, (struct sockaddr*)&clientAddr, sizeof(clientAddr)) == SOCKET_ERROR) {
        std::cerr << "Bind failed!" << std::endl;
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    // Set up the server address structure (DHCP server)
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(DHCP_SERVER_PORT); // Server port 67

    // Using inet_pton to convert the IP address
    if (inet_pton(AF_INET, "192.168.1.1", &serverAddr.sin_addr) <= 0) {
        std::cerr << "Invalid address or address not supported." << std::endl;
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    // Simulate sending a DHCP DISCOVER packet
    std::string dhcpDiscover = "DHCP DISCOVER: Client requests IP";
    if (sendto(clientSocket, dhcpDiscover.c_str(), static_cast<int>(dhcpDiscover.size()), 0,
        (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Failed to send DHCP DISCOVER!" << std::endl;
        closesocket(clientSocket);
        WSACleanup();
        return;
    }
    std::cout << "Sent DHCP DISCOVER packet to the DHCP server." << std::endl;

    // Simulate receiving a DHCP OFFER packet from the server
    int serverAddrSize = sizeof(serverAddr);
    if (recvfrom(clientSocket, buffer, BUFFER_SIZE, 0,
        (struct sockaddr*)&serverAddr, &serverAddrSize) == SOCKET_ERROR) {
        std::cerr << "Failed to receive DHCP OFFER!" << std::endl;
        closesocket(clientSocket);
        WSACleanup();
        return;
    }
    std::cout << "Received DHCP OFFER: " << buffer << std::endl;

    // Simulate sending a DHCP REQUEST packet
    std::string dhcpRequest = "DHCP REQUEST: Client requests offered IP";
    if (sendto(clientSocket, dhcpRequest.c_str(), static_cast<int>(dhcpRequest.size()), 0,
        (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Failed to send DHCP REQUEST!" << std::endl;
        closesocket(clientSocket);
        WSACleanup();
        return;
    }
    std::cout << "Sent DHCP REQUEST packet to the server." << std::endl;

    // Simulate receiving a DHCP ACK packet from the server
    if (recvfrom(clientSocket, buffer, BUFFER_SIZE, 0,
        (struct sockaddr*)&serverAddr, &serverAddrSize) == SOCKET_ERROR) {
        std::cerr << "Failed to receive DHCP ACK!" << std::endl;
        closesocket(clientSocket);
        WSACleanup();
        return;
    }
    std::cout << "Received DHCP ACK: " << buffer << std::endl;

    // Close the socket and cleanup
    closesocket(clientSocket);
    WSACleanup();
}

int main() {
    simulateDHCPClient();
    return 0;
}
