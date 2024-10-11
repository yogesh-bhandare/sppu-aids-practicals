import heapq

# Link State Routing (Dijkstra’s Algorithm)
def dijkstra(graph, start):
    # Priority queue to store (cost, node)
    queue = [(0, start)]
    # Dictionary to store the shortest path to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        # Check neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Distance Vector Routing (Bellman-Ford Algorithm)
def bellman_ford(graph, start):
    # Initialize distances from start to all other nodes as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Relax edges |V| - 1 times (V is the number of vertices)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise Exception("Graph contains a negative-weight cycle")

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node} (Link State Routing - Dijkstra's Algorithm): {distances}")

distances_bf = bellman_ford(graph, start_node)
print(f"Shortest paths from {start_node} (Distance Vector Routing - Bellman-Ford Algorithm): {distances_bf}")
