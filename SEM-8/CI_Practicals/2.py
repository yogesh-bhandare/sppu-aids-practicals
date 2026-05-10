import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Load Iris dataset
data = load_iris()
x = data.data
y = data.target


# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# GA settings
pop_size = 20
generations = 30
mutation_rate = 0.1


# Initialize population
def initialize_population():
    population = []
    for _ in range(pop_size):
        hidden_neurons = np.random.randint(5, 50)
        learning_rate = np.random.uniform(0.001, 0.1)
        population.append([hidden_neurons, learning_rate])
    return population


# Fitness function
def fitness(individual):
    hidden, lr = individual
    model = MLPClassifier(
        hidden_layer_sizes=(hidden,),
        learning_rate_init=lr,
        max_iter=300,
        random_state=42,
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    return 1 - accuracy


# Selection
def selection(population):
    sorted_population = sorted(population, key=lambda ind: fitness(ind))
    return sorted_population[: pop_size // 2]


# Crossover
def crossover(parent1, parent2):
    return [
        np.random.choice([parent1[0], parent2[0]]),
        np.random.choice([parent1[1], parent2[1]]),
    ]


# Mutation
def mutate(individual):
    if np.random.rand() < mutation_rate:
        individual[0] = np.random.randint(5, 50)
    if np.random.rand() < mutation_rate:
        individual[1] = np.random.uniform(0.001, 0.1)
    return individual


# GA optimization
population = initialize_population()

for generation in range(generations):
    selected = selection(population)
    new_population = selected.copy()

    while len(new_population) < pop_size:
        idx1, idx2 = np.random.choice(len(selected), 2)
        child = crossover(selected[idx1], selected[idx2])
        child = mutate(child)
        new_population.append(child)

    population = new_population

    best = min(population, key=lambda ind: fitness(ind))
    print(f"Generation {generation + 1}, Best Accuracy: {1 - fitness(best)}")

# Best individual
best_individual = min(population, key=lambda ind: fitness(ind))

print("\nOptimal Hidden Neurons:", best_individual[0])
print("Optimal Learning Rate:", best_individual[1])

# Final model
final_model = MLPClassifier(
    hidden_layer_sizes=(best_individual[0],),
    learning_rate_init=best_individual[1],
    max_iter=500,
    random_state=42,
)

final_model.fit(x_train, y_train)
final_predictions = final_model.predict(x_test)

print("\nFinal Accuracy:", accuracy_score(y_test, final_predictions))
