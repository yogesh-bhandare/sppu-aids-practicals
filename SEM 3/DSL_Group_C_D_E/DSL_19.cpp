//Yogesh Bhandare SE AIDS 22506
//Department of Computer Engineering has student's club named 'Pinnacle Club'. Students of
//second, third and final year of department can be granted membership on request.Similarly
//one may cancel the membership of club.First node is reserved for president of club and last
//node is reserved for secretary of club.Write C++ program to maintain club member‘s
//information using singly linked list.Store student PRN and Name.Write functions to :
//a) Add and delete the members as well as president or even secretary.
//b) Compute total number of members of club
//c) Display members
//d) Two linked lists exists for two divisions.Concatenate two lists.

#include<iostream>
#include<string>
using namespace std;

// Node structure to represent a club member
struct Node {
    int prn;
    string name;
    Node* next;
};

// Linked List class for managing club members
class ClubList {
private:
    Node* head; // Head of the linked list

public:
    // Constructor
    ClubList() {
        head = nullptr;
    }

    // Function to add a new member to the club
    void addMember(int prn, const string& name) {
        Node* newNode = new Node;
        newNode->prn = prn;
        newNode->name = name;
        newNode->next = head;
        head = newNode;
        cout << "Member added successfully!" << endl;
    }

    // Function to delete a member from the club
    void deleteMember(int prn) {
        Node* current = head;
        Node* previous = nullptr;

        // Search for the member
        while (current != nullptr && current->prn != prn) {
            previous = current;
            current = current->next;
        }

        // If member found, delete it
        if (current != nullptr) {
            if (previous != nullptr) {
                previous->next = current->next;
            }
            else {
                head = current->next;
            }
            delete current;
            cout << "Member deleted successfully!" << endl;
        }
        else {
            cout << "Member not found!" << endl;
        }
    }

    // Function to compute the total number of members
    int totalMembers() {
        int count = 0;
        Node* current = head;
        while (current != nullptr) {
            count++;
            current = current->next;
        }
        return count;
    }

    // Function to display all members
    void displayMembers() {
        Node* current = head;
        while (current != nullptr) {
            cout << "PRN: " << current->prn << ", Name: " << current->name << endl;
            current = current->next;
        }
    }

    // Function to concatenate two linked lists
    void concatenateLists(ClubList& otherList) {
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = otherList.head;
        cout << "Lists concatenated successfully!" << endl;
    }
};

int main() {
    ClubList division1, division2;
    int choice, prn;
    string name;
    char continueChoice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Add a member to Division 1" << endl;
        cout << "2. Add a member to Division 2" << endl;
        cout << "3. Delete a member" << endl;
        cout << "4. Display members" << endl;
        cout << "5. Concatenate two divisions" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter PRN: ";
            cin >> prn;
            cout << "Enter Name: ";
            cin.ignore();
            getline(cin, name);
            division1.addMember(prn, name);
            break;
        case 2:
            cout << "Enter PRN: ";
            cin >> prn;
            cout << "Enter Name: ";
            cin.ignore();
            getline(cin, name);
            division2.addMember(prn, name);
            break;
        case 3:
            cout << "Enter PRN to delete: ";
            cin >> prn;
            division1.deleteMember(prn);
            division2.deleteMember(prn);
            break;
        case 4:
            cout << "Division 1 Members:" << endl;
            division1.displayMembers();

            cout << "\nDivision 2 Members:" << endl;
            division2.displayMembers();
            break;
        case 5:
            division1.concatenateLists(division2);
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

