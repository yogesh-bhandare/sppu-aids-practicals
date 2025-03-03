#include<iostream>
using namespace std;

// Function template for selection sort
template<typename T>
void selectionSort(T arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < size; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
}

// Function template to display array elements
template<typename T>
void displayArray(const T arr[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    const int maxSize = 5; // Set a maximum size for the arrays
    int intArray[maxSize];
    float floatArray[maxSize];
    char continueChoice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Input and Sort Integer Array" << endl;
        cout << "2. Input and Sort Float Array" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";

        int choice;
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter " << maxSize << " integer elements: ";
            for (int i = 0; i < maxSize; ++i) {
                cin >> intArray[i];
            }
            selectionSort(intArray, maxSize);
            cout << "Sorted Integer Array: ";
            displayArray(intArray, maxSize);
            break;
        case 2:
            cout << "Enter " << maxSize << " float elements: ";
            for (int i = 0; i < maxSize; ++i) {
                cin >> floatArray[i];
            }
            selectionSort(floatArray, maxSize);
            cout << "Sorted Float Array: ";
            displayArray(floatArray, maxSize);
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
