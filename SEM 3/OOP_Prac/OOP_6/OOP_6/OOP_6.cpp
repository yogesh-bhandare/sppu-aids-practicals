//Yogesh Bhandare 22506 SE AIDS
//Write C++ program using STL for sorting and searching user defined records such as personal
//records(Name, DOB, Telephone number etc) using vector container

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

// Define a structure for the personal record
struct PersonalRecord {
    string name;
    string dob; // Date of Birth
    string phoneNumber;

    // Constructor to initialize the personal record
    PersonalRecord(const string& n, const string& d, const string& phone)
        : name(n), dob(d), phoneNumber(phone) {}

    // Function to display the personal record
    void display() const {
        cout << "Name: " << name << ", DOB: " << dob << ", Phone Number: " << phoneNumber << endl;
    }
};

// Function to display a vector of personal records
void displayRecords(const vector<PersonalRecord>& records) {
    for (const auto& record : records) {
        record.display();
    }
    cout << endl;
}

int main() {
    vector<PersonalRecord> personalRecords;

    char continueChoice;
    do {
        cout << "\nMenu:" << endl;
        cout << "1. Add Personal Record" << endl;
        cout << "2. Display Personal Records" << endl;
        cout << "3. Sort Personal Records by Name" << endl;
        cout << "4. Search for a Personal Record by Name" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";

        int choice;
        cin >> choice;

        switch (choice) {
        case 1: {
            string name, dob, phoneNumber;
            cin.ignore(); // Clear the input buffer
            cout << "Enter Name: ";
            getline(cin, name);
            cout << "Enter DOB: ";
            getline(cin, dob);
            cout << "Enter Phone Number: ";
            getline(cin, phoneNumber);
            personalRecords.push_back(PersonalRecord(name, dob, phoneNumber));
            cout << "Personal Record added successfully." << endl;
            break;
        }
        case 2:
            cout << "\nPersonal Records:" << endl;
            displayRecords(personalRecords);
            break;
        case 3:
            sort(personalRecords.begin(), personalRecords.end(),
                [](const PersonalRecord& a, const PersonalRecord& b) {
                    return a.name < b.name;
                });
            cout << "Personal Records sorted by Name." << endl;
            break;
        case 4: {
            string searchName;
            cin.ignore(); // Clear the input buffer
            cout << "Enter the Name to search: ";
            getline(cin, searchName);
            auto it = find_if(personalRecords.begin(), personalRecords.end(),
                [&searchName](const PersonalRecord& record) {
                    return record.name == searchName;
                });

            if (it != personalRecords.end()) {
                cout << "Personal Record found:" << endl;
                it->display();
            }
            else {
                cout << "Personal Record not found." << endl;
            }
            break;
        }
        case 5:
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
