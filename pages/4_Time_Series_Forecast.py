import sys
from pathlib import Path

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
    render_topbar,
)


st.set_page_config(page_title="Forecast | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Forecast")

render_hero(
    title="Rainfall and Climate Forecast",
    summary=(
        "Generate a short city-level weather outlook with temperature, humidity, wind, "
        "rainfall, and a five-day forecast for environmental monitoring."
    ),
    image="https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=2400&q=90",
    kicker="Climate monitoring",
    meta="5-day forecast",
)

render_section(
    "Select a city",
    "Input",
    "Choose a country and city to generate current weather conditions and a five-day rainfall outlook.",
)

locations = {
    "India": ["Delhi", "Mumbai", "Kolkata", "Chennai", "Lucknow"],
    "United States": ["New York", "Los Angeles", "Chicago", "Houston"],
    "United Kingdom": ["London", "Manchester", "Birmingham"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"],
    "UAE": ["Dubai", "Abu Dhabi"],
}

city_climate = {
    "Delhi": [32, 40], "Mumbai": [30, 80], "Kolkata": [31, 70],
    "Chennai": [33, 65], "Lucknow": [34, 50],
    "New York": [25, 60], "Los Angeles": [27, 20],
    "Chicago": [23, 45], "Houston": [29, 75],
    "London": [22, 65], "Manchester": [21, 70],
    "Birmingham": [22, 60], "Tokyo": [28, 70],
    "Osaka": [29, 65], "Kyoto": [27, 60],
    "Sydney": [24, 55], "Melbourne": [23, 50],
    "Brisbane": [26, 60], "Dubai": [38, 5], "Abu Dhabi": [37, 4],
}

col1, col2 = st.columns(2)
with col1:
    country = st.selectbox("Country", list(locations.keys()))
with col2:
    city = st.selectbox("City", locations[country])

render_panel(
    "Forecast note",
    "This module uses simulated city climate baselines for demonstration and a consistent dashboard presentation.",
)

if st.button("Generate Rainfall Report"):
    base_temp, base_rain = city_climate[city]
    temperature = round(base_temp + np.random.normal(0, 1), 1)
    humidity = int(np.random.uniform(40, 80))
    wind = round(np.random.uniform(1, 6), 1)
    rainfall = round(base_rain * np.random.uniform(0.01, 0.05), 2)

    render_section(f"{city}, {country}", "Forecast result", "Current conditions and short-term rainfall signal.")
    metric_cols = st.columns(4)
    for col, (label, value) in zip(
        metric_cols,
        [
            ("Temperature", f"{temperature} C"),
            ("Humidity", f"{humidity}%"),
            ("Wind Speed", f"{wind} m/s"),
            ("Rainfall", f"{rainfall} mm"),
        ],
    ):
        with col:
            render_metric_card(label, value)

    if rainfall < 1:
        st.success("No rainfall expected")
    elif rainfall < 5:
        st.info("Light rainfall possible")
    elif rainfall < 15:
        st.warning("Moderate rainfall expected")
    else:
        st.error("Heavy rainfall risk")

    render_section("5-day forecast", "Outlook", "Use the trend chart to compare near-term temperature and rainfall movement.")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    forecast = {
        "Temperature": [round(base_temp + np.random.normal(0, 2), 1) for _ in days],
        "Rainfall": [round(base_rain * np.random.uniform(0.01, 0.05), 2) for _ in days],
    }
    st.line_chart(forecast, height=300)

    day_cols = st.columns(5)
    for i, day in enumerate(days):
        with day_cols[i]:
            render_metric_card(day, f"{forecast['Temperature'][i]} C")

render_footer()
