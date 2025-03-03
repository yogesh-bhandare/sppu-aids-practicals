//#include <iostream>
//#include <stack>
//#include <cctype>
//
//using namespace std;
//
//// Structure for the expression tree node
//struct TreeNode {
//    char data;
//    TreeNode* left;
//    TreeNode* right;
//};
//
//// Function to check if a character is an operator
//bool isOperator(char c) {
//    return (c == '+' || c == '-' || c == '*' || c == '/');
//}
//
//// Function to create a new expression tree node
//TreeNode* createNode(char data) {
//    TreeNode* newNode = new TreeNode;
//    newNode->data = data;
//    newNode->left = nullptr;
//    newNode->right = nullptr;
//    return newNode;
//}
//
//// Function to construct the expression tree from the given prefix expression
//TreeNode* constructExpressionTree(string prefixExpression) {
//    stack<TreeNode*> st;
//    int length = prefixExpression.length();
//    for (int i = length - 1; i >= 0; i--) {
//        if (isalnum(prefixExpression[i])) {
//            TreeNode* newNode = createNode(prefixExpression[i]);
//            st.push(newNode);
//        }
//        else if (isOperator(prefixExpression[i])) {
//            TreeNode* newNode = createNode(prefixExpression[i]);
//            newNode->left = st.top();
//            st.pop();
//            newNode->right = st.top();
//            st.pop();
//            st.push(newNode);
//        }
//    }
//    return st.top();
//}
//
//// Function to traverse the expression tree using post-order traversal (non-recursive)
//void postOrderTraversal(TreeNode* root) {
//    if (root == nullptr) return;
//    stack<TreeNode*> st;
//    do {
//        while (root) {
//            if (root->right)
//                st.push(root->right);
//            st.push(root);
//            root = root->left;
//        }
//        root = st.top();
//        st.pop();
//        if (root->right && !st.empty() && root->right == st.top()) {
//            st.pop();
//            st.push(root);
//            root = root->right;
//        }
//        else {
//            cout << root->data << " ";
//            root = nullptr;
//        }
//    } while (!st.empty());
//}
//
//// Function to delete the entire expression tree
//void deleteTree(TreeNode* root) {
//    if (root == nullptr) return;
//    deleteTree(root->left);
//    deleteTree(root->right);
//    delete root;
//}
//
//int main() {
//    string prefixExpression = "+--a*bc/def";
//    TreeNode* root = constructExpressionTree(prefixExpression);
//
//    cout << "Post-order traversal: ";
//    postOrderTraversal(root);
//    cout << endl;
//
//    deleteTree(root); // Deleting the entire tree
//
//    return 0;
//}
