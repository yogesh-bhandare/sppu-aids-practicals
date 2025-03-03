//Yogesh Bhandare SE AIDS 22506
//Write a C++ program that creates an output file, writes information to it, closes the file, open it
//again as an input file and read the information from the file.

#include<iostream>
#include<fstream>
#include<string>
using namespace std;

// Function to create an output file and write information to it
void writeToFile(const string& filename) {
    ofstream outputFile(filename);

    if (outputFile.is_open()) {
        cout << "Enter information to write to the file (type 'exit' to stop):" << endl;

        string input;
        while (true) {
            getline(cin, input);

            if (input == "exit") {
                break;
            }

            outputFile << input << endl;
        }

        cout << "Information written to the file." << endl;
        outputFile.close();
    }
    else {
        cerr << "Error: Unable to open the file for writing." << endl;
    }
}

// Function to open the file as an input file and read information from it
void readFromFile(const string& filename) {
    ifstream inputFile(filename);

    if (inputFile.is_open()) {
        cout << "Reading information from the file:" << endl;

        string line;
        while (getline(inputFile, line)) {
            cout << line << endl;
        }

        inputFile.close();
    }
    else {
        cerr << "Error: Unable to open the file for reading." << endl;
    }
}

int main() {
    string filename;
    char continueChoice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Write to File" << endl;
        cout << "2. Read from File" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";

        int choice;
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter the filename to write: ";
            cin >> filename;
            writeToFile(filename);
            break;
        case 2:
            cout << "Enter the filename to read: ";
            cin >> filename;
            readFromFile(filename);
            break;
        case 3:
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
