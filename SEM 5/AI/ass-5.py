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
        countJob = 0
        jobProfit = 0

        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJob += 1
                    jobProfit += jobs[i].profit
                    break

        return countJob, jobProfit
    
if __name__ == "__main__":
    jobs = []
    n = int(input("Ener total Number of jobs: "))
    for i in range(1, n+1):
        d, p = map(int, input(f"Enter Deadline and Profit for {i} job: ").split(" "))
        jobs.append(Job(i, d, p))
    count, profit = Solution().jobsScheduling(jobs)
    print(f"No. of days {count} max profit {profit}")