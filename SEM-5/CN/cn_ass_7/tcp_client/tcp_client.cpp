#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>  
#include <string>      

using namespace std;

#pragma comment(lib, "ws2_32.lib")  

void start_tcp_client() {
    const char* host = "127.0.0.1";  
    const int port = 65432;          
    WSADATA wsaData;
    SOCKET clientSocket;
    char buffer[1024] = { 0 };

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        cerr << "WSAStartup failed.\n";
        return;
    }

    // Create socket
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);
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

    // Connect to the server
    if (connect(clientSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        cerr << "Connection failed.\n";
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    cout << "Connected to server.\n";

    // Send message to server
    string message;
    cout << "Enter message to send: ";
    getline(std::cin, message);  // Use std::getline to read input
    send(clientSocket, message.c_str(), static_cast<int>(message.length()), 0);  // Send message

    // Receive response from server
    int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);
    if (bytesReceived > 0) {
        cout << "Received from server: " << string(buffer, bytesReceived) << "\n";
    }

    // Close socket
    closesocket(clientSocket);
    WSACleanup();
}

int main() {
    start_tcp_client();
    return 0;
}
