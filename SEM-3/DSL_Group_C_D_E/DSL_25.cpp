//Yogesh Bhandare SE AIDS 22506
//A palindrome is a string of character that‘s the same forward and backward.Typically,
//punctuation, capitalization, and spaces are ignored.For example, “Poor Dan is in a droop” is
//a palindrome, as can be seen by examining the characters “poor danisina droop” and
//observing that they are the same forward and backward.One way to check for a palindrome
//is to reverse the characters in the string and then compare with them the original - in a
//palindrome, the sequence will be identical.Write C++ program with functions -
//a) To print original string followed by reversed string using stack
//b) To check whether given string is palindrome or not

#include<iostream>
#include<string>
using namespace std;

class stack
{
public:
    int size = 100;
    char arr[100];
    int top = -1;

    void push(char x)
    {
        if (top == size - 1)
        {
            cout << "Stack Overflow!!!" << endl;
            return;
        }

        top++;
        arr[top] = x;
    }

    char pop()
    {
        if (top == -1)
        {
            cout << "Stack Underflow!!!" << endl;
            return -1;
        }
        return arr[top--];
    }

    void display()
    {
        if (top == -1)
        {
            cout << "Stack is Empty." << endl;
        }
        cout << "Stack Contains: ";
        for (int i = 0; i < top + 1; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

void printOriginalAndReversed(stack& s, string user_input)
{
    string org_str = "";
    for (int i = 0; i < user_input.size(); i++)
    {
        char ch = user_input[i];

        if (ch >= 'a' and ch <= 'z')
        {
            ch = (char)(ch - 'a' + 'A');
        }
        if (ch >= 'A' and ch <= 'Z')
        {
            s.push(ch);
            org_str.push_back(ch);
        }
    }
    cout << "Entered String is: " << user_input << endl;
    cout << "Original String is: " << org_str << endl;

    s.display();

    cout << "Reversed String is: ";
    string rev_str = "";
    while (s.top != -1)
    {
        rev_str.push_back(s.pop());
    }

    cout << rev_str;

    bool is_palindrome = true;
    for (int i = 0; i < org_str.size(); i++)
    {
        if (org_str[i] != rev_str[i])
        {
            is_palindrome = false;
            break;
        }
    }
    cout << endl;
    cout << "Entered String is " << (is_palindrome ? "" : "not ") << "a Palindrome." << endl;
}

int main()
{
    stack s;
    string user_input;
    int choice;

    do
    {
        cout << "\nMenu:" << endl;
        cout << "1. Enter a new string" << endl;
        cout << "2. Check if the string is a palindrome" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cin.ignore(); // To clear the newline character from the previous input
            cout << "Enter String: ";
            getline(cin, user_input);
            break;
        case 2:
            printOriginalAndReversed(s, user_input);
            break;
        case 3:
            cout << "Exiting the program." << endl;
            break;
        default:
            cout << "Invalid choice. Please enter a valid option." << endl;
        }
    } while (choice != 3);

    return 0;
}
