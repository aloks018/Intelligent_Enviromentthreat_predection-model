import math
import sys
from pathlib import Path

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
    render_photo_card,
    render_section,
    render_text_card,
    render_topbar,
)


st.set_page_config(page_title="Water Pollution AI | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Water AI")

RIVER_BASELINE = {
    "Ganga": {"risk": 42, "industrial": 34, "population": 70},
    "Yamuna": {"risk": 58, "industrial": 62, "population": 78},
    "Brahmaputra": {"risk": 28, "industrial": 22, "population": 45},
    "Godavari": {"risk": 35, "industrial": 30, "population": 54},
    "Narmada": {"risk": 31, "industrial": 26, "population": 40},
    "Local River": {"risk": 38, "industrial": 36, "population": 48},
}


def calculate_pollution_score(
    river,
    ph,
    dissolved_oxygen,
    bod,
    turbidity,
    nitrate,
    conductivity,
    rainfall,
    industry_index,
):
    baseline = RIVER_BASELINE[river]
    score = baseline["risk"]
    score += abs(ph - 7.2) * 6
    score += max(0, 7 - dissolved_oxygen) * 6
    score += bod * 4
    score += turbidity * 0.45
    score += nitrate * 2.8
    score += max(0, conductivity - 450) * 0.025
    score += rainfall * 0.08
    score += industry_index * 0.32
    score += baseline["industrial"] * 0.08
    score += baseline["population"] * 0.06
    return min(100, max(0, int(round(score))))


def predicted_24h_score(score, rainfall, turbidity, bod):
    trend = 0.18 * rainfall + 0.22 * turbidity + 1.8 * bod
    dampening = 10 * math.exp(-max(score, 1) / 80)
    return min(100, max(0, int(round(score + trend / 8 - dampening))))


def pollution_category(score):
    if score <= 30:
        return "Clean / Low Risk", "Continue monitoring and protect catchment vegetation."
    if score <= 55:
        return "Moderate Risk", "Increase sampling frequency and inspect discharge sources."
    if score <= 75:
        return "High Risk", "Prioritize treatment, public warning, and industrial inspection."
    return "Critical Risk", "Restrict use, trace contamination, and activate river restoration response."


render_hero(
    title="River Water Pollution Detection and Prediction",
    summary=(
        "Use river big-data indicators to estimate pollution pressure, predict the next "
        "monitoring window, and plan restoration action."
    ),
    image="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=2400&q=90",
    kicker="River intelligence",
    meta="Detection | Prediction | Action",
)

render_section(
    "Big-data river workflow",
    "Pipeline",
    "A professional system combines field sensors, lab validation, rainfall, land-use pressure, and historical river records.",
)

pipeline_cols = st.columns(4)
pipeline = [
    ("Collect", "Ingest pH, oxygen, BOD, turbidity, nitrate, conductivity, rainfall, and station data.", "01"),
    ("Clean", "Normalize units, align timestamps, remove missing values, and flag outliers.", "02"),
    ("Detect", "Identify contamination, sewage inflow, industrial discharge, and runoff events.", "03"),
    ("Predict", "Forecast near-term pollution risk and recommend sampling priorities.", "04"),
]
for col, (title, body, kicker) in zip(pipeline_cols, pipeline):
    with col:
        render_text_card(title, body, kicker)

render_section(
    "Monitoring views",
    "Evidence",
    "The same visual structure is used for field condition, lab validation, and analytics.",
)

photo_cols = st.columns(3)
with photo_cols[0]:
    render_photo_card(
        "River segment monitoring",
        "Track pollution by location so response can target the exact stretch where risk is rising.",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1400&q=85",
        "Field",
    )
with photo_cols[1]:
    render_photo_card(
        "Laboratory validation",
        "Use sample testing to confirm sensor alerts and calibrate prediction quality over time.",
        "https://images.unsplash.com/photo-1581093588401-fbb62a02f120?auto=format&fit=crop&w=1400&q=85",
        "Lab",
    )
with photo_cols[2]:
    render_photo_card(
        "Big-data analytics",
        "Combine current readings, history, rainfall, and human pressure into one decision view.",
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1400&q=85",
        "Analytics",
    )

render_section(
    "Water pollution predictor",
    "Calculator",
    "Enter water-quality indicators to generate an educational risk score and 24-hour prediction.",
)

left, right = st.columns([1, 1], gap="large")
with left:
    river = st.selectbox("River", list(RIVER_BASELINE.keys()))
    ph = st.slider("pH level", 4.0, 10.0, 7.4, 0.1)
    dissolved_oxygen = st.slider("Dissolved oxygen mg/L", 0.0, 14.0, 6.2, 0.1)
    bod = st.slider("BOD mg/L", 0.0, 20.0, 4.5, 0.1)
    turbidity = st.slider("Turbidity NTU", 0.0, 120.0, 28.0, 1.0)
    nitrate = st.slider("Nitrate mg/L", 0.0, 25.0, 5.0, 0.5)
    conductivity = st.slider("Conductivity uS/cm", 50, 2500, 680, 10)
    rainfall = st.slider("Recent rainfall mm", 0, 250, 42)
    industry_index = st.slider("Nearby industry pressure index", 0, 100, 38)

score = calculate_pollution_score(
    river,
    ph,
    dissolved_oxygen,
    bod,
    turbidity,
    nitrate,
    conductivity,
    rainfall,
    industry_index,
)
next_score = predicted_24h_score(score, rainfall, turbidity, bod)
category, advice = pollution_category(score)

with right:
    render_metric_card("Current risk", f"{score}/100")
    st.progress(score / 100)
    render_metric_card("24h prediction", f"{next_score}/100")
    render_panel(category, advice)

render_section(
    "Sample river trend",
    "Preview",
    "This chart shows how live sensor streams could be visualized after integration with verified river monitoring data.",
)

trend = {
    "Pollution risk": [max(0, score - 20), max(0, score - 12), max(0, score - 8), score, next_score],
    "Turbidity": [max(0, turbidity - 16), max(0, turbidity - 8), max(0, turbidity - 4), turbidity, min(120, turbidity + rainfall / 20)],
    "BOD": [max(0, bod - 2), max(0, bod - 1.2), max(0, bod - 0.5), bod, min(20, bod + 0.8)],
}
st.line_chart(trend, height=310)

render_section(
    "River protection plan",
    "Action",
    "Use this order for municipal teams, schools, NGOs, housing societies, and local environmental groups.",
)

action_cols = st.columns(4)
actions = [
    ("Detect", "Install sensors, schedule lab tests, and map pollution hotspots.", "Step 1"),
    ("Stop sources", "Trace sewage, discharge, plastic dumping, and fertilizer runoff.", "Step 2"),
    ("Restore", "Build treatment, wetlands, river buffers, and cleanup drives.", "Step 3"),
    ("Govern", "Publish alerts, monitor compliance, and keep long-term records.", "Step 4"),
]
for col, (title, body, kicker) in zip(action_cols, actions):
    with col:
        render_text_card(title, body, kicker)

with st.expander("Recommended dataset columns for future model training"):
    st.write(
        "River name, station id, latitude, longitude, timestamp, pH, dissolved oxygen, BOD, COD, turbidity, "
        "temperature, nitrate, phosphate, fecal coliform, conductivity, rainfall, discharge, land-use type, "
        "industrial density, population density, and verified pollution class."
    )

render_footer()
