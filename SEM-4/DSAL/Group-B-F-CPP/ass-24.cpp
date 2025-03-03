//#include <iostream>
//#include <fstream>
//#include <iomanip>
//
//using namespace std;
//
//struct Employee {
//    int empID;
//    char name[50];
//    char designation[50];
//    float salary;
//};
//
//const int MAX_EMPLOYEES = 100;
//
//// Function to add a new employee to the file
//void addEmployee(fstream& file) {
//    Employee emp;
//    cout << "Enter Employee ID: ";
//    cin >> emp.empID;
//    cout << "Enter Name: ";
//    cin.ignore();
//    cin.getline(emp.name, 50);
//    cout << "Enter Designation: ";
//    cin.getline(emp.designation, 50);
//    cout << "Enter Salary: ";
//    cin >> emp.salary;
//
//    file.seekp(0, ios::end);
//    file.write(reinterpret_cast<char*>(&emp), sizeof(Employee));
//}
//
//// Function to delete an employee from the file
//void deleteEmployee(fstream& file, int empID) {
//    Employee emp;
//    int found = 0;
//    file.seekg(0);
//    ofstream tempFile("temp.dat", ios::out | ios::binary);
//    while (file.read(reinterpret_cast<char*>(&emp), sizeof(Employee))) {
//        if (emp.empID != empID)
//            tempFile.write(reinterpret_cast<char*>(&emp), sizeof(Employee));
//        else
//            found = 1;
//    }
//    tempFile.close();
//    file.close();
//    remove("employees.dat");
//    rename("temp.dat", "employees.dat");
//
//    if (found == 0)
//        cout << "Employee with ID " << empID << " not found." << endl;
//    else
//        cout << "Employee with ID " << empID << " deleted successfully." << endl;
//}
//
//// Function to display information of a particular employee
//void displayEmployee(fstream& file, int empID) {
//    Employee emp;
//    int found = 0;
//    file.seekg(0);
//    while (file.read(reinterpret_cast<char*>(&emp), sizeof(Employee))) {
//        if (emp.empID == empID) {
//            found = 1;
//            cout << "Employee ID: " << emp.empID << endl;
//            cout << "Name: " << emp.name << endl;
//            cout << "Designation: " << emp.designation << endl;
//            cout << "Salary: " << emp.salary << endl;
//            break;
//        }
//    }
//    if (found == 0)
//        cout << "Employee with ID " << empID << " not found." << endl;
//}
//
//int main() {
//    fstream file("employees.dat", ios::in | ios::out | ios::binary);
//    if (!file) {
//        cerr << "Error: Unable to open file." << endl;
//        return 1;
//    }
//
//    int choice, empID;
//    do {
//        cout << "\nEmployee Management System" << endl;
//        cout << "1. Add Employee" << endl;
//        cout << "2. Delete Employee" << endl;
//        cout << "3. Display Employee" << endl;
//        cout << "4. Exit" << endl;
//        cout << "Enter your choice: ";
//        cin >> choice;
//
//        switch (choice) {
//        case 1:
//            addEmployee(file);
//            break;
//        case 2:
//            cout << "Enter Employee ID to delete: ";
//            cin >> empID;
//            deleteEmployee(file, empID);
//            break;
//        case 3:
//            cout << "Enter Employee ID to display: ";
//            cin >> empID;
//            displayEmployee(file, empID);
//            break;
//        case 4:
//            cout << "Exiting..." << endl;
//            break;
//        default:
//            cout << "Invalid choice. Please try again." << endl;
//        }
//    } while (choice != 4);
//
//    file.close();
//    return 0;
//}
