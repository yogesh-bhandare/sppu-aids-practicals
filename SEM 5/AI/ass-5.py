# 5. Implement Greedy search algorithm for any of the following application: Selection Sort
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    result = [-1] * n
    job_sequence = ['-1'] * n

    for job in jobs:
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] == -1:
                result[j] = job.job_id
                job_sequence[j] = job.job_id
                break

    total_profit = sum([jobs[i - 1].profit for i in result if i != -1])
    return job_sequence, total_profit

if __name__ == "__main__":
    jobs = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 1, 40),
        Job(4, 1, 30)
    ]
    
    max_deadline = max(job.deadline for job in jobs)

    job_sequence, total_profit = job_scheduling(jobs, max_deadline)
    
    print("Job sequence to maximize profit:", job_sequence)
    print("Total Profit:", total_profit)
