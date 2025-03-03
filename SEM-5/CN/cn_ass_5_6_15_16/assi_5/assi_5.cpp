#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

// Function to convert IP address from string format to vector of integers
vector<int> parseIPAddress(const string& ipAddress) {
    vector<int> result;
    stringstream ss(ipAddress);
    string segment;
    while (getline(ss, segment, '.')) {
        result.push_back(stoi(segment));
    }
    return result;
}

// Function to convert vector of integers to string format for IP address
string formatIPAddress(const vector<int>& ip) {
    stringstream ss;
    for (int i = 0; i < ip.size(); i++) {
        ss << ip[i];
        if (i != ip.size() - 1) ss << ".";
    }
    return ss.str();
}

// Function to calculate the subnet mask based on prefix length
vector<int> calculateSubnetMask(int prefixLength) {
    vector<int> subnetMask(4, 0);
    for (int i = 0; i < 4; i++) {
        if (prefixLength >= 8) {
            subnetMask[i] = 255;
            prefixLength -= 8;
        }
        else if (prefixLength > 0) {
            subnetMask[i] = 256 - pow(2, 8 - prefixLength);
            break;
        }
    }
    return subnetMask;
}

// Function to calculate the network address
vector<int> calculateNetworkAddress(const vector<int>& ipAddress, const vector<int>& subnetMask) {
    vector<int> networkAddress(4, 0);
    for (int i = 0; i < 4; i++) {
        networkAddress[i] = ipAddress[i] & subnetMask[i];
    }
    return networkAddress;
}

// Function to calculate the number of subnets and their addresses
void subnetCalculator(const string& network, int newPrefix) {
    try {
        // Parse the network and extract the prefix length
        stringstream ss(network);
        string ipPart, prefixPart;
        getline(ss, ipPart, '/');
        getline(ss, prefixPart);

        int originalPrefix = stoi(prefixPart);
        vector<int> ipAddress = parseIPAddress(ipPart);

        // Display original network information
        vector<int> originalSubnetMask = calculateSubnetMask(originalPrefix);
        cout << "\nOriginal Network: " << network << endl;
        cout << "Subnet Mask: " << formatIPAddress(originalSubnetMask) << endl;
        int totalAddresses = pow(2, 32 - originalPrefix);
        cout << "Total IP addresses: " << totalAddresses << endl;

        // Calculate new subnets based on the new prefix
        int subnetsCount = pow(2, newPrefix - originalPrefix);
        int addressesPerSubnet = pow(2, 32 - newPrefix);
        cout << "\nDividing network into subnets with /" << newPrefix << " prefix..." << endl;
        cout << "Number of subnets: " << subnetsCount << endl;

        for (int i = 0; i < subnetsCount; i++) {
            vector<int> subnetAddress = ipAddress;

            // Calculate subnet address by adding the offset to the network address
            int offset = i * addressesPerSubnet;
            for (int j = 3; j >= 0 && offset > 0; j--) {
                subnetAddress[j] += offset % 256;
                offset /= 256;
            }

            vector<int> newSubnetMask = calculateSubnetMask(newPrefix);
            vector<int> networkAddress = calculateNetworkAddress(subnetAddress, newSubnetMask);

            cout << "\nSubnet " << (i + 1) << ":" << endl;
            cout << "  Network Address: " << formatIPAddress(networkAddress) << endl;
            cout << "  Subnet Mask: " << formatIPAddress(newSubnetMask) << endl;

            vector<int> firstIP = networkAddress;
            firstIP[3] += 1;  // First usable IP is the next IP after network address
            vector<int> lastIP = networkAddress;
            lastIP[3] += (addressesPerSubnet - 2);  // Last usable IP is the second to last IP

            cout << "  First Usable IP: " << formatIPAddress(firstIP) << endl;
            cout << "  Last Usable IP: " << formatIPAddress(lastIP) << endl;
            cout << "  Total Usable IPs: " << (addressesPerSubnet - 2) << endl;
        }

    }
    catch (const exception& e) {
        cout << "Error: Invalid input or calculation." << endl;
    }
}

int main() {
    string network;
    int newPrefix;
    char choice;  

    do {
        cout << "Enter the network address (e.g., 192.168.1.0/24): ";
        cin >> network;

        cout << "Enter the new prefix length (e.g., 26): ";
        cin >> newPrefix;

        subnetCalculator(network, newPrefix);

        cout << "\nDo you want to calculate another subnet? (y/n): ";
        cin >> choice;

    } while (choice == 'y' || choice == 'Y');  

    cout << "Exiting the program." << endl;
    return 0;
}
