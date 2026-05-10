import itertools
import random

servers = ["Server1", "Server2", "Server3"]
server_loads = {s: 0 for s in servers}
rr_cycle = itertools.cycle(servers)
# Uses the same servers list; weights are by position.
weights = [3, 2, 1]
weighted_rr_cycle = itertools.cycle(
    [server for server, weight in zip(servers, weights) for _ in range(weight)]
)


# Round Robin
def round_robin():
    return next(rr_cycle)


# Random
def random_lb():
    return random.choice(servers)


# Least Connections
def least_connections():
    return min(server_loads, key=server_loads.get)


# Weighted Round Robin
def weighted_round_robin():
    return next(weighted_rr_cycle)


def handle_request(client_id, algorithm="round_robin"):
    if algorithm == "round_robin":
        server = round_robin()
    elif algorithm == "weighted_round_robin":
        server = weighted_round_robin()
    elif algorithm == "random":
        server = random_lb()
    elif algorithm == "least_connections":
        server = least_connections()
    server_loads[server] += 1
    print(f"Client {client_id} -> {server} (Load: {server_loads[server]})")


print("=== Round Robin ===")
for i in range(1, 7):
    handle_request(i, "round_robin")

server_loads = {s: 0 for s in servers}
print("\n=== Least Connections ===")
for i in range(1, 7):
    handle_request(i, "least_connections")

server_loads = {s: 0 for s in servers}
print("\n=== Random ===")
for i in range(1, 7):
    handle_request(i, "random")

server_loads = {s: 0 for s in servers}
print("\n=== Weighted Round Robin ===")
for i in range(1, 13):
    handle_request(i, "weighted_round_robin")
