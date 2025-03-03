def dfs(g, s, vis):
    vis[s] = 1
    print(s, end=" ")
    for c in g[s]:
        if not vis[c]:
            dfs(g, c, vis)

def bfs(g, q, vis):
    if not q:
        return
    
    cur = q.pop(0)
    print(cur, end=" ")
    for c in g[cur]:
        if c not in vis:
            q.append(c)
            vis.append(c)

    bfs(g, q, vis)

if __name__ == "__main__":
    g = {}
    n = int(input("Enter total no. of edges: "))
    for i in range(n):
        a, b = map(int, input().split(" "))
        if g.get(a) == None:
            g[a] = []
        g[a].append(b)
        if g.get(b) == None:
            g[b] = []
        g[b].append(a)

    start = 0
    vis = [0] * len(g)
    vist = [start]
    q = [start]
    dfs(g, start, vis)
    print()
    bfs(g, q, vist)
