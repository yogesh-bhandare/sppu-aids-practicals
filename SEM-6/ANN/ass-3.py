# 3. Write a Python Program using Perceptron Neural Network to recognise even and odd numbers. Given numbers are in ASCII form 0 to 9
import numpy as np

j = int(input("Enter a Number (0-9): "))

training_data = [
    {"input": [int(b) for b in f"{n:06b}"], "label": 1 if n % 2 == 0 else 0}
    for n in range(10)
]

weights = np.zeros(6)

for data in training_data:
    x = np.array(data["input"])
    y = data["label"]
    pred = 1 if np.dot(x, weights) >= 0 else 0
    weights += (y - pred) * x

x = np.array([int(b) for b in f"{j:06b}"])
pred = 1 if np.dot(x, weights) >= 0 else 0
print(j, "is", "even" if pred == 1 else "odd")
