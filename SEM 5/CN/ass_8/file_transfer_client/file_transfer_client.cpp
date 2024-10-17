#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <fstream>
#pragma comment(lib, "ws2_32.lib")  

void start_client() {
    const char* host = "127.0.0.1";  
    const int port = 65432;          
    const char* filename = "file_to_send1.txt";  
    WSADATA wsaData;
    SOCKET clientSocket;

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed.\n";
        return;
    }

    // Create socket
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);  // TCP socket
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed.\n";
        WSACleanup();
        return;
    }

    // Setup the server address
    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(port);

    if (InetPtonA(AF_INET, host, &serverAddr.sin_addr) <= 0) {
        std::cerr << "Invalid address/ Address not supported.\n";
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    // Connect to the server
    if (connect(clientSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Connection failed.\n";
        closesocket(clientSocket);
        WSACleanup();
        return;
    }

    // Send the filename
    send(clientSocket, filename, static_cast<int>(strlen(filename)), 0);

    // Open the file and send its contents
    std::ifstream file(filename, std::ios::binary);
    if (file.is_open()) {
        char buffer[1024];
        while (file.read(buffer, sizeof(buffer)) || file.gcount() > 0) {
            send(clientSocket, buffer, static_cast<int>(file.gcount()), 0);
        }
        std::cout << "File " << filename << " sent successfully!\n";
    }
    else {
        std::cerr << "Unable to open file: " << filename << "\n";
    }

    // Close the socket and cleanup
    closesocket(clientSocket);
    WSACleanup();
}

int main() {
    start_client();
    return 0;
}
