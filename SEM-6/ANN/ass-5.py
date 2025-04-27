# Group A-5: Write a python Program for Bidirectional Associative Memory with two pairs of vectors.
import numpy as np

# Define vectors and weight matrix
X = np.array([[1, 1, -1, -1], [-1, 1, -1, 1]])
Y = np.array([[1, -1], [-1, 1]])
W = np.dot(Y.T, X)


# BAM functions
def recall_x(y):
    return np.sign(np.dot(W.T, y))


def recall_y(x):
    return np.sign(np.dot(W, x))


# Bidirectional recall
def bam(vector, is_x=True, max_iter=5):
    if is_x:
        x = vector
        for _ in range(max_iter):
            y = recall_y(x)
            new_x = recall_x(y)
            if np.array_equal(new_x, x):
                break
            x = new_x
        return x, y
    else:
        y = vector
        for _ in range(max_iter):
            x = recall_x(y)
            new_y = recall_y(x)
            if np.array_equal(new_y, y):
                break
            y = new_y
        return x, y


# Test
x_test = np.array([1, -1, -1, -1])
x_recalled, y_recalled = bam(x_test)
print("Input x:", x_test)
print("Recalled x:", x_recalled)
print("Recalled y:", y_recalled)
