# n second year computer engineering class, group A student’s play cricket, group B students
# play badminton and group C students play football.
# Write a Python program using functions to compute following: -
# a) List of students who play both cricket and badminton
# b) List of students who play either cricket or badminton but not both
# c) Number of students who play neither cricket nor badminton
# d) Number of students who play cricket and football but not badminton.
# (Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-
# in functions)

def intersection(l1,l2):
    res=[]
    for student in l1:
        if student in l2:
            res.append(student)
    return res

def union(l1,l2):
    res=l2.copy()
    for student in l1:
        if student not in l2:
            res.append(student)
    return res

def diffrence(l1,l2):
    res=[]
    for student in l1:
        if student not in l2:
            res.append(student)
    return res



a=[1,2,3,4,5,6,7]
b=[2,3,6,7,9,10]
c=[2,4,6,8,10,12]

print(intersection(a,b))
print(union(a,b))
u=union(a,b)
i=intersection(a,b)
print(diffrence(u,i))
x=diffrence(c,b)
print(diffrence(x,a))
y=union(a,c)
print(diffrence(y,b))
