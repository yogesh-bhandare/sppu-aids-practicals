//#include <iostream>
//#include <string>
//
//using namespace std;
//
//// Structure to store keyword and its meaning
//struct Node {
//    string keyword;
//    string meaning;
//    Node* left;
//    Node* right;
//    int height;
//};
//
//// Function to get maximum of two integers
//int max(int a, int b) {
//    return (a > b) ? a : b;
//}
//
//// Function to get the height of a node
//int getHeight(Node* node) {
//    if (node == NULL)
//        return 0;
//    return node->height;
//}
//
//// Function to create a new node
//Node* newNode(string keyword, string meaning) {
//    Node* node = new Node();
//    node->keyword = keyword;
//    node->meaning = meaning;
//    node->left = NULL;
//    node->right = NULL;
//    node->height = 1;
//    return node;
//}
//
//// Function to right rotate subtree rooted with y
//Node* rightRotate(Node* y) {
//    Node* x = y->left;
//    Node* T2 = x->right;
//
//    // Perform rotation
//    x->right = y;
//    y->left = T2;
//
//    // Update heights
//    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
//    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
//
//    // Return new root
//    return x;
//}
//
//// Function to left rotate subtree rooted with x
//Node* leftRotate(Node* x) {
//    Node* y = x->right;
//    Node* T2 = y->left;
//
//    // Perform rotation
//    y->left = x;
//    x->right = T2;
//
//    // Update heights
//    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
//    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
//
//    // Return new root
//    return y;
//}
//
//// Get the balance factor of a node
//int getBalance(Node* node) {
//    if (node == NULL)
//        return 0;
//    return getHeight(node->left) - getHeight(node->right);
//}
//
//// Function to insert a node into the AVL tree
//Node* insert(Node* node, string keyword, string meaning) {
//    // Perform the normal BST insertion
//    if (node == NULL)
//        return newNode(keyword, meaning);
//
//    if (keyword < node->keyword)
//        node->left = insert(node->left, keyword, meaning);
//    else if (keyword > node->keyword)
//        node->right = insert(node->right, keyword, meaning);
//    else { // Keyword already exists, update meaning
//        node->meaning = meaning;
//        return node;
//    }
//
//    // Update height of this ancestor node
//    node->height = 1 + max(getHeight(node->left), getHeight(node->right));
//
//    // Get the balance factor to check whether this node became unbalanced
//    int balance = getBalance(node);
//
//    // If unbalanced, there are 4 possible cases
//
//    // Left Left Case
//    if (balance > 1 && keyword < node->left->keyword)
//        return rightRotate(node);
//
//    // Right Right Case
//    if (balance < -1 && keyword > node->right->keyword)
//        return leftRotate(node);
//
//    // Left Right Case
//    if (balance > 1 && keyword > node->left->keyword) {
//        node->left = leftRotate(node->left);
//        return rightRotate(node);
//    }
//
//    // Right Left Case
//    if (balance < -1 && keyword < node->right->keyword) {
//        node->right = rightRotate(node->right);
//        return leftRotate(node);
//    }
//
//    // If the node is balanced, return unchanged node pointer
//    return node;
//}
//
//// Function to find the node with minimum key value in a subtree
//Node* minValueNode(Node* node) {
//    Node* current = node;
//    while (current->left != NULL)
//        current = current->left;
//    return current;
//}
//
//// Function to delete a node from the AVL tree
//Node* deleteNode(Node* root, string keyword) {
//    if (root == NULL)
//        return root;
//
//    // Perform standard BST delete
//    if (keyword < root->keyword)
//        root->left = deleteNode(root->left, keyword);
//    else if (keyword > root->keyword)
//        root->right = deleteNode(root->right, keyword);
//    else {
//        // Node with only one child or no child
//        if ((root->left == NULL) || (root->right == NULL)) {
//            Node* temp = root->left ? root->left : root->right;
//
//            // No child case
//            if (temp == NULL) {
//                temp = root;
//                root = NULL;
//            }
//            else // One child case
//                *root = *temp; // Copy the contents of the non-empty child
//
//            delete temp;
//        }
//        else {
//            // Node with two children: Get the inorder successor (smallest in the right subtree)
//            Node* temp = minValueNode(root->right);
//
//            // Copy the inorder successor's data to this node
//            root->keyword = temp->keyword;
//            root->meaning = temp->meaning;
//
//            // Delete the inorder successor
//            root->right = deleteNode(root->right, temp->keyword);
//        }
//    }
//
//    // If the tree had only one node, then return
//    if (root == NULL)
//        return root;
//
//    // Update height of the current node
//    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
//
//    // Get the balance factor to check whether this node became unbalanced
//    int balance = getBalance(root);
//
//    // If unbalanced, there are 4 possible cases
//
//    // Left Left Case
//    if (balance > 1 && getBalance(root->left) >= 0)
//        return rightRotate(root);
//
//    // Left Right Case
//    if (balance > 1 && getBalance(root->left) < 0) {
//        root->left = leftRotate(root->left);
//        return rightRotate(root);
//    }
//
//    // Right Right Case
//    if (balance < -1 && getBalance(root->right) <= 0)
//        return leftRotate(root);
//
//    // Right Left Case
//    if (balance < -1 && getBalance(root->right) > 0) {
//        root->right = rightRotate(root->right);
//        return leftRotate(root);
//    }
//
//    // If the node is balanced, return unchanged node pointer
//    return root;
//}
//
//// Function to search for a keyword and return its meaning
//string search(Node* root, string keyword, int& comparisons) {
//    while (root != NULL) {
//        comparisons++;
//        if (keyword < root->keyword)
//            root = root->left;
//        else if (keyword > root->keyword)
//            root = root->right;
//        else
//            return root->meaning;
//    }
//    return "Keyword not found";
//}
//
//// Function to find maximum comparisons required for finding a keyword
//int maxComparisons(Node* root) {
//    if (root == NULL)
//        return 0;
//
//    // Traverse to the rightmost node, which will have the maximum height
//    int comparisons = 0;
//    while (root->right != NULL) {
//        comparisons++;
//        root = root->right;
//    }
//    return comparisons + 1; // Adding 1 for the last comparison
//}
//
//// Function to display the AVL tree in ascending order (inorder traversal)
//void displayAscending(Node* root) {
//    if (root != NULL) {
//        displayAscending(root->left);
//        cout << root->keyword << " : " << root->meaning << endl;
//        displayAscending(root->right);
//    }
//}
//
//// Function to display the AVL tree in descending order
//void displayDescending(Node* root) {
//    if (root != NULL) {
//        displayDescending(root->right);
//        cout << root->keyword << " : " << root->meaning << endl;
//        displayDescending(root->left);
//    }
//}
//
//int main() {
//    Node* root = NULL;
//    int choice, comparisons;
//    string keyword, meaning;
//
//    do {
//        cout << "\n1. Add a new keyword\n2. Delete a keyword\n3. Update meaning of a keyword\n";
//        cout << "4. Display data in ascending order\n5. Display data in descending order\n";
//        cout << "6. Search for a keyword\n7. Maximum comparisons required for finding a keyword\n";
//        cout << "8. Exit\nEnter your choice: ";
//        cin >> choice;
//
//        switch (choice) {
//        case 1:
//            cout << "Enter keyword: ";
//            cin >> keyword;
//            cout << "Enter meaning: ";
//            cin.ignore(); // Ignore newline character
//            getline(cin, meaning);
//            root = insert(root, keyword, meaning);
//            break;
//        case 2:
//            cout << "Enter keyword to delete: ";
//            cin >> keyword;
//            root = deleteNode(root, keyword);
//            break;
//        case 3:
//            cout << "Enter keyword to update meaning: ";
//            cin >> keyword;
//            cout << "Enter new meaning: ";
//            cin.ignore(); // Ignore newline character
//            getline(cin, meaning);
//            root = deleteNode(root, keyword); // Delete old entry
//            root = insert(root, keyword, meaning); // Insert updated entry
//            break;
//        case 4:
//            cout << "Data in ascending order:\n";
//            displayAscending(root);
//            break;
//        case 5:
//            cout << "Data in descending order:\n";
//            displayDescending(root);
//            break;
//        case 6:
//            cout << "Enter keyword to search: ";
//            cin >> keyword;
//            comparisons = 0;
//            meaning = search(root, keyword, comparisons);
//            cout << "Meaning: " << meaning << endl;
//            cout << "Comparisons made: " << comparisons << endl;
//            break;
//        case 7:
//            comparisons = maxComparisons(root);
//            cout << "Maximum comparisons required for finding a keyword: " << comparisons << endl;
//            break;
//        case 8:
//            cout << "Exiting...\n";
//            break;
//        default:
//            cout << "Invalid choice. Please enter a valid option.\n";
//        }
//    } while (choice != 8);
//
//    return 0;
//}
