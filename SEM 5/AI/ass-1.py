# 1. Implement depth first search algorithm and Breadth First Search algorithm. Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

# DFS
# g = {
#     0:[1,2],
#     1:[0,3,4],
#     2:[0,3],
#     3:[1,2,4],
#     4:[1,3],
# }

def input_graph():
    n = int(input("Enter the number of vertices: "))
    g = {}
    for i in range(n):
        edges = input(f"Enter the neighbors of vertex {i} (space-separated): ").split()
        g[i] = [int(x) for x in edges]
    s = int(input("Enter starting node: "))
    return g, n, s

# DFS
def dfs(g,s,vis):
    vis[s]=1
    print(s, end=" ")
    for c in g[s]:
        if not vis[c]:
            dfs(g,c, vis)

# BFS
def bfs(g,s):
    q=[s]
    vis=[s]
    while q:
        cur=q.pop(0)
        print(cur, end=" ")
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)

def main():
    g, n, s = input_graph()
    vis=[0]*n
    print("BFS: ", end=" ")
    bfs(g,s)
    print()
    print("DFS: ", end=" ")
    dfs(g,s,vis)
    
if __name__ == "__main__":
    main()
