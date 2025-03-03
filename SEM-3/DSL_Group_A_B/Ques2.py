# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by
# N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

marklist=[]
n=int(input("Enter Total Number of students: "))
for students in range(n):
    mark=int(input(f"Enter the marks for roll num {students+1}: "))
    marklist.append(mark)

#Average score claculation
total=0
for marks in marklist:
    total += marks

print(f"Average score of class is: {total/len(marklist)}")

#Calculate max and min
max_val=marklist[0]
min_val=marklist[0]
for marks in marklist:
    if marks<min_val:
        min_val=marks
    if max_val<marks:
        max_val=marks

#Count of absent students
cout=0
for marks in marklist:
    if marks==None:
        cout+=1

