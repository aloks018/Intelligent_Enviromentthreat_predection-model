import pandas as pd
import numpy as np
import os

def generate_big_data(rows=1000000):

    np.random.seed(42)

    # Realistic feature distributions
    temperature = np.random.normal(35, 4, rows)
    rainfall = np.random.normal(50, 15, rows)

    # Create correlation (important for good R²)
    humidity = 0.6 * rainfall + np.random.normal(20, 3, rows)

    wind_speed = np.random.uniform(2, 15, rows)

    # Strong deterministic AQI formula (clear signal)
    aqi = (
        2.0 * temperature
        - 1.5 * rainfall
        + 2.2 * humidity
        - 1.0 * wind_speed
        + 0.05 * temperature * humidity
        - 0.02 * rainfall * wind_speed
        + np.random.normal(0, 1.0, rows)   # Very small noise
    )

    df = pd.DataFrame({
        "Temperature": temperature,
        "Rainfall": rainfall,
        "Humidity": humidity,
        "WindSpeed": wind_speed,
        "AQI": aqi
    })

    return df


if __name__ == "__main__":

    df = generate_big_data()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    data_folder = os.path.join(project_root, "data")
    os.makedirs(data_folder, exist_ok=True)

    file_path = os.path.join(data_folder, "big_environment_data.csv")

    df.to_csv(file_path, index=False)

    print("Big dataset generated successfully.")
    print("Saved at:", file_path)