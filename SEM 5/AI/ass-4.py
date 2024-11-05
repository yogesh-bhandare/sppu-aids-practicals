# 4. Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for a graph coloring problem.
m = int(input("Enter the total number of colours: "))

g = {}

n = int(input("Enter the total number of edges in graph g: "))

for i in range(n):
    a, b = map(int, input().split(" "))
    if g.get(a) == None:
        g[a] = []
    g[a].append(b)
    if g.get(b) == None:
        g[b] = []
    g[b].append(a)

print(g)

posCol = ["voilet", "indigo", "blue", "yellow", "green", "orange", "red"]

def canColour(g, n, col, colList):
    for child in g[n]:
        if colList[child] == posCol[col]:
            return False
    
    return True

def graphColouring(g, m, v, n, colList):
    if n == v:
        return True
    
    for col in range(m):
        if canColour(g, n, col, colList):
            colList[n] = posCol[col]
            if graphColouring(g, m, v, n+1, colList) == True:
                return True
            colList[n] = -1

v = len(g.keys())
colList = {}
for i in g.keys():
    colList[i] = -1

if graphColouring(g, m, v, 0, colList):
    print(colList)
else:
    print(f"Can't perform graph coloring on m({m}) colours")


"""
0 1
0 2
0 3
1 2
2 3
3 4
"""