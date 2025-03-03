def canColor(g, s, color, colorList, posColors):
    for child in g[s]:
        if colorList[child] == posColors[color]:
            return False
    return True

def graphColouring(g, m, v, s, colorList, posColors):
    if v == s:
        return True
    
    for color in range(m):
        if canColor(g, s, color, colorList, posColors):
            colorList[s] = posColors[color]
            if graphColouring(g, m, v, s+1, colorList, posColors):
                return True
            colorList[s] = -1

if __name__ == "__main__":
    g = {}
    posColors = ["Violet", "Indigo", "Blue", "Yellow", "Green", "Orange", "Red"]
    m = int(input("Enter total number of colors to use: "))
    n = int(input("Enter total number of edges in graph: "))
    for i in range(n):
        a, b = map(int, input().split(" "))
        if g.get(a) == None:
            g[a] = []
        g[a].append(b)
        if g.get(b) == None:
            g[b] = []
        g[b].append(a)

    v = len(g)
    s = int(input("Enter Start Vertex: "))
    colorList = {}
    for i in range(v):
        colorList[i] = -1
    
    if graphColouring(g, m, v, s, colorList, posColors):
        print(colorList)
    else:
        print(f"Entered number of colors does not satisfy graph coloring")

"""
3
6
0 1
0 2
0 3
1 2
2 3
3 4
0
"""