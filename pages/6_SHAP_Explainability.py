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
    render_section,
    render_text_card,
    render_topbar,
)


st.set_page_config(page_title="Safety Advisor | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Safety")

render_hero(
    title="Environmental Safety Advisor",
    summary=(
        "Convert AQI values into practical health guidance for citizens, students, "
        "and local awareness reports."
    ),
    image="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=2400&q=90",
    kicker="Public safety",
    meta="AQI guidance",
)

render_section(
    "Check safety level",
    "Input",
    "Select a city and AQI level to receive a simple risk category, health advisory, and recommended actions.",
)

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Lucknow"]

col1, col2 = st.columns(2)
with col1:
    city = st.selectbox("City", cities)
with col2:
    aqi = st.slider("AQI Level", 0, 500, 120)

render_panel(
    "Health context",
    "Air pollution affects lungs, heart health, productivity, and outdoor activity decisions.",
)

if st.button("Analyze Safety"):
    if aqi <= 50:
        status = "Good"
        advice = "Air quality is good. Outdoor activity is generally suitable."
        action = "Continue normal outdoor routines and keep monitoring."
    elif aqi <= 100:
        status = "Moderate"
        advice = "Acceptable for most people, but sensitive groups should be cautious."
        action = "Limit prolonged outdoor exertion for sensitive groups."
    elif aqi <= 200:
        status = "Unhealthy"
        advice = "Health effects may begin for many people, especially outdoors."
        action = "Reduce outdoor activity and use masks if exposure is unavoidable."
    else:
        status = "Very Unhealthy"
        advice = "Serious exposure risk. Indoor protection should be prioritized."
        action = "Stay indoors, use filtration, and avoid heavy outdoor work."

    render_section(f"{city} environmental status", "Result", "The advisory below can be used in local awareness reports.")
    result_cols = st.columns(3)
    with result_cols[0]:
        render_metric_card("AQI", str(aqi))
    with result_cols[1]:
        render_metric_card("Status", status)
    with result_cols[2]:
        st.progress(min(aqi / 500, 1))
        st.caption("Relative exposure pressure")

    detail_cols = st.columns(2)
    with detail_cols[0]:
        render_text_card("Health advisory", advice, "Guidance")
    with detail_cols[1]:
        render_text_card("Recommended action", action, "Action")

    render_panel(
        "Daily precautions",
        "Stay hydrated, monitor AQI regularly, reduce exposure during high-pollution periods, and protect sensitive people first.",
    )

render_footer()
