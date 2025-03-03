#Yogesh Bhandare SE AIDS 22506
# Given the list of processes, their CPU burst times. Display/print the Gantt chart for FCFS , SJF
# , Priority and Round Robin scheduling algorithm. Compute and print the average waiting time
# and average turnaround time

class Process:
    def __init__(self, process_id, burst_time, priority):
        self.process_id = process_id
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

def print_gantt_chart(order):
    gantt_chart = "|"
    for process_id in order:
        gantt_chart += f" P{process_id} |"
    print("Gantt Chart:")
    print(gantt_chart)

def calculate_average_waiting_time(processes):
    return sum(process.waiting_time for process in processes) / len(processes)

def calculate_average_turnaround_time(processes):
    return sum(process.turnaround_time for process in processes) / len(processes)

def fcfs_scheduling(processes):
    order = [process.process_id for process in processes]
    return order

def sjf_scheduling(processes):
    order = [process.process_id for process in sorted(processes, key=lambda x: x.burst_time)]
    return order

def priority_scheduling(processes):
    order = [process.process_id for process in sorted(processes, key=lambda x: x.priority)]
    return order

def round_robin_scheduling(processes, time_quantum):
    order = []
    queue = processes.copy()
    while queue:
        process = queue.pop(0)
        order.append(process.process_id)
        if process.burst_time > time_quantum:
            process.waiting_time += time_quantum
            process.burst_time -= time_quantum
            queue.append(process)
        else:
            process.turnaround_time = sum(process.burst_time for process in processes[:process.process_id])
            process.burst_time = 0
    return order

def main():
    processes = [
        Process(1, 10, 2),
        Process(2, 6, 1),
        Process(3, 8, 4),
        Process(4, 7, 3),
    ]

    time_quantum = 2

    print("FCFS Scheduling:")
    fcfs_order = fcfs_scheduling(processes)
    print_gantt_chart(fcfs_order)
    print("Average Waiting Time:", calculate_average_waiting_time(processes))
    print("Average Turnaround Time:", calculate_average_turnaround_time(processes))

    print("\nSJF Scheduling:")
    sjf_order = sjf_scheduling(processes)
    print_gantt_chart(sjf_order)
    print("Average Waiting Time:", calculate_average_waiting_time(processes))
    print("Average Turnaround Time:", calculate_average_turnaround_time(processes))

    print("\nPriority Scheduling:")
    priority_order = priority_scheduling(processes)
    print_gantt_chart(priority_order)
    print("Average Waiting Time:", calculate_average_waiting_time(processes))
    print("Average Turnaround Time:", calculate_average_turnaround_time(processes))

    print("\nRound Robin Scheduling:")
    rr_order = round_robin_scheduling(processes, time_quantum)
    print_gantt_chart(rr_order)
    print("Average Waiting Time:", calculate_average_waiting_time(processes))
    print("Average Turnaround Time:", calculate_average_turnaround_time(processes))

if __name__ == "__main__":
    main()
