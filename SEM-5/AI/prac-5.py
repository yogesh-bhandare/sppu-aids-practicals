class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def jobsScheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = max(job.deadline for job in jobs)

        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobsProfit = 0

        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobsProfit += jobs[i].profit
                    break

        return countJobs, jobsProfit
    
if __name__ == "__main__":
    jobs = []
    n = int(input("Enter total no. of jobs: "))
    for i in range(1, n+1):
        d, p = map(int, input(f"Enter the job deadline and profit for {i}: ").split(" "))
        jobs.append(Job(i, d, p))
    count, profit = Solution().jobsScheduling(jobs)
    print(count, profit)
    