#include<iostream>
using namespace std;

//min heap
void mininsert(int arr[], int i)
{
	int parent = (i - 1) / 2;
	int cur = i;
	while (parent >= 0 && arr[parent] > arr[cur])
	{
		swap(arr[parent], arr[cur]);
		cur = parent;
		parent = (cur - 1) / 2;
	}
}

//max heap
void maxinsert(int arr[], int i)
{
	int parent = (i - 1) / 2;
	int cur = i;
	while (parent >= 0 && arr[parent] < arr[cur])
	{
		swap(arr[parent], arr[cur]);
		cur = parent;
		parent = (cur - 1) / 2;
	}
}

void displayminmarks(int arr[], int n)
{
	cout << "\nDisplaying min heap: " << endl;
	for (int i = 0; i < n; i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
	cout << "Min Marks: " << arr[0] << endl;
}

void displaymaxmarks(int arr[], int n)
{
	cout << "\nDisplaying max heap: " << endl;
	for (int i = 0; i < n; i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
	cout << "Max Marks: " << arr[0] << endl;
}

int main()
{
	int n;
	cout << "Enter total number of Marks to store in heap: ";
	cin >> n;
	int arr[20];

	for (int i = 0; i < n; i++)
	{
		cout << "Enter DSA marks: ";
		cin >> arr[i];
		cout << endl;
	}

	int choice = 0;
	while (choice != 3)
	{	
		cout << "\n1. To display minimum marks \n2. To display maximum marks \n3. Exit >> ";
		cin >> choice;
		switch (choice)
		{
		case 1:
			for (int i = 1; i < n; i++)
			{
				mininsert(arr, i);
			}
			displayminmarks(arr, n);
			break;
		case 2:
			for (int i = 1; i < n; i++)
			{
				maxinsert(arr, i);
			}
			displaymaxmarks(arr, n);
			break;
		case 3:
			return 0;
			break;
		default:
			cout << "Invalid choice." << endl;
		}
	}

	return 0;
}
