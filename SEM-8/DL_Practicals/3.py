import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# 1. Load Dataset
df = pd.read_csv(
    r"C:\Users\rv401\Desktop\DL\IMDB Dataset.csv"
)  # Ensure path is correct

# Convert 'positive'/'negative' labels to 1/0
df["sentiment"] = df["sentiment"].map({"positive": 1, "negative": 0})

# 2. Tokenization and Preprocessing
max_words = 10000
max_len = 200

tokenizer = Tokenizer(num_words=max_words, lower=True)
tokenizer.fit_on_texts(df["review"])

# Convert sentences to sequences of integers
sequences = tokenizer.texts_to_sequences(df["review"])
data = pad_sequences(sequences, maxlen=max_len)
labels = df["sentiment"].values

# Split into Train/Test (80% train, 20% test)
split = int(len(data) * 0.8)
x_train, x_test = data[:split], data[split:]
y_train, y_test = labels[:split], labels[split:]

# 3. Build LSTM Model
model = Sequential(
    [
        Embedding(max_words, 128, input_length=max_len),
        LSTM(64, dropout=0.2),
        Dense(1, activation="sigmoid"),
    ]
)

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# 4. Train (Small epoch for demonstration)
print("Training on Kaggle Dataset...")
model.fit(x_train, y_train, epochs=2, batch_size=64, validation_split=0.1)


# 1. Generate predictions for the entire test set
# model.predict returns probabilities; we convert them to 0 or 1 using a 0.5 threshold
y_pred_probs = model.predict(x_test)
y_pred = (y_pred_probs > 0.5).astype("int32")

# 2. Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# 3. Display the confusion matrix visually
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=["Negative", "Positive"]
)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix: IMDB Sentiment Analysis")
plt.show()

# 4. Print the detailed Classification Report
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))
# 5. RANDOM TEST ENTRY PREDICTION
random_idx = np.random.randint(0, len(df))
random_review_text = df.iloc[random_idx]["review"]
actual_sentiment = "POSITIVE" if df.iloc[random_idx]["sentiment"] == 1 else "NEGATIVE"

# Preprocess the random entry for prediction
sample_seq = tokenizer.texts_to_sequences([random_review_text])
sample_pad = pad_sequences(sample_seq, maxlen=max_len)

# Predict
prediction_score = model.predict(sample_pad)[0][0]
predicted_sentiment = "POSITIVE" if prediction_score > 0.5 else "NEGATIVE"

# Output Result

print("RANDOM REVIEW FROM DATASET:")
print(f"{random_review_text[:300]}...")  # Printing first 300 chars

print(f"ACTUAL SENTIMENT:    {actual_sentiment}")
print(f"PREDICTED SENTIMENT: {predicted_sentiment} ({prediction_score:.4f})")
