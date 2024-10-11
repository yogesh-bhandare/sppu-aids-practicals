# 4. Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for a graph coloring problem.
def is_safe(graph, vertex, color, colors_assigned):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors_assigned[i] == color:
            return False
    return True

def graph_coloring(graph, num_colors, colors_assigned, vertex):
    if vertex == len(graph):
        return True

    for color in range(1, num_colors + 1):
        if is_safe(graph, vertex, color, colors_assigned):
            colors_assigned[vertex] = color  
            if graph_coloring(graph, num_colors, colors_assigned, vertex + 1):
                return True
            colors_assigned[vertex] = 0

    return False  

def solve_graph_coloring(graph, num_colors=3):
    colors_assigned = [0] * len(graph)

    if graph_coloring(graph, num_colors, colors_assigned, 0):
        return colors_assigned
    else:
        return "No solution exists."

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    result = solve_graph_coloring(graph, 3)
    
    color_map = {1: "Red", 2: "Green", 3: "Blue"}
    
    if isinstance(result, list):
        print("Solution found:")
        for vertex, color in enumerate(result):
            print(f"Vertex {vertex + 1} -> {color_map[color]}")
    else:
        print(result)
