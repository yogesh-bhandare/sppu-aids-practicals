#include<iostream>
#include<vector>
#include<queue>
#include<map> 
using namespace std;

void dfs(vector<vector<int> >& graph, int start, vector<int>& visited)
{
    visited[start] = 1;
    cout << start << " ";
    for (size_t i = 0; i < graph[start].size(); i++)
    {
        int child = graph[start][i];
        if (!visited[child])
        {
            dfs(graph, child, visited);
        }
    }
}

void bfs(vector<vector<int> >& graph, int start)
{
    vector<int> visited(graph.size(), 0);
    queue<int> q;
    q.push(start);
    visited[start] = 1;

    while (!q.empty())
    {
        int cur = q.front();
        q.pop();
        cout << cur << " ";
        for (size_t i = 0; i < graph[cur].size(); i++)
        {
            int child = graph[cur][i];
            if (!visited[child])
            {
                q.push(child);
                visited[child] = 1;
            }
        }
    }
}

int main()
{
    char charChoice;
    do
    {
        int V;
        cout << "Enter number of vertices: ";
        cin >> V;
        vector<vector<int> > g;

        for (int i = 0; i < V; i++)
        {
            vector<int> temp;
            g.push_back(temp);
        }

        map<string, int> vertexToIndex;
        vector<string> indexToVertex;

        for (int i = 0; i < V; i++)
        {
            string vertex;
            cout << "Enter vertex " << i << ": ";
            cin >> vertex;
            vertexToIndex[vertex] = i;
            indexToVertex.push_back(vertex);
        }

        int E;
        cout << "Enter number of edges: ";
        cin >> E;
        for (int i = 0; i < E; i++)
        {
            string a, b;
            cout << "Enter (a,b): ";
            cin >> a >> b;
            int index_a = vertexToIndex[a];
            int index_b = vertexToIndex[b];
            g[index_a].push_back(index_b);
            g[index_b].push_back(index_a);
        }

        vector<int> visited(V, 0);
        cout << "DFS: ";
        dfs(g, 0, visited);
        cout << endl;

        cout << "BFS: ";
        bfs(g, 0);
        cout << endl;

        cout << "Do you want to continue (y/n): ";
        cin >> charChoice;

    } while (charChoice == 'y' || charChoice == 'Y');


}
