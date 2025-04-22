import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

plt.plot(x, 1 / (1 + np.exp(-x)), label="Sigmoid")
plt.plot(x, np.tanh(x), label="tanh")
plt.plot(x, np.maximum(0, x), label="Relu")
plt.plot(x, x, label="Identity")
plt.plot(x, np.exp(x) / np.sum(np.exp(x)), label="Softmax")

plt.ylabel("Activation")
plt.xlabel("Input")
plt.title("Activation Fucntion")
plt.legend()
plt.grid(True)
plt.show()
