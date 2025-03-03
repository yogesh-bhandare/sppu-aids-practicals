# Implement A star (A*) Algorithm for any game search problem.
import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other):
        return (self.depth + self.cost) < (other.depth + other.cost)

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))

def find_blank(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

def is_valid(row, col):
    return 0 <= row < 3 and 0 <= col < 3

def generate_moves(row, col):
    moves = []
    if is_valid(row-1, col):
        moves.append((-1, 0, "UP"))
    if is_valid(row+1, col):
        moves.append((1, 0, "DOWN"))
    if is_valid(row, col-1):
        moves.append((0, -1, "LEFT"))
    if is_valid(row, col+1):
        moves.append((0, 1, "RIGHT"))
    return moves

def apply_move(state, row, col, move):
    new_state = [row[:] for row in state]
    dr, dc, _ = move
    new_state[row][col], new_state[row+dr][col+dc] = new_state[row+dr][col+dc], new_state[row][col]
    return new_state

def heuristic(state, target):
    count = 0
    for row in range(3):
        for col in range(3):
            if state[row][col] != target[row][col]:
                count += 1
    return count

def a_star_search(initial_state, target_state):
    open_list = []
    closed_set = set()
    
    initial_node = PuzzleNode(initial_state, cost=heuristic(initial_state, target_state))
    heapq.heappush(open_list, initial_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(tuple(map(tuple, current_node.state))) 
        
        if current_node.state == target_state:
            moves = []
            while current_node.parent:
                moves.append(current_node.move)
                current_node = current_node.parent
            return moves[::-1]
        
        blank_row, blank_col = find_blank(current_node.state)
        possible_moves = generate_moves(blank_row, blank_col)
        
        for dr, dc, move in possible_moves:
            new_state = apply_move(current_node.state, blank_row, blank_col, (dr, dc, move))
            
            if tuple(map(tuple, new_state)) not in closed_set:
                new_node = PuzzleNode(new_state, parent=current_node, move=move, depth=current_node.depth+1, cost=heuristic(new_state, target_state))
                heapq.heappush(open_list, new_node)
    
    return None

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    print("Initial state:")
    print_puzzle(initial_state)
    
    print("\nTarget state:")
    print_puzzle(target_state)
    
    print("\nSolving...")
    solution = a_star_search(initial_state, target_state)
    
    if solution is None:
        print("\nNo solution found!")
    else:
        print("\nSolution:")
        for step, move in enumerate(solution, start=1):
            print(f"Step {step}: {move}")
            