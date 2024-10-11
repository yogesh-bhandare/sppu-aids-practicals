#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>
using namespace std;

void addStudent()
{
	ofstream inputS("db.txt", ios::app);

	string rn, name, div, add;
	cout << "Enter Student Roll Number: ";
	cin >> rn;
	cout << endl;
	cout << "Enter Student Name: ";
	cin >> name;
	cout << endl;
	cout << "Enter Student Div: ";
	cin >> div;
	cout << endl;
	cout << "Enter Student Address: ";
	cin >> add;
	cout << endl;

	inputS << left << setw(20) << rn << setw(20) << name << setw(20) << div << setw(20) << add << endl;

	inputS.close();

}

void deleteStudent()
{
	ifstream printS("db.txt");
	string line, rn;
	cout << "Enter Student Roll Number to del: ";
	cin >> rn;

	string filedata;

	while (getline(printS, line))
	{
		if (line.find(rn) == string::npos)
		{
			filedata += line;
			filedata += "\n";
		}

	}
	printS.close();

	ofstream printm("db.txt", ios::out);
	printm << filedata;
	printm.close();
}

void searchStudent()
{
	ifstream printS("db.txt");
	string line, rn;
	cout << "Enter Student Roll Number to search: ";
	cin >> rn;

	bool found = false;

	while (getline(printS, line))
	{
		if (line.find(rn) != string::npos)
		{
			cout << "Student Details: " << endl;
			cout << line << endl;
			found = true;
			break;
		}
		
	}
	printS.close();

	if (!found)
	{
		cout << "Student does not exists." << endl;
	}
}

void printData()
{
	ifstream printS("db.txt");
	string line;
	cout << "\nPrinting file data..." << endl;
	while (getline(printS, line))
	{
		cout << line << endl;
	}
	cout << "Printing Completed" << endl;
	printS.close();
}

int main()
{
	ofstream f("db.txt");
	f << left << setw(20) << "Roll No." << setw(20) << "Name" << setw(20) << "Div" << setw(20) << "Add" << endl;
	f.close();

	int ip = 0;
	while (ip != 5)
	{
		cout << "---------Student Dashbord---------" << endl;
		cout << "1. Add Student.\n2. Delete Student.\n3. Search Student.\n4. Print Data.\n5. Exit." << endl;
		cout << "Enter your choice: ";
		cin >> ip;
		switch (ip)
		{
		case 1:
			addStudent();
			break;
		case 2:
			deleteStudent();
			break;
		case 3:
			searchStudent();
			break;
		case 4:
			printData();
			break;
		case 5:
			return 0;
			break;
		default:
			cout << "Please ReEnter choice. ";
			break;
		}
	}
}