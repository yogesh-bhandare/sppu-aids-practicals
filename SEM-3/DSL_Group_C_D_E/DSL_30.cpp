//Yogesh Bhandare SE AIDS 22506
//Write program to implement a priority queue in C++ using an inorder list to store the items
//in the queue.Create a class that includes the data items(which should be template) and the
//priority(which should be int).The inorder list should contain these objects, with operator <=
//overloaded so that the items with highest priority appear at the start of the list(which will
//	make it relatively easy to retrieve the highest item.)

#include<iostream>
using namespace std;

template <class T>
class PriorityNode {
public:
    T data;
    int priority;
    PriorityNode<T>* next;

    PriorityNode(T item, int p) {
        data = item;
        priority = p;
        next = nullptr;
    }
};

template <class T>
class PriorityQueue {
private:
    PriorityNode<T>* head;

public:
    PriorityQueue() {
        head = nullptr;
    }

    // Function to add an item with priority to the priority queue
    void enqueue(T item, int priority) {
        PriorityNode<T>* newNode = new PriorityNode<T>(item, priority);

        if (head == nullptr || priority > head->priority) {
            newNode->next = head;
            head = newNode;
        }
        else {
            PriorityNode<T>* current = head;

            while (current->next != nullptr && priority <= current->next->priority) {
                current = current->next;
            }

            newNode->next = current->next;
            current->next = newNode;
        }

        cout << "Item added to the priority queue." << endl;
    }

    // Function to dequeue (retrieve and remove) the item with the highest priority
    void dequeue() {
        if (head == nullptr) {
            cout << "Priority queue is empty." << endl;
        }
        else {
            PriorityNode<T>* temp = head;
            head = head->next;
            delete temp;
            cout << "Item dequeued successfully." << endl;
        }
    }

    // Function to display the items in the priority queue
    void display() {
        PriorityNode<T>* current = head;
        cout << "Priority Queue (highest priority to lowest priority): ";
        while (current != nullptr) {
            cout << "(" << current->data << ", " << current->priority << ") ";
            current = current->next;
        }
        cout << endl;
    }
};

int main() {
    PriorityQueue<int> priorityQueue;
    int choice, item, priority;
    char continueChoice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Enqueue (Add item with priority)" << endl;
        cout << "2. Dequeue (Retrieve and remove item with highest priority)" << endl;
        cout << "3. Display Priority Queue" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter item: ";
            cin >> item;
            cout << "Enter priority: ";
            cin >> priority;
            priorityQueue.enqueue(item, priority);
            break;
        case 2:
            priorityQueue.dequeue();
            break;
        case 3:
            priorityQueue.display();
            break;
        case 4:
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