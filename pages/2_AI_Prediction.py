import os
import sys
from pathlib import Path

import joblib
import numpy as np
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from natgeo_theme import (
    inject_natgeo_theme,
    render_footer,
    render_hero,
    render_metric_card,
    render_panel,
    render_section,
    render_text_card,
    render_topbar,
)


st.set_page_config(page_title="AQI Prediction | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Predict AQI")

render_hero(
    title="Air Quality Prediction",
    summary=(
        "Estimate AQI from temperature, rainfall, humidity, and wind speed, then turn "
        "the result into a clear risk message for environmental action."
    ),
    image="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=2400&q=90",
    kicker="AI prediction",
    meta="Model driven AQI estimate",
)

render_section(
    "Enter environmental parameters",
    "Input",
    "Adjust the four values below and run the model to generate a live air-quality estimate.",
)


@st.cache_resource
def load_model():
    model_path = ROOT_DIR / "models" / "best_aqi_model.pkl"
    if not model_path.exists():
        return None, f"Model file not found: {model_path}"
    try:
        return joblib.load(model_path), ""
    except Exception as exc:
        return None, f"Error loading model: {exc}"


model, model_error = load_model()

left, right = st.columns([1, 1], gap="large")
with left:
    temperature = st.slider("Temperature (C)", 20.0, 50.0, 35.0)
    rainfall = st.slider("Rainfall (mm)", 0.0, 150.0, 50.0)
with right:
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 60.0)
    wind_speed = st.slider("Wind speed (km/h)", 1.0, 25.0, 8.0)

render_panel(
    "Prediction guide",
    "Lower AQI suggests cleaner air. Higher AQI indicates pollution stress and stronger need for precautions.",
)

if st.button("Predict AQI"):
    if model is None:
        st.warning(model_error)
    else:
        try:
            input_data = np.array([[temperature, rainfall, humidity, wind_speed]])
            prediction = float(model.predict(input_data)[0])
            risk_score = min(max(prediction / 300, 0), 1)

            render_section("Prediction result", "Output", "The model result is shown with a simple risk interpretation.")
            result_cols = st.columns(3)
            with result_cols[0]:
                render_metric_card("Predicted AQI", f"{prediction:.2f}")
            with result_cols[1]:
                st.progress(risk_score)
                st.caption("Relative pollution pressure")
            with result_cols[2]:
                if prediction < 100:
                    st.success("Air quality status: Good")
                elif prediction < 200:
                    st.warning("Air quality status: Moderate")
                else:
                    st.error("Air quality status: Unhealthy")

            insight_cols = st.columns(2)
            with insight_cols[0]:
                render_text_card(
                    "Model input",
                    f"Temperature {temperature:.1f} C, rainfall {rainfall:.1f} mm, humidity {humidity:.1f}%, wind {wind_speed:.1f} km/h.",
                    "Features",
                )
            with insight_cols[1]:
                render_text_card(
                    "Recommended next step",
                    "Open the Map page to connect the prediction with local location context and risk reporting.",
                    "Action",
                )
        except Exception as exc:
            st.error(f"Prediction error: {exc}")

render_footer()
