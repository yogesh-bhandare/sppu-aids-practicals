//Yogesh Bhandare SE AIDS 22506
//Implement C++ program for expression conversion as infix to postfix and its evaluation
//using stack based on given conditions :
//1. Operands and operator, both must be single character.
//2. Input Postfix expression must be in a desired format.
//3. Only '+', '-', '*' and '/ ' operators are expected.

#include<iostream>
#include<stack>
#include<cctype>
#include<cmath>
using namespace std;

// Function to check if a character is an operator
bool isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

// Function to get the precedence of an operator
int getPrecedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    else if (op == '*' || op == '/') {
        return 2;
    }
    return 0; // for other characters
}

// Function to convert infix expression to postfix
string infixToPostfix(const string& infix) {
    stack<char> operatorStack;
    string postfix = "";

    for (char ch : infix) {
        if (isalnum(ch)) {
            postfix += ch;
        }
        else if (ch == '(') {
            operatorStack.push(ch);
        }
        else if (ch == ')') {
            while (!operatorStack.empty() && operatorStack.top() != '(') {
                postfix += operatorStack.top();
                operatorStack.pop();
            }
            if (!operatorStack.empty() && operatorStack.top() == '(') {
                operatorStack.pop();
            }
        }
        else if (isOperator(ch)) {
            while (!operatorStack.empty() && getPrecedence(ch) <= getPrecedence(operatorStack.top())) {
                postfix += operatorStack.top();
                operatorStack.pop();
            }
            operatorStack.push(ch);
        }
    }

    while (!operatorStack.empty()) {
        postfix += operatorStack.top();
        operatorStack.pop();
    }

    return postfix;
}

// Function to evaluate postfix expression
double evaluatePostfix(const string& postfix) {
    stack<double> operandStack;

    for (char ch : postfix) {
        if (isalnum(ch)) {
            operandStack.push(ch - '0'); // Convert character to integer
        }
        else if (isOperator(ch)) {
            double operand2 = operandStack.top();
            operandStack.pop();
            double operand1 = operandStack.top();
            operandStack.pop();

            switch (ch) {
            case '+':
                operandStack.push(operand1 + operand2);
                break;
            case '-':
                operandStack.push(operand1 - operand2);
                break;
            case '*':
                operandStack.push(operand1 * operand2);
                break;
            case '/':
                if (operand2 != 0) {
                    operandStack.push(operand1 / operand2);
                }
                else {
                    cerr << "Error: Division by zero" << endl;
                    return NAN; // Return NaN for undefined result
                }
                break;
            }
        }
    }

    if (!operandStack.empty()) {
        return operandStack.top();
    }
    else {
        cerr << "Error: Invalid postfix expression" << endl;
        return NAN;
    }
}

int main() {
    string infixExpression;
    char continueChoice;

    do {
        cout << "Enter an infix expression: ";
        cin >> infixExpression;

        // Convert infix to postfix
        string postfixExpression = infixToPostfix(infixExpression);
        cout << "Postfix expression: " << postfixExpression << endl;

        // Evaluate postfix expression
        double result = evaluatePostfix(postfixExpression);
        if (!isnan(result)) {
            cout << "Result: " << result << endl;
        }

        cout << "Do you want to continue? (y/n): ";
        cin >> continueChoice;
    } while (continueChoice == 'y' || continueChoice == 'Y');

    return 0;
}
