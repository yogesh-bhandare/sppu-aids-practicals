#include <iostream>
#include <vector>
#include <climits>

using namespace std;

#define V 5 // Number of vertices (routers)
#define E 8 // Number of edges (connections between routers)

// Structure to represent an edge
struct Edge {
    int src, dest, weight;
};

// Function to print the shortest distances
void printSolution(int dist[]) {
    cout << "Vertex \t Distance from Source" << endl;
    for (int i = 0; i < V; i++) {
        cout << i << " \t\t " << dist[i] << endl;
    }
}

// Bellman-Ford algorithm to find the shortest path
void bellmanFord(vector<Edge>& edges, int src) {
    int dist[V];

    // Initialize distances from src to all vertices as infinite and src to itself as 0
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
    }
    dist[src] = 0;

    // Relax all edges |V| - 1 times
    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].src;
            int v = edges[j].dest;
            int weight = edges[j].weight;
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
            }
        }
    }

    // Check for negative-weight cycles
    for (int i = 0; i < E; i++) {
        int u = edges[i].src;
        int v = edges[i].dest;
        int weight = edges[i].weight;
        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
            cout << "Graph contains negative weight cycle" << endl;
            return;
        }
    }

    printSolution(dist);
}

int main() {
    vector<Edge> edges(E);

    // Adding edges to the graph (src, dest, weight)
    edges[0] = { 0, 1, 10 };
    edges[1] = { 0, 3, 30 };
    edges[2] = { 0, 4, 100 };
    edges[3] = { 1, 2, 50 };
    edges[4] = { 2, 4, 10 };
    edges[5] = { 3, 2, 20 };
    edges[6] = { 3, 4, 60 };
    edges[7] = { 4, 2, 10 };

    bellmanFord(edges, 0); // Find shortest paths from vertex 0 (source)

    return 0;
}
