def canColor(g, s, color, colorList, posColors):
    for child in g[s]:
        if colorList[child] == posColors[color]:
            return False
    return True

def graphColouring(g, m, v, s, colorList, posColors):
    if s == v:
        return True
    
    for color in range(m):
        if canColor(g, s, color, colorList, posColors):
            colorList[s] = posColors[color]
            if graphColouring(g, m, v, s+1, colorList, posColors) == True:
                return True
            colorList[s] = -1

if __name__ == "__main__":
    posColors = ["Violet", "Indigo", "Blue", "Yellow", "Green", "Orange", "Red"]
    m = int(input("Enter Total no. of colors to use: "))
    g = {}
    n = int(input("Enter Total number of edges in graph: "))
    for i in range(n):
        a, b = map(int, input().split(" "))
        if g.get(a) == None:
            g[a] = []
        g[a].append(b)
        if g.get(b) == None:
            g[b] = []
        g[b].append(a)
    colorList = {}
    for i in g.keys():
        colorList[i] = -1
    v = len(g.keys())
    if graphColouring(g, m, v, 0, colorList, posColors):
        print(colorList)
    else:
        print(f"Graph Coloring not possible for {m} colors")

"""
3
6
0 1
0 2
0 3
1 2
2 3
3 4
"""