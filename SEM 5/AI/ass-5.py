# 5. Implement Greedy search algorithm for any of the following application: Selection Sort
class Job:
    def __init__(self, id, deadline, profit) -> None:
        self.id = id 
        self.deadline = deadline
        self.profit = profit

def jobScheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    maxi = jobs[0].deadline
    for i in range(1, len(jobs)):
        maxi = max(maxi, jobs[i].deadline)

    slot = [-1] * (maxi+1)
    countJobs = 0
    jobProfit = 0

    for i in range(len(jobs)):
        for j in range(jobs[i].deadline, 0, -1):
            if slot[j] == -1:
                slot[j] = i
                countJobs += 1
                jobProfit += jobs[i].profit
                break

    return countJobs, jobProfit

if __name__ == "__main__":
    jobs = [
        Job(1,4,20),
        Job(2,1,10),
        Job(3,2,40),
        Job(4,2,30)
    ]

    count, profit = jobScheduling(jobs)
    print(count, profit)
