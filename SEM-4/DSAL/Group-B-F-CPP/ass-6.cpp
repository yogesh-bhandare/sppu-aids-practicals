#include<iostream>
#include<algorithm>
using namespace std;

class Node
{
public:
	int data;
	Node* left = NULL;
	Node* right = NULL;
	Node(int val)
	{
		data = val;
		left = right = NULL;
	}
};

class BST
{
public:
	Node* insert(Node* root, int val)
	{
		if (root == NULL) return new Node(val);
		Node* cur = root;
		while (true)
		{
			if (cur->data <= val)
			{
				if (cur->right != NULL)
				{
					cur = cur->right;
				}
				else
				{
					cur->right = new Node(val);
					break;
				}
			}
			else
			{
				if (cur->left != NULL)
				{
					cur = cur->left;
				}
				else
				{
					cur->left = new Node(val);
					break;
				}
			}
		}
		return root;
	}

	void preorder(Node* root)
	{
		if (root == NULL)
			return;
		cout << root->data << " ";
		preorder(root->left);
		preorder(root->right);
	}

	void inorder(Node* root)
	{
		if (root == NULL)
			return;
		inorder(root->left);
		cout << root->data << " ";
		inorder(root->right);
	}

	void postorder(Node* root)
	{
		if (root == NULL)
			return;
		postorder(root->left);
		postorder(root->right);
		cout << root->data << " ";
	}

	int minVal(Node* root)
	{
		if (root->left == NULL)
		{
			return root->data;
		}
		minVal(root->left);
	}

	int maxVal(Node* root)
	{
		if (root->right == NULL)
		{
			return root->data;
		}
		maxVal(root->right);
	}

	int calHeight(Node* root)
	{
		if (root == NULL)
			return 0;
		return max(1 + calHeight(root->left), 1 + calHeight(root->right));
	}

	bool search(Node* root, int val)
	{
		if (root == NULL)
			return false;

		bool ans = false;

		ans |= search(root->left, val);
		if (root->data == val)
		{
			return true;
		}
		ans |= search(root->right, val);

		return ans;
	}

	void swapTree(Node* root)
	{
		if (root == NULL)
			return;
		swapTree(root->left);
		swapTree(root->right);

		Node* temp = root->left;
		root->left = root->right;
		root->right = temp;
	}
};

int main() {
	BST t;
	Node* root = NULL;

	int numNodes;
	cout << "Enter the number of nodes to insert: ";
	cin >> numNodes;

	cout << "Enter " << numNodes << " values to insert into the BST:" << endl;
	for (int i = 0; i < numNodes; ++i) {
		int value;
		cin >> value;
		root = t.insert(root, value);
	}

	char choice;
	do {
		int operationChoice;
		cout << "Enter your choice:\n1. Inorder\n2. Search\n3. Min\n4. Max\n5. Calculate Height\n6. Mirror\n";
		cin >> operationChoice;

		switch (operationChoice) {
		case 1:
			cout << "Inorder: ";
			t.inorder(root);
			cout << endl;
			break;
		case 2: {
			int key;
			cout << "Enter key to search: ";
			cin >> key;
			cout << "Search Found: " << (t.search(root, key) ? "true" : "false") << endl;
			break;
		}
		case 3:
			cout << "Min: " << t.minVal(root) << endl;
			break;
		case 4:
			cout << "Max: " << t.maxVal(root) << endl;
			break;
		case 5:
			cout << "Calculate Height: " << t.calHeight(root) << endl;
			break;
		case 6:
			cout << "Mirror: ";
			t.swapTree(root);
			t.inorder(root);
			cout << endl;
			break;
		default:
			cout << "Invalid choice!" << endl;
		}

		cout << "Do you want to continue? (y/n): ";
		cin >> choice;
	} while (choice == 'y' || choice == 'Y');

	return 0;
}