import pandas as pd
from tensorflow.keras import datasets, layers, models, optimizers

# 1. Load and Preprocess CIFAR-10 Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# 2. Define Hyperparameter Sets
hyper_sets = [
    {
        "name": "Set_1_Baseline",
        "learning_rate": 0.001,
        "filter_size": (3, 3),
        "dropout_rate": 0.2,
        "optimizer": "adam",
    },
    {
        "name": "Set_2_High_Regularization",
        "learning_rate": 0.0005,
        "filter_size": (3, 3),
        "dropout_rate": 0.5,
        "optimizer": "adam",
    },
    {
        "name": "Set_3_Large_Filters_SGD",
        "learning_rate": 0.01,
        "filter_size": (5, 5),
        "dropout_rate": 0.3,
        "optimizer": "sgd",
    },
]


def train_and_evaluate(config):
    print(f"\n>>> Training Model: {config['name']}...")

    model = models.Sequential(
        [
            layers.Conv2D(
                32, config["filter_size"], activation="relu", input_shape=(32, 32, 3)
            ),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, config["filter_size"], activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dropout(config["dropout_rate"]),
            layers.Dense(10, activation="softmax"),
        ]
    )

    # Select Optimizer
    if config["optimizer"] == "adam":
        opt = optimizers.Adam(learning_rate=config["learning_rate"])
    else:
        opt = optimizers.SGD(learning_rate=config["learning_rate"])

    model.compile(
        optimizer=opt, loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )

    # Train for 3 epochs (limited for quick demonstration)
    history = model.fit(
        train_images,
        train_labels,
        epochs=3,
        validation_data=(test_images, test_labels),
        verbose=0,
    )

    # Evaluate
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
    return test_loss, test_acc


# 3. Execute Loop
results = []
for setup in hyper_sets:
    loss, acc = train_and_evaluate(setup)
    results.append(
        {
            "Model Name": setup["name"],
            "Optimizer": setup["optimizer"],
            "LR": setup["learning_rate"],
            "Filter": setup["filter_size"],
            "Test Loss": round(loss, 4),
            "Test Accuracy": round(acc, 4),
        }
    )

# 4. Print Final Comparison Metrics
print("\n" + "=" * 70)
print("FINAL HYPERPARAMETER METRICS COMPARISON")
print("=" * 70)
results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
print("=" * 70)
