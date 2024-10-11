# a) Write a Python program to store roll numbers of student in array who attended training
# program in random order. Write function for searching whether particular student
# attended training program or not, using Linear search and Sentinel search

stud_list=[]
n=int(input("Total Number of students: "))
for i in range(n):
    print()
    marks=int(input(f"Enter marks for Student {i+1}: "))
    stud_list.append(marks)
key=int(input("Enter Key to search in list: "))

def linear_search(list,key):
    for i in range(len(stud_list)):
        if stud_list[i]==key:
            return i
    return -1

res_linear=linear_search(stud_list,key)
if res_linear==-1:
    print("(Linear Search) Student is not present.")
else:
    print("(Linear Search) Student is present at index: ",res_linear)
