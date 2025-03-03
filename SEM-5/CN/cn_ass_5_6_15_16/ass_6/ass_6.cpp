#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <limits>
#include <stdexcept>

using namespace std;

// Dijkstra's Algorithm (Link State Routing)
unordered_map<char, int> dijkstra(const unordered_map<char, unordered_map<char, int>>& graph, char start) {
    // Priority queue to store (cost, node)
    priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> pq;
    // Map to store the shortest path to each node
    unordered_map<char, int> distances;
    for (const auto& pair : graph) {
        distances[pair.first] = numeric_limits<int>::max();
    }
    distances[start] = 0;
    pq.push({ 0, start });

    while (!pq.empty()) {
        int current_distance = pq.top().first;
        char current_node = pq.top().second;
        pq.pop();

        if (current_distance > distances[current_node]) {
            continue;
        }

        // Check neighbors of the current node
        for (const auto& neighbor : graph.at(current_node)) {
            char next_node = neighbor.first;
            int weight = neighbor.second;
            int distance = current_distance + weight;

            if (distance < distances[next_node]) {
                distances[next_node] = distance;
                pq.push({ distance, next_node });
            }
        }
    }

    return distances;
}

// Bellman-Ford Algorithm (Distance Vector Routing)
unordered_map<char, int> bellmanFord(const unordered_map<char, unordered_map<char, int>>& graph, char start) {
    // Initialize distances from start to all other nodes as infinity
    unordered_map<char, int> distances;
    for (const auto& pair : graph) {
        distances[pair.first] = numeric_limits<int>::max();
    }
    distances[start] = 0;

    // Relax edges |V| - 1 times (V is the number of vertices)
    for (size_t i = 0; i < graph.size() - 1; ++i) {
        for (const auto& node : graph) {
            char u = node.first;
            for (const auto& neighbor : graph.at(u)) {
                char v = neighbor.first;
                int weight = neighbor.second;
                if (distances[u] != numeric_limits<int>::max() && distances[u] + weight < distances[v]) {
                    distances[v] = distances[u] + weight;
                }
            }
        }
    }

    // Check for negative-weight cycles
    for (const auto& node : graph) {
        char u = node.first;
        for (const auto& neighbor : graph.at(u)) {
            char v = neighbor.first;
            int weight = neighbor.second;
            if (distances[u] != numeric_limits<int>::max() && distances[u] + weight < distances[v]) {
                throw runtime_error("Graph contains a negative-weight cycle");
            }
        }
    }

    return distances;
}

int main() {
    unordered_map<char, unordered_map<char, int>> graph = {
        {'A', {{'B', 5}, {'C', 10}}},
        {'B', {{'A', 5}, {'C', 3}, {'D', 9}}},
        {'C', {{'A', 10}, {'B', 3}, {'D', 7}}},
        {'D', {{'B', 9}, {'C', 7}}}
    };

    char start_node = 'A';

    auto distances = dijkstra(graph, start_node);
    cout << "Shortest paths from " << start_node << " (Link State Routing - Dijkstra's Algorithm):" << endl;
    for (const auto& pair : distances) {
        cout << "To " << pair.first << ": " << pair.second << endl;
    }

    try {
        auto distances_bf = bellmanFord(graph, start_node);
        cout << "\nShortest paths from " << start_node << " (Distance Vector Routing - Bellman-Ford Algorithm):" << endl;
        for (const auto& pair : distances_bf) {
            cout << "To " << pair.first << ": " << pair.second << endl;
        }
    }
    catch (const exception& e) {
        cout << e.what() << endl;
    }

    return 0;
}
