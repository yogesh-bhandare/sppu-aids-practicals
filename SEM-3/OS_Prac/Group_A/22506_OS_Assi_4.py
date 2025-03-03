class BankersAlgorithm:
    def __init__(self, processes, resources, allocation, max_claim):
        self.processes = processes
        self.resources = resources
        self.allocation = allocation
        self.max_claim = max_claim
        self.available = [resources[j] - sum(allocation[i][j] for i in range(processes)) for j in range(resources)]

    def is_safe(self, process, request):
        # Check if the request is within the max claim for the process
        if any(request[i] > self.max_claim[process][i] for i in range(self.resources)):
            return False

        # Check if the request can be satisfied with the available resources
        if any(request[i] > self.available[i] for i in range(self.resources)):
            return False

        # Simulate resource allocation to check for safety
        temp_allocation = [self.allocation[i][:] for i in range(self.processes)]
        temp_available = self.available[:]

        for i in range(self.resources):
            temp_allocation[process][i] += request[i]
            temp_available[i] -= request[i]

        # Check if the resulting state is safe
        safe_sequence = []
        finish = [False] * self.processes

        for _ in range(self.processes):
            for i in range(self.processes):
                if not finish[i]:
                    if all(temp_available[j] >= self.max_claim[i][j] - temp_allocation[i][j] for j in range(self.resources)):
                        # Resources can be allocated to process i
                        for j in range(self.resources):
                            temp_available[j] += temp_allocation[i][j]
                        safe_sequence.append(i)
                        finish[i] = True

        # If all processes can be finished, the request is safe
        return all(finish)

    def request_resources(self, process, request):
        if not self.is_safe(process, request):
            print("Unsafe request. Process must wait.")
            return

        # Grant the request and update the available resources
        for i in range(self.resources):
            self.allocation[process][i] += request[i]
            self.available[i] -= request[i]

        print("Request granted. New allocation matrix:")
        self.print_allocation_matrix()

    def print_allocation_matrix(self):
        print("Allocation Matrix:")
        for i in range(self.processes):
            print(self.allocation[i])

    def print_max_claim_matrix(self):
        print("Max Claim Matrix:")
        for i in range(self.processes):
            print(self.max_claim[i])

    def print_available_resources(self):
        print("Available Resources:")
        print(self.available)


# Example usage:
if __name__ == "__main__":
    processes = 5
    resources = 3

    allocation_matrix = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]

    max_claim_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]

    available_resources = [3, 3, 2]

    banker = BankersAlgorithm(processes, resources, allocation_matrix, max_claim_matrix)

    banker.print_allocation_matrix()
    banker.print_max_claim_matrix()
    banker.print_available_resources()

    process_to_request = 1
    request_resources = [1, 0, 2]

    banker.request_resources(process_to_request, request_resources)
