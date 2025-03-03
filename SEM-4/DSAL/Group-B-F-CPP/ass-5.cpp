//#include <iostream>
//using namespace std;
//
//class Node {
//public:
//    string name;
//    Node* next;
//    Node* down;
//    Node(string n) : name(n), next(nullptr), down(nullptr) {};
//};
//
//class Tree {
//public:
//    Node* root;
//    Tree() : root(nullptr) {};
//
//    void addChild(Node* parent, string name) {
//        if (parent == nullptr) {
//            cout << "Cannot add child to null" << endl;
//            return;
//        }
//        if (parent->down == nullptr) {
//            parent->down = new Node(name);
//        }
//        else {
//            Node* lastChild = parent->down;
//            while (lastChild->next != nullptr) {
//                lastChild = lastChild->next;
//            }
//            lastChild->next = new Node(name);
//        }
//    }
//
//    // Function to insert a book
//    void insertBook(string name) {
//        if (root == nullptr) {
//            root = new Node(name);
//            cout << "Book '" << name << "' inserted." << endl;
//        }
//        else {
//            cout << "Book already exists." << endl;
//        }
//    }
//
//    // Function to insert a chapter
//    void insertChapter(string name) {
//        if (root == nullptr) {
//            cout << "Please insert a book first." << endl;
//            return;
//        }
//        addChild(root, name);
//        cout << "Chapter '" << name << "' inserted." << endl;
//    }
//
//    // Function to insert a section
//    void insertSection(string name) {
//        if (root == nullptr) {
//            cout << "Please insert a book first." << endl;
//            return;
//        }
//        if (root->down == nullptr) {
//            cout << "Please insert a chapter first." << endl;
//            return;
//        }
//        addChild(root->down, name);
//        cout << "Section '" << name << "' inserted." << endl;
//    }
//
//    // Function to insert a subsection
//    void insertSubsection(string name) {
//        if (root == nullptr) {
//            cout << "Please insert a book first." << endl;
//            return;
//        }
//        if (root->down == nullptr) {
//            cout << "Please insert a chapter first." << endl;
//            return;
//        }
//        if (root->down->down == nullptr) {
//            cout << "Please insert a section first." << endl;
//            return;
//        }
//        addChild(root->down->down, name);
//        cout << "Subsection '" << name << "' inserted." << endl;
//    }
//
//    void printNodes(Node* root, int depth = 0) {
//        if (root == nullptr) return;
//
//        for (int i = 0; i < depth; i++)
//            cout << "    ";
//        cout << root->name << endl;
//
//        printNodes(root->down, depth + 1);
//        printNodes(root->next, depth);
//    }
//};
//
//int main() {
//    Tree book;
//
//    int choice;
//    string name;
//
//    while (true) {
//        cout << "Menu:\n";
//        cout << "1. Insert Book\n";
//        cout << "2. Insert Chapter\n";
//        cout << "3. Insert Section\n";
//        cout << "4. Insert Subsection\n";
//        cout << "5. Display Book Structure\n";
//        cout << "6. Exit\n";
//        cout << "Enter your choice: ";
//        cin >> choice;
//
//        switch (choice) {
//        case 1:
//            cout << "Enter book name: ";
//            cin >> name;
//            book.insertBook(name);
//            break;
//        case 2:
//            cout << "Enter chapter name: ";
//            cin >> name;
//            book.insertChapter(name);
//            break;
//        case 3:
//            cout << "Enter section name: ";
//            cin >> name;
//            book.insertSection(name);
//            break;
//        case 4:
//            cout << "Enter subsection name: ";
//            cin >> name;
//            book.insertSubsection(name);
//            break;
//        case 5:
//            cout << "Book structure:\n";
//            book.printNodes(book.root);
//            break;
//        case 6:
//            cout << "Exiting...\n";
//            return 0;
//        default:
//            cout << "Invalid choice. Please try again.\n";
//        }
//    }
//
//    return 0;
//}
