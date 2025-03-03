//#include<iostream>
//using namespace std;
//
//class node
//{
//public:
//	int data;
//	node* next;
//	node(int d)
//	{
//		data = d;
//		next = nullptr;
//	}
//}*hashTable[10]; 
//
//class hashing
//{
//public:
//	hashing()
//	{
//		for (int i = 0; i < 10; i++)
//		{
//			hashTable[i] = nullptr;
//		}
//	}
//
//	int hashFunction(int val)
//	{
//		return val % 10;
//	}
//
//	void display()
//	{
//		for (int i = 0; i < 10; i++)
//		{
//			node* temp = hashTable[i];
//			cout << "a[" << i << "]: ";
//			while (temp != NULL)
//			{
//				cout << temp->data << "->";
//				temp = temp->next;
//			}
//			cout << endl;
//		}
//	}
//
//	int searchElement(int val)
//	{
//		bool flag = true;
//		int hash_val = hashFunction(val);
//		node* temp = hashTable[hash_val];
//		while (temp != NULL)
//		{
//			if (temp->data == val)
//			{
//				cout << "Element found at: " << hash_val << ": " << temp->data << endl;
//				flag = true;
//			}
//			temp = temp->next;
//		}
//		if (!flag) return -1;
//	}
//
//	void deleteElement(int val)
//	{
//		int hash_val = hashFunction(val);
//		node* temp = hashTable[hash_val];
//		if (temp == NULL)
//		{
//			cout << "Element Not Found";
//			return;
//		}
//		if (temp->data == val)
//		{
//			hashTable[hash_val] = temp->next;
//			return;
//		}
//		while (temp->next->data != val)
//		{
//			temp = temp->next;
//		}
//		temp->next = temp->next->next;
//	}
//
//	void insertElement(int val)
//	{
//		int hash_val = hashFunction(val);
//		node* temp = hashTable[hash_val];
//		node* head = new node(val);
//		if (temp == NULL)
//		{
//			hashTable[hash_val] = head;
//			return;
//		}
//		else
//		{
//			while (temp->next != NULL)
//			{
//				temp = temp->next;
//			}
//			temp->next = head;
//		}
//	}
//};
//
//int main()
//{
//	int ch;
//	int data, search, del;
//	hashing h;
//	do
//	{
//		cout << "+++++++++Telephone Book+++++++++\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit>> " << endl;
//		cin >> ch;
//		switch (ch)
//		{
//		case 1:
//			cout << "Enter New Telephone Number: ";
//			cin >> data;
//			h.insertElement(data);
//			break;
//		case 2:
//			cout << "Enter Telephone Number to delete: ";
//			cin >> del;
//			h.deleteElement(del);
//			break;
//		case 3:
//			cout << "Enter Number to search: ";
//			cin >> search;
//			h.searchElement(search);
//			break;
//		case 4:
//			h.display();
//			break;
//		}
//	} while (ch != 5);
//}