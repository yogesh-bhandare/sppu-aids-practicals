#include <iostream>
#include <winsock2.h>
#include <ws2tcpip.h> 

using namespace std;

#pragma comment(lib, "ws2_32.lib") // Winsock library

void dnsLookupByDomain(const std::string& domain) {
    struct addrinfo hints, * res;
    char ipstr[INET6_ADDRSTRLEN]; 

    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC; 
    hints.ai_socktype = SOCK_STREAM; 

    int status = getaddrinfo(domain.c_str(), nullptr, &hints, &res);
    if (status != 0) {
        cerr << "Error: Unable to resolve domain. " << gai_strerror(status) << endl;
        return;
    }

    for (struct addrinfo* p = res; p != nullptr; p = p->ai_next) {
        void* addr;
        string ipver;

        if (p->ai_family == AF_INET) { 
            struct sockaddr_in* ipv4 = (struct sockaddr_in*)p->ai_addr;
            addr = &(ipv4->sin_addr);
            ipver = "IPv4";
        }
        else { 
            struct sockaddr_in6* ipv6 = (struct sockaddr_in6*)p->ai_addr;
            addr = &(ipv6->sin6_addr);
            ipver = "IPv6";
        }

        inet_ntop(p->ai_family, addr, ipstr, sizeof(ipstr));
        cout << "Resolved " << ipver << " address: " << ipstr << endl;
    }

    freeaddrinfo(res); 
}

void dnsLookupByIP(const string& ip) {
    struct sockaddr_in sa; 
    char host[NI_MAXHOST];

    inet_pton(AF_INET, ip.c_str(), &(sa.sin_addr));
    sa.sin_family = AF_INET;

    int status = getnameinfo((struct sockaddr*)&sa, sizeof(sa), host, NI_MAXHOST, nullptr, 0, 0);
    if (status != 0) {
        cerr << "Error: Unable to resolve IP address. " << gai_strerror(status) << endl;
        return;
    }

    cout << "Resolved domain: " << host << endl;
}

int main() {
    // Initialize Winsock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        cerr << "Failed to initialize Winsock." << endl;
        return 1;
    }

    string input;
    int choice;
    char continueChoice; 

    do {
        cout << "Enter 1 for domain to IP lookup or 2 for IP to domain lookup: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter domain name (e.g., www.google.com): ";
            cin >> input;
            dnsLookupByDomain(input);
        }
        else if (choice == 2) {
            cout << "Enter IP address (e.g., 8.8.8.8): ";
            cin >> input;
            dnsLookupByIP(input);
        }
        else {
            cout << "Invalid choice." << endl;
        }

        cout << "\nDo you want to perform another lookup? (y/n): ";
        cin >> continueChoice;

    } while (continueChoice == 'y' || continueChoice == 'Y');  

    // Cleanup Winsock
    WSACleanup();

    cout << "Exiting the program." << endl;
    return 0;
}
