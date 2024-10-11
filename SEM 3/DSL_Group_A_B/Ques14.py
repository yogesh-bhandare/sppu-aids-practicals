# Write a Python program to store first year percentage of students in array. Write function for
# sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.

stud_list=[]
n=int(input("Total Number of students: "))
for i in range(n):
    print()
    marks=int(input(f"Enter marks for Student {i+1}: "))
    stud_list.append(marks)

def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)):
            pass
