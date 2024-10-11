//#include <iostream>
//#include <vector>
//#include <limits>
//using namespace std;
//
//float sumProbabilities(const vector<float>& probabilities, int i, int j) {
//    float sum = 0;
//    for (int k = i; k <= j; k++) {
//        sum += probabilities[k];
//    }
//    return sum;
//}
//
//float optimalBST(const vector<float>& probabilities, int n) {
//    vector<vector<float> > cost(n + 1, vector<float>(n + 1, 0));
//
//    for (int i = 0; i < n; i++) {
//        cost[i][i] = probabilities[i];
//    }
//
//    for (int length = 2; length <= n; length++) {
//        for (int i = 0; i <= n - length + 1; i++) {
//            int j = i + length - 1;
//            cost[i][j] = numeric_limits<float>::max();
//            for (int r = i; r <= j; r++) {
//                float c = ((r > i) ? cost[i][r - 1] : 0) +
//                    ((r < j) ? cost[r + 1][j] : 0) +
//                    sumProbabilities(probabilities, i, j);
//                if (c < cost[i][j]) {
//                    cost[i][j] = c;
//                }
//            }
//        }
//    }
//
//    return cost[0][n - 1];
//}
//
//int main() {
//    int n;
//    cout << "Enter the number of keys: ";
//    cin >> n;
//
//    vector<float> probabilities(n);
//    cout << "Enter the probabilities for each key:" << endl;
//    for (int i = 0; i < n; i++) {
//        cin >> probabilities[i];
//    }
//
//    float minCost = optimalBST(probabilities, n);
//    cout << "The minimum search cost of the optimal BST is: " << minCost << endl;
//
//    return 0;
//}