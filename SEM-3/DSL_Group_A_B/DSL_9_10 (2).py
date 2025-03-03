# MATRIX OPERATIONS

# Function to input a matrix
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter the element at row {i + 1} and column {j + 1}: ")))
        matrix.append(row)
    return matrix



# Function to display a matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)


# Function for matrix addition
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrix addition is not possible. Matrix dimensions are different.")
        return None
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result


# Function for matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrix subtraction is not possible. Matrix dimensions are different.")
        return None
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result


# Function for matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print(
            "Matrix multiplication is not possible. Number of columns in the first matrix should match the number of rows in the second matrix.")
        return None
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


# Function to transpose a matrix
def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed


# SPARSE MATRIX

# Function to find non-zero elements and their indices
def non_zero(matrix):
    non_zero_elements = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                non_zero_elements.append([matrix[i][j], (i, j)])
    return non_zero_elements


# Function to check if the matrix is sparse
def is_sparse(matrix):
    threshold = 1 / 3 * (len(matrix) * len(matrix[0]))
    return len(non_zero(matrix)) <= threshold


def fast_transpose(matrix):
    if not matrix:
        return []

    num_rows, num_cols = len(matrix), len(matrix[0])

    # Create a list of empty lists to represent the transposed matrix
    transposed = [[] for _ in range(num_cols)]

    # Fill the transposed matrix with values
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i] and j < len(matrix[i]):
                transposed[j].append(matrix[i][j])
            else:
                transposed[j].append(0)

    return transposed


# Function for sparse matrix addition
def sparse_matrix_addition(matrix1, matrix2):
    # Ensure that the dimensions match
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Sparse matrix addition is not possible. Matrix dimensions are different.")
        return None

    # Create a matrix to store the result
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Iterate through the rows and columns
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            # Calculate the sum of corresponding elements from both matrices
            value1 = matrix1[i][j]
            value2 = matrix2[i][j]
            result[i][j] = value1 + value2

    return result

# Create and initialize the sparse matrices
sparse_matrix1 = []
sparse_matrix2 = []

# Taking inputs for the matrix
row1 = int(input("Enter the number of rows for the first matrix: "))
col1 = int(input("Enter the number of columns for the first matrix: "))
matrixA = input_matrix(row1, col1)

row2 = int(input("Enter the number of rows for the second matrix: "))
col2 = int(input("Enter the number of columns for the second matrix: "))
matrixB = input_matrix(row2, col2)

# Input sparse matrices (each element as [value, (row, column)])
num_rows = int(input("Enter the number of rows for the first sparse matrix: "))
num_cols = int(input("Enter the number of columns for the first sparse matrix: "))
num_elements = int(input("Enter the number of non-zero elements for the first sparse matrix: "))

print("Input elements for the first sparse matrix (value, row, column):")
for _ in range(num_elements):
    value = int(input("Enter the value: "))
    row = int(input("Enter the row: "))
    col = int(input("Enter the column: "))
    sparse_matrix1.append((value, (row, col)))

num_rows = int(input("Enter the number of rows for the second sparse matrix: "))
num_cols = int(input("Enter the number of columns for the second sparse matrix: "))
num_elements = int(input("Enter the number of non-zero elements for the second sparse matrix: "))

print("Input elements for the second sparse matrix (value, row, column):")
for _ in range(num_elements):
    value = int(input("Enter the value: "))
    row = int(input("Enter the row: "))
    col = int(input("Enter the column: "))
    sparse_matrix2.append((value, (row, col)))

# Display the first sparse matrix
print("Sparse Matrix 1:")
for row in sparse_matrix1:
    print(row)

# Display the second sparse matrix
print("Sparse Matrix 2:")
for row in sparse_matrix2:
    print(row)

print("Matrix A:")
display_matrix(matrixA)
print("Matrix B:")
display_matrix(matrixB)

while True:
    print("MENU:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Transpose of Matrix B")
    print("6. Check if Matrix A is Sparse")
    print("7. Check if Matrix B is Sparse")
    print("8. Sparse Matrix Addition")
    print("9. Fast Transpose of Sparse Matrix 1")
    print("10. Fast Transpose of Sparse Matrix 2")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = matrix_addition(matrixA, matrixB)
        if result:
            print("Matrix Addition Result:")
            display_matrix(result)

    elif choice == 2:
        result = matrix_subtraction(matrixA, matrixB)
        if result:
            print("Matrix Subtraction Result (A - B):")
            display_matrix(result)
        result = matrix_subtraction(matrixB, matrixA)
        if result:
            print("Matrix Subtraction Result (B - A):")
            display_matrix(result)

    elif choice == 3:
        result = matrix_multiplication(matrixA, matrixB)
        if result:
            print("Matrix Multiplication Result:")
            display_matrix(result)

    elif choice == 4:
        print("Transpose of Matrix A:")
        display_matrix(transpose_matrix(matrixA))

    elif choice == 5:
        print("Transpose of Matrix B:")
        display_matrix(transpose_matrix(matrixB))

    elif choice == 6:
        if is_sparse(matrixA):
            print("Matrix A is a Sparse Matrix.")
        else:
            print("Matrix A is not a Sparse Matrix.")

    elif choice == 7:
        if is_sparse(matrixB):
            print("Matrix B is a Sparse Matrix.")
        else:
            print("Matrix B is not a Sparse Matrix.")

    elif choice == 8:
        result = sparse_matrix_addition(sparse_matrix1, sparse_matrix2)
        if result:
            print("Sparse Matrix Addition Result:")
            for row in result:
                print([row])

    elif choice == 9:
        result = fast_transpose(sparse_matrix1)
        print("Fast Transpose of Sparse Matrix 1:")
        for row in result:
            print(row)

    elif choice == 10:
        result = fast_transpose(sparse_matrix2)
        print("Fast Transpose of Sparse Matrix 2:")
        for row in result:
            print(row)

    elif choice == 11:
        break
