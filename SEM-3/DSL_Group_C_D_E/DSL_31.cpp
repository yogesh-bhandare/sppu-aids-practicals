#include <iostream>
#include <cstdlib>

class Deque {
private:
    static const int MAX_SIZE = 5; // Adjust the size as needed
    int arr[MAX_SIZE];
    int front;
    int rear;

public:
    Deque() : front(-1), rear(-1) {}

    bool isFull() const {
        return (front == 0 && rear == MAX_SIZE - 1) || (front == rear + 1);
    }

    bool isEmpty() const {
        return front == -1;
    }

    void insertFront(int value) {
        if (isFull()) {
            std::cout << "Deque is full. Cannot insert at front.\n";
            return;
        }

        if (front == -1) {
            front = rear = 0;
        }
        else if (front == 0) {
            front = MAX_SIZE - 1;
        }
        else {
            front--;
        }

        arr[front] = value;
        std::cout << "Inserted " << value << " at the front.\n";
    }

    void insertRear(int value) {
        if (isFull()) {
            std::cout << "Deque is full. Cannot insert at rear.\n";
            return;
        }

        if (front == -1) {
            front = rear = 0;
        }
        else if (rear == MAX_SIZE - 1) {
            rear = 0;
        }
        else {
            rear++;
        }

        arr[rear] = value;
        std::cout << "Inserted " << value << " at the rear.\n";
    }

    void deleteFront() {
        if (isEmpty()) {
            std::cout << "Deque is empty. Cannot delete from front.\n";
            return;
        }

        std::cout << "Deleted " << arr[front] << " from the front.\n";

        if (front == rear) {
            front = rear = -1;
        }
        else if (front == MAX_SIZE - 1) {
            front = 0;
        }
        else {
            front++;
        }
    }

    void deleteRear() {
        if (isEmpty()) {
            std::cout << "Deque is empty. Cannot delete from rear.\n";
            return;
        }

        std::cout << "Deleted " << arr[rear] << " from the rear.\n";

        if (front == rear) {
            front = rear = -1;
        }
        else if (rear == 0) {
            rear = MAX_SIZE - 1;
        }
        else {
            rear--;
        }
    }

    void display() const {
        if (isEmpty()) {
            std::cout << "Deque is empty.\n";
            return;
        }

        std::cout << "Deque elements: ";
        int i = front;
        do {
            std::cout << arr[i] << " ";
            i = (i + 1) % MAX_SIZE;
        } while (i != (rear + 1) % MAX_SIZE);
        std::cout << "\n";
    }
};

int main() {
    Deque deque;

    char choice;
    do {
        std::cout << "\nMenu:\n";
        std::cout << "1. Insert at Front\n";
        std::cout << "2. Insert at Rear\n";
        std::cout << "3. Delete from Front\n";
        std::cout << "4. Delete from Rear\n";
        std::cout << "5. Display Deque\n";
        std::cout << "6. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
        case '1': {
            int value;
            std::cout << "Enter value to insert at the front: ";
            std::cin >> value;
            deque.insertFront(value);
            break;
        }

        case '2': {
            int value;
            std::cout << "Enter value to insert at the rear: ";
            std::cin >> value;
            deque.insertRear(value);
            break;
        }

        case '3':
            deque.deleteFront();
            break;

        case '4':
            deque.deleteRear();
            break;

        case '5':
            deque.display();
            break;

        case '6':
            std::cout << "Exiting the program.\n";
            break;

        default:
            std::cout << "Invalid choice. Please enter a valid option.\n";
        }

        // Prompt for continuation
        std::cout << "Do you want to continue? (y/n): ";
        std::cin >> choice;

    } while (choice == 'y' || choice == 'Y');

    return 0;
}
