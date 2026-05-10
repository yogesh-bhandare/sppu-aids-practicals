import numpy as np

# Distance Matrix
dist = np.array([[0, 2, 9, 10], [2, 0, 6, 4], [9, 6, 0, 8], [10, 4, 8, 0]])

# Number of cities
n = len(dist)

# Initialize pheromone matrix
pher = np.ones((n, n))

# Parameters
alpha = 1  # Pheromone importance
beta = 2  # Distance importance
evap = 0.5  # Evaporation rate

ants = 5
iters = 20


# Function to calculate route length
def route_len(route):
    total = 0

    for i in range(len(route) - 1):
        total += dist[route[i]][route[i + 1]]

    # Return to starting city
    total += dist[route[-1]][route[0]]

    return total


best_route = None
best_len = float("inf")

# =========================
# Main ACO Loop
# =========================
for iteration in range(iters):
    all_routes = []

    # Each ant builds a route
    for ant in range(ants):
        # Random starting city
        route = [np.random.randint(n)]

        # Build route
        while len(route) < n:
            current = route[-1]
            choices = []

            # Calculate attractiveness
            for j in range(n):
                if j not in route:
                    pheromone = pher[current][j] ** alpha
                    heuristic = (1 / dist[current][j]) ** beta

                    score = pheromone * heuristic

                    choices.append((j, score))

            # Choose city with maximum score
            next_city = max(choices, key=lambda x: x[1])[0]

            route.append(next_city)

        # Store completed route
        all_routes.append(route)

    # =========================
    # Pheromone Evaporation
    # =========================
    pher *= 1 - evap

    # =========================
    # Pheromone Update
    # =========================
    for route in all_routes:
        length = route_len(route)

        # Update best solution
        if length < best_len:
            best_len = length
            best_route = route

        # Deposit pheromone
        for i in range(n - 1):
            a = route[i]
            b = route[i + 1]

            pher[a][b] += 1 / length
            pher[b][a] += 1 / length

        # Return edge pheromone
        pher[route[-1]][route[0]] += 1 / length
        pher[route[0]][route[-1]] += 1 / length

print("\nBest Route:", best_route)
print("Shortest Distance:", best_len)
