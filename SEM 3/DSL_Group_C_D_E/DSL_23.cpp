//Yogesh Bhandare SE AIDS 22506
//Write C++ program for storing binary number using doubly linked lists.Write functions -
//a) To compute 1‘s and 2‘s complement
//b) Add two binary numbers

#include<iostream>
using namespace std;

// Node structure for a doubly linked list
struct Node {
    int data;
    Node* next;
    Node* prev;
};

// Doubly linked list class for managing binary numbers
class BinaryList {
private:
    Node* head; // Head of the linked list

public:
    // Constructor
    BinaryList() {
        head = nullptr;
    }

    // Function to add a binary digit to the front of the list
    void addDigit(int digit) {
        Node* newNode = new Node;
        newNode->data = digit;
        newNode->next = head;
        newNode->prev = nullptr;

        if (head != nullptr) {
            head->prev = newNode;
        }

        head = newNode;
    }

    // Function to display the binary number
    void displayNumber() {
        Node* current = head;
        while (current != nullptr) {
            cout << current->data;
            current = current->next;
        }
        cout << endl;
    }

    // Function to compute 1's complement
    void onesComplement() {
        Node* current = head;
        while (current != nullptr) {
            current->data = 1 - current->data;
            current = current->next;
        }
    }

    // Function to compute 2's complement
    void twosComplement() {
        onesComplement();

        // Add 1 to the 1's complement
        int carry = 1;
        Node* current = head;

        while (current != nullptr) {
            int sum = current->data + carry;
            current->data = sum % 2;
            carry = sum / 2;
            current = current->next;
        }

        // If there's a carry left, add a new node
        if (carry) {
            addDigit(carry);
        }
    }

    // Function to add two binary numbers
    void add(BinaryList& otherList) {
        int carry = 0;
        Node* current1 = head;
        Node* current2 = otherList.head;
        BinaryList result;

        while (current1 != nullptr || current2 != nullptr) {
            int sum = carry + (current1 ? current1->data : 0) + (current2 ? current2->data : 0);
            carry = sum / 2;
            result.addDigit(sum % 2);

            if (current1) {
                current1 = current1->next;
            }
            if (current2) {
                current2 = current2->next;
            }
        }

        // If there's a carry left, add a new node
        if (carry) {
            result.addDigit(carry);
        }

        // Copy the result back to the original list
        head = result.head;
    }
};

int main() {
    BinaryList binaryNumber1, binaryNumber2, result;
    int choice;
    char continueChoice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Enter binary number 1" << endl;
        cout << "2. Enter binary number 2" << endl;
        cout << "3. Compute 1's complement of a number" << endl;
        cout << "4. Compute 2's complement of a number" << endl;
        cout << "5. Add two binary numbers" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter binary number 1: ";
            // Assuming that the input consists of 0s and 1s only
            while (true) {
                char digit;
                cin >> digit;
                if (digit == '0' || digit == '1') {
                    binaryNumber1.addDigit(digit - '0');
                }
                else {
                    break;
                }
            }
            break;
        case 2:
            cout << "Enter binary number 2: ";
            // Assuming that the input consists of 0s and 1s only
            while (true) {
                char digit;
                cin >> digit;
                if (digit == '0' || digit == '1') {
                    binaryNumber2.addDigit(digit - '0');
                }
                else {
                    break;
                }
            }
            break;
        case 3:
            cout << "Enter the binary number to compute 1's complement: ";
            binaryNumber1.displayNumber();
            binaryNumber1.onesComplement();
            cout << "1's complement: ";
            binaryNumber1.displayNumber();
            break;
        case 4:
            cout << "Enter the binary number to compute 2's complement: ";
            binaryNumber1.displayNumber();
            binaryNumber1.twosComplement();
            cout << "2's complement: ";
            binaryNumber1.displayNumber();
            break;
        case 5:
            binaryNumber1.displayNumber();
            binaryNumber2.displayNumber();
            result = binaryNumber1; // Copy binaryNumber1 to result before adding binaryNumber2
            result.add(binaryNumber2);
            cout << "Sum: ";
            result.displayNumber();
            break;
        case 6:
            cout << "Exiting the program." << endl;
            break;
        default:
            cout << "Invalid choice. Please enter a valid option." << endl;
        }

        cout << "Do you want to continue? (y/n): ";
        cin >> continueChoice;
    } while (continueChoice == 'y' || continueChoice == 'Y');

    return 0;
}
