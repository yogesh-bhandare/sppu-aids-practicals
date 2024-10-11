//Yogesh Bhandare SE AIDS 22506
//Imagine a publishing company which does marketing for book and audio cassette versions.
//Create a class publication that stores the title(a string) and price(type float) of publications.
//From this class derive two classes : book which adds a page count(type int) and tape which adds
//a playing time in minutes(type float).
//Write a program that instantiates the book and tape class, allows user to enter data and displays
//the data members.If an exception is caught, replace all the data member values with zero
//values.

#include<iostream>
#include<string>
using namespace std;

class Publication {
protected:
    string title;
    float price;

public:
    // Constructor with default values
    Publication() : title(""), price(0.0) {}

    // Function to input data for a publication
    virtual void getData() {
        cout << "Enter title: ";
        cin.ignore(); // Clear the input buffer
        getline(cin, title);
        cout << "Enter price: $";
        cin >> price;
    }

    // Function to display data for a publication
    virtual void displayData() const {
        cout << "Title: " << title << endl;
        cout << "Price: $" << price << endl;
    }
};

class Book : public Publication {
private:
    int pageCount;

public:
    // Constructor with default values
    Book() : pageCount(0) {}

    // Function to input data for a book
    void getData() override {
        Publication::getData(); // Call base class function
        cout << "Enter page count: ";
        cin >> pageCount;
    }

    // Function to display data for a book
    void displayData() const override {
        Publication::displayData(); // Call base class function
        cout << "Page Count: " << pageCount << " pages" << endl;
    }
};

class Tape : public Publication {
private:
    float playingTime;

public:
    // Constructor with default values
    Tape() : playingTime(0.0) {}

    // Function to input data for a tape
    void getData() override {
        Publication::getData(); // Call base class function
        cout << "Enter playing time (in minutes): ";
        cin >> playingTime;
    }

    // Function to display data for a tape
    void displayData() const override {
        Publication::displayData(); // Call base class function
        cout << "Playing Time: " << playingTime << " minutes" << endl;
    }
};

int main() {
    char continueChoice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Enter Book Data" << endl;
        cout << "2. Enter Tape Data" << endl;
        cout << "3. Display Book Data" << endl;
        cout << "4. Display Tape Data" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";

        int choice;
        cin >> choice;

        switch (choice) {
        case 1: {
            Book book;
            book.getData();
            cout << "\nBook Data Entered:" << endl;
            book.displayData();
            break;
        }
        case 2: {
            Tape tape;
            tape.getData();
            cout << "\nTape Data Entered:" << endl;
            tape.displayData();
            break;
        }
        case 3:
            // Display book data
            break;
        case 4:
            // Display tape data
            break;
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
