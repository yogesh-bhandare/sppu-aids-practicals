#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>  
#include <string>      

using namespace std;

#pragma comment(lib, "ws2_32.lib")  

void start_udp_client() {
    const char* host = "127.0.0.1";  
    const int port = 65432;          
    const int buffer_size = 1024;    
    WSADATA wsaData;
    SOCKET clientSocket;
    char buffer[buffer_size] = { 0 };

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        cerr << "WSAStartup failed.\n";
        return;
    }

    // Create socket
    clientSocket = socket(AF_INET, SOCK_DGRAM, 0);  // UDP socket
    if (clientSocket == INVALID_SOCKET) {
        cerr << "Socket creation failed.\n";
        WSACleanup();
        return;
    }

    // Setup the server address
    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(port);

    // Use InetPtonA for compatibility
    if (InetPtonA(AF_INET, host, &serverAddr.sin_addr) <= 0) {
        cerr << "Invalid address/ Address not supported.\n";
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    // Send message to server
    string message;
    cout << "Enter message to send: ";
    getline(cin, message);  
    sendto(clientSocket, message.c_str(), static_cast<int>(message.length()), 0,
        (sockaddr*)&serverAddr, sizeof(serverAddr));

    // Receive response from server
    int serverAddrSize = sizeof(serverAddr);
    int bytesReceived = recvfrom(clientSocket, buffer, buffer_size, 0,
        (sockaddr*)&serverAddr, &serverAddrSize);
    if (bytesReceived > 0) {
        cout << "Received from server: " << string(buffer, bytesReceived) << "\n";
    }

    // Close socket
    closesocket(clientSocket);
    WSACleanup();
}

int main() {
    start_udp_client();
    return 0;
}
