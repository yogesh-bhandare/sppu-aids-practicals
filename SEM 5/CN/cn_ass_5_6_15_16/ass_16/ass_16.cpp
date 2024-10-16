#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h> // For modern functions like getaddrinfo and inet_ntop

#pragma comment(lib, "ws2_32.lib") // Winsock library

void dnsLookupByDomain(const std::string& domain) {
    struct addrinfo hints, * res;
    char ipstr[INET6_ADDRSTRLEN]; // For both IPv4 and IPv6

    // Initialize the hints structure
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC; // AF_INET for IPv4 only, AF_UNSPEC for both IPv4/IPv6
    hints.ai_socktype = SOCK_STREAM; // Use SOCK_DGRAM for UDP connections

    // Perform DNS lookup using getaddrinfo
    int status = getaddrinfo(domain.c_str(), nullptr, &hints, &res);
    if (status != 0) {
        std::cerr << "Error: Unable to resolve domain. " << gai_strerror(status) << std::endl;
        return;
    }

    // Loop through all the results and convert the IP to a readable string
    for (struct addrinfo* p = res; p != nullptr; p = p->ai_next) {
        void* addr;
        std::string ipver;

        // Get the pointer to the address itself (different fields for IPv4 vs IPv6)
        if (p->ai_family == AF_INET) { // IPv4
            struct sockaddr_in* ipv4 = (struct sockaddr_in*)p->ai_addr;
            addr = &(ipv4->sin_addr);
            ipver = "IPv4";
        }
        else { // IPv6
            struct sockaddr_in6* ipv6 = (struct sockaddr_in6*)p->ai_addr;
            addr = &(ipv6->sin6_addr);
            ipver = "IPv6";
        }

        // Convert the IP to a string and print it
        inet_ntop(p->ai_family, addr, ipstr, sizeof(ipstr));
        std::cout << "Resolved " << ipver << " address: " << ipstr << std::endl;
    }

    freeaddrinfo(res); // Free the linked list
}

void dnsLookupByIP(const std::string& ip) {
    struct sockaddr_in sa; // For IPv4 only in this case
    char host[NI_MAXHOST];

    // Initialize the sockaddr_in structure
    inet_pton(AF_INET, ip.c_str(), &(sa.sin_addr));
    sa.sin_family = AF_INET;

    // Perform reverse DNS lookup using getnameinfo
    int status = getnameinfo((struct sockaddr*)&sa, sizeof(sa), host, NI_MAXHOST, nullptr, 0, 0);
    if (status != 0) {
        std::cerr << "Error: Unable to resolve IP address. " << gai_strerror(status) << std::endl;
        return;
    }

    // Print the resolved domain name
    std::cout << "Resolved domain: " << host << std::endl;
}

int main() {
    // Initialize Winsock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "Failed to initialize Winsock." << std::endl;
        return 1;
    }

    std::string input;
    int choice;
    char continueChoice;  // Variable to store user's choice for continuing the program

    do {
        std::cout << "Enter 1 for domain to IP lookup or 2 for IP to domain lookup: ";
        std::cin >> choice;

        if (choice == 1) {
            std::cout << "Enter domain name (e.g., www.google.com): ";
            std::cin >> input;
            dnsLookupByDomain(input);
        }
        else if (choice == 2) {
            std::cout << "Enter IP address (e.g., 8.8.8.8): ";
            std::cin >> input;
            dnsLookupByIP(input);
        }
        else {
            std::cout << "Invalid choice." << std::endl;
        }

        std::cout << "\nDo you want to perform another lookup? (y/n): ";
        std::cin >> continueChoice;

    } while (continueChoice == 'y' || continueChoice == 'Y');  // Continue if user inputs 'y' or 'Y'

    // Cleanup Winsock
    WSACleanup();

    std::cout << "Exiting the program." << std::endl;
    return 0;
}
