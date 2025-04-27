# Group A-1: Write a Python program to plot a few activation functions that are being used in neural networks.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.plot(x, 1 / (1 + np.exp(-x)), label="Sigmoid")
plt.plot(x, (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)), label="tanh")
plt.plot(x, np.where(x > 0, x, 0), label="ReLU")
plt.plot(x, x, label="Identity")
plt.plot(x, np.where(x < 0, 0.01 * x, x), label="Leaky ReLU")

plt.xlabel("Input")
plt.ylabel("Activation")
plt.title("Activation Functions")
plt.legend()
plt.grid(True)
plt.show()
