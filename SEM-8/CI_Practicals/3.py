import matplotlib.pyplot as plt
import numpy as np


# Fitness function
def fitness(x):
    return x**2


# Parameters
pop_size = 10
generations = 20
clone_factor = 3
mutation_rate = 0.3

# Initialize population
population = np.random.uniform(-10, 10, pop_size)
best_values = []

for _ in range(generations):
    # Evaluate fitness
    fit = fitness(population)

    # Select best 3
    selected = population[np.argsort(fit)[-3:]]

    # Clone
    clones = np.repeat(selected, clone_factor)

    # Mutate
    mutations = clones + np.random.normal(0, 1, len(clones)) * mutation_rate

    # New population = best of all
    population = np.concatenate((population, mutations))
    population = population[np.argsort(fitness(population))[-pop_size:]]
    best_values.append(max(fitness(population)))

print("Best Solution:", max(population))
print("Max Fitness:", max(fitness(population)))

plt.plot(best_values)
plt.title("CSA Convergence")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.show()
