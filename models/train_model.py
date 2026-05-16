import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Locate dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_path = os.path.join(project_root, "data", "big_environment_data.csv")

print("Loading dataset...")
df = pd.read_csv(data_path)

X = df[["Temperature", "Rainfall", "Humidity", "WindSpeed"]]
y = df["AQI"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", round(mae, 3))
print("RMSE:", round(rmse, 3))
print("R² Score:", round(r2, 4))

model_path = os.path.join(project_root, "models", "best_aqi_model.pkl")
joblib.dump(model, model_path)

print("\nModel saved successfully.")