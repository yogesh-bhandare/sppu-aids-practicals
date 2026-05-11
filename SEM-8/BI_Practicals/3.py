import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("studentP.csv")
df.head()
df.info()
df.describe()

df = df.dropna()
df = df.drop_duplicates()
df.columns = df.columns.str.strip()

df.to_csv("clean_data.csv", index=False)

plt.figure(figsize=(12, 10))

# plot 1: final grade distribution
plt.subplot(2, 2, 1)
plt.hist(df["G3"], bins=10, color="skyblue", edgecolor="black")
plt.title("Final Grade Distribution")
plt.xlabel("Grade (G3)")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)

# plot 2: age distribution
plt.subplot(2, 2, 2)
plt.hist(df["age"], bins=10, color="lightcoral", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)

# plot 3: study time vs final grade
plt.subplot(2, 2, 3)
plt.scatter(df["studytime"], df["G3"], alpha=0.6, color="green")
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time (hours)")
plt.ylabel("Final Grade (G3)")
plt.grid(alpha=0.3)

# plot 4: absences vs final grade
plt.subplot(2, 2, 4)
plt.scatter(df["absences"], df["G3"], alpha=0.6, color="orange")
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
