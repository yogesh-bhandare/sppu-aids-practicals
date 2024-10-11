# Write a Python program to compute following computation on matrix:
# a) Addition of two matrices B) Subtraction of two matrices
# c) Multiplication of two matrices d) Transpose of a matrix

row=int(input("Enter number of rows: "))
col=int(input("Enter number of cols: "))

m1=[[0 for i in range(col)] for i in range(row)]
m2=[[0 for i in range(col)] for i in range(row)]
ans=[[0 for i in range(col)] for i in range(row)]

for n in range(2):
    print(f"\nEnter data for matrix {n+1}: ")
    if n==0:
        matrix=m1
    else:
        matrix=m2
    for m in range(row):
        for n in range(col):
            matrix[m][n]=int(input(f"Enter element at row {m} col {n}: "))


#Addition
for m in range(row):
    for n in range(col):
        ans[m][n]=m1[m][n]+m2[m][n]
#Substaction
for m in range(row):
    for n in range(col):
        ans[m][n]=m1[m][n]-m2[m][n]
#Multiplication
for m in range(row):
    for n in range(col):
        ans[m][n]=m1[m][n]+m2[m][n]
#Transpose
def transpose(m,r,c):
    ans=[[0 for i in range(r)]for j in range(c)]
    for i in range(r):
        for j in range(c):
            ans[i][j] = m[j][i]
    return ans

print("Transpose: ",transpose(m1,row,col))

print("Adition of matrix: ",ans)