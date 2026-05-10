import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from tensorflow.keras.layers import Dense, Embedding, SimpleRNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# 1. Load Local Dataset
df = pd.read_csv("IMDB Dataset.csv")
df["sentiment_val"] = df["sentiment"].map({"positive": 1, "negative": 0})

# 2. Tokenization & Preprocessing
max_words, max_len = 5000, 100
tokenizer = Tokenizer(num_words=max_words, lower=True)
tokenizer.fit_on_texts(df["review"])

X = pad_sequences(tokenizer.texts_to_sequences(df["review"]), maxlen=max_len)
Y = df["sentiment_val"].values

# 3. Build & Train RNN (Lightweight for speed)
model = Sequential(
    [
        Embedding(max_words, 32, input_length=max_len),
        SimpleRNN(32, dropout=0.2),
        Dense(1, activation="sigmoid"),
    ]
)
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X[:1500], Y[:1500], epochs=1, batch_size=32, verbose=0)  # Hidden training

# 4. Select Graph Nodes
num_nodes = 12
indices = np.random.choice(len(df), num_nodes, replace=False)
node_X = X[indices]
node_texts = df.iloc[indices]["review"].values
node_actuals = df.iloc[indices]["sentiment"].values

# 5. Predict Sentiment
preds = model.predict(node_X)
pred_labels = [1 if p > 0.5 else 0 for p in preds]

# 6. Build and Visualize Graph
G = nx.Graph()
for i in range(num_nodes):
    G.add_node(i)
for i in range(num_nodes - 1):
    G.add_edge(i, i + 1)

colors = ["#2ecc71" if s == 1 else "#e74c3c" for s in pred_labels]
plt.figure(figsize=(8, 5))
nx.draw(G, nx.spring_layout(G), with_labels=True, node_color=colors, node_size=800)
plt.title("Sentiment Network (Green=Pos, Red=Neg)")
plt.show()

# 7. PRINT VERIFICATION TABLE
print("\n" + "=" * 90)
print(
    f"{'NODE ID':<8} | {'ACTUAL (CSV)':<12} | {'RNN PREDICTION':<15} | {'TEXT PREVIEW'}"
)
print("-" * 90)

for i in range(num_nodes):
    p_text = "Positive" if pred_labels[i] == 1 else "Negative"
    # Clean the review text for display
    clean_text = node_texts[i][:65].replace("\n", " ") + "..."

    # Mark if the prediction was WRONG
    status = "✓" if p_text == node_actuals[i].capitalize() else "✗ WRONG"

    print(
        f"Node {i:<3}   | {node_actuals[i].capitalize():<12} | {p_text:<15} | {clean_text} ({status})"
    )
