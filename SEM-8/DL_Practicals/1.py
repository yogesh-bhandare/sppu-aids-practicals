import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\rv401\Downloads\USA_Housing.csv")

print("HEAD \n", df.head())
print("DESCRIBE \n", df.describe())
print("INFO \n", df.info())
X = df[
    [
        "Avg. Area Income",
        "Avg. Area House Age",
        "Avg. Area Number of Rooms",
        "Avg. Area Number of Bedrooms",
        "Area Population",
    ]
]
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²  :", r2_score(y_test, y_pred))
coef_df = pd.DataFrame({"Feature": X.columns, "Coefficient": model.coef_})
print(coef_df)
print("Intercept   :", model.intercept_)
random_input = X_test.iloc[5].values.reshape(1, -1)
actual_price = y_test.iloc[5]

predict_price = model.predict(random_input)

print("Predicted Price", predict_price)
print("Actual Price", actual_price)
print("Random input", random_input)
