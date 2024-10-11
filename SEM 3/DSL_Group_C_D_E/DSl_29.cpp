//Yogesh Bhandare SE AIDS 22506
//Queues are frequently used in computer programming, and a typical example is the creation
//of a job queue by an operating system.If the operating system does not use priorities, then
//the jobs are processed in the order they enter the system.Write C++ program for simulating
//job queue.Write functions to add job and delete job from queue.

#include<iostream>
using namespace std;

class queue
{
public:
    int size = 10;
    int start = -1;
    int end = -1;
    int arr[10];

    void push(int x)
    {
        if (end == size - 1)
        {
            cout << "Queue Overflow!!" << endl;
        }
        arr[++end] = x;
    }

    int pop()
    {
        if (start == end)
        {
            cout << "Queue Underflow" << endl;
            return -1; // Indicating an underflow condition
        }
        return arr[++start];
    }

    void display()
    {
        if (start == end)
        {
            cout << "Queue is empty" << endl;
        }
        cout << "Queue Contains: ";
        for (int i = start + 1; i <= end; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    void addMultipleJobs(int numJobs)
    {
        for (int i = 0; i < numJobs; ++i)
        {
            int job;
            cout << "Enter job " << i + 1 << ": ";
            cin >> job;
            push(job);
        }
    }
};

int main()
{
    queue q;
    int choice, job, numJobs;

    do
    {
        cout << "\nMenu:" << endl;
        cout << "1. Add a job to the queue" << endl;
        cout << "2. Delete a job from the queue" << endl;
        cout << "3. Display the queue" << endl;
        cout << "4. Add multiple jobs" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter the job to add to the queue: ";
            cin >> job;
            q.push(job);
            break;
        case 2:
            job = q.pop();
            if (job != -1)
            {
                cout << "Job " << job << " deleted from the queue." << endl;
            }
            break;
        case 3:
            q.display();
            break;
        case 4:
            cout << "Enter the number of jobs to add: ";
            cin >> numJobs;
            q.addMultipleJobs(numJobs);
            break;
        case 5:
            cout << "Exiting the program." << endl;
            break;
        default:
            cout << "Invalid choice. Please enter a valid option." << endl;
        }
    } while (choice != 5);

    return 0;
}

