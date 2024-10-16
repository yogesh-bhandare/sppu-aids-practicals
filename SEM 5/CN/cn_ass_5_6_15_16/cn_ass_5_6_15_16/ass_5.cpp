//#include <iostream>
//#include <vector>
//#include <bitset>
//#include <cmath>
//
//using namespace std;
//
//// Function to convert a decimal number to binary
//string decimalToBinary(int n) {
//    return bitset<8>(n).to_string();  // Converts the decimal number to 8-bit binary
//}
//
//// Function to find the subnet mask for a given number of subnets
//void findSubnetMask(int subnetBits) {
//    int subnetMask[4] = { 0, 0, 0, 0 }; // Initializing the subnet mask to 0
//
//    // Set the bits in the subnet mask
//    for (int i = 0; i < 4; i++) {
//        if (subnetBits >= 8) {
//            subnetMask[i] = 255;  // If 8 or more bits, set the octet to 255
//            subnetBits -= 8;
//        }
//        else {
//            subnetMask[i] = (256 - pow(2, 8 - subnetBits)); // Calculate the remaining bits in the last octet
//            subnetBits = 0;
//        }
//    }
//
//    // Print the subnet mask
//    cout << "Subnet Mask: ";
//    for (int i = 0; i < 4; i++) {
//        cout << subnetMask[i];
//        if (i != 3) cout << ".";
//    }
//    cout << endl;
//}
//
//// Function to calculate the network address
//void calculateNetworkAddress(vector<int> ipAddress, vector<int> subnetMask) {
//    vector<int> networkAddress(4, 0);
//
//    for (int i = 0; i < 4; i++) {
//        networkAddress[i] = ipAddress[i] & subnetMask[i];  // Perform bitwise AND to find network address
//    }
//
//    // Print the network address
//    cout << "Network Address: ";
//    for (int i = 0; i < 4; i++) {
//        cout << networkAddress[i];
//        if (i != 3) cout << ".";
//    }
//    cout << endl;
//}
//
//// Function to demonstrate subnetting
//void subnetting(vector<int> ipAddress, int subnetBits) {
//    cout << "IP Address: ";
//    for (int i = 0; i < 4; i++) {
//        cout << ipAddress[i];
//        if (i != 3) cout << ".";
//    }
//    cout << endl;
//
//    // Calculate and print subnet mask
//    findSubnetMask(subnetBits);
//
//    // Calculate and print network address
//    vector<int> subnetMask = { 255, 255, 255, 0 }; // Example: /24 Subnet Mask
//    calculateNetworkAddress(ipAddress, subnetMask);
//}
//
//int main() {
//    vector<int> ipAddress = { 192, 168, 1, 10 }; // Example IP Address
//    int subnetBits = 24;  // Example subnet bits (e.g., /24)
//
//    subnetting(ipAddress, subnetBits);
//
//    return 0;
//}
