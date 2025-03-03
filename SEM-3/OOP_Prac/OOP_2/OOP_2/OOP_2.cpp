#include<iostream>
#include<string>
using namespace std;

class Student
{
private:
	int rollnumber;
	int phonenumber;
	string name;
	string division;
	string class_name;
public:
	//Default constructor
	Student() : rollnumber(0), phonenumber(0), name(""), division(""), class_name(""){}
	//Parameterized Conatructor
	Student(int rollnum, int phone, string n, string d, string cn) : rollnumber(rollnum), phonenumber(phone), name(n), division(d), class_name(cn){}
	//Copy Constructor
	Student(const Student& other)
	{
		this->rollnumber=other.rollnumber;
		this->name=other.name;
		this->division=other.division;
		this->class_name=other.class_name;
		this->phonenumber=other.phonenumber;
	}
	//Input
	void input()
	{
		cout << "Enter Name of student: ";
		cin >> name;
		cout << "Enter Roll Number: ";
		cin >> rollnumber;
		cout << "Enter Division: ";
		cin >> division;
		cout << "Enter Class: ";
		cin >> class_name;
		cout << "Enter Phone Number: ";
		cin >> phonenumber;
	}
	//Output
	void output()
	{
		cout << "Student Name is: " << name << endl;
		cout << "Student Roll Number is: " << rollnumber << endl;
		cout << "Student Division is: " << division << endl;
		cout << "Student Class is: " << class_name << endl;
		cout << "Student Phonenumber is: " << phonenumber << endl;
	}
};

int main()
{
	Student student[3];
	for (int i = 0; i < 3; i++)
	{
		student->input();
	}

	cin.get();
}