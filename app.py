import streamlit as st

from natgeo_theme import (
    inject_natgeo_theme,
    render_cta_links,
    render_footer,
    render_hero,
    render_metric_card,
    render_panel,
    render_photo_card,
    render_section,
    render_status,
    render_text_card,
    render_topbar,
    render_trust_note,
)


st.set_page_config(
    page_title="IEIRAS | Environmental Intelligence",
    page_icon="IE",
    layout="wide",
)

inject_natgeo_theme()
render_topbar("Home")

render_hero(
    title="Environmental Intelligence for Safer Decisions",
    summary=(
        "IEIRAS brings air-quality prediction, map intelligence, weather forecasting, "
        "model analytics, ocean risk, river water pollution AI, and reports into one "
        "professional environmental dashboard."
    ),
    image="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=2400&q=90",
    kicker="Integrated dashboard",
    meta="AQI | Climate | Water | Reports",
)

render_status("System ready: choose a tool below or start with the AQI prediction workflow.")
render_cta_links()

render_section(
    "Dashboard overview",
    "Start here",
    "Use the same sequence across the website: understand the project, run prediction, inspect maps and forecasts, review model logic, then generate a report.",
)

metric_cols = st.columns(4)
metrics = [
    ("Prediction", "AQI"),
    ("Mapping", "Risk"),
    ("Forecast", "Rainfall"),
    ("Reporting", "PDF"),
]
for col, (label, value) in zip(metric_cols, metrics):
    with col:
        render_metric_card(label, value)

render_section(
    "Core tools",
    "Workflow",
    "Each page now follows one design system so the project feels like a single product instead of separate demos.",
)

tool_cols = st.columns(3)
with tool_cols[0]:
    render_text_card(
        "Air intelligence",
        "Predict AQI, review safety guidance, and explain model behavior with clear environmental indicators.",
        "Prediction",
    )
with tool_cols[1]:
    render_text_card(
        "Spatial awareness",
        "Open the interactive map, select a location, and convert coordinates into risk and weather context.",
        "Mapping",
    )
with tool_cols[2]:
    render_text_card(
        "Climate and water risk",
        "Use ocean, ice, and river pollution pages to connect air quality with wider environmental resilience.",
        "Resilience",
    )

render_section(
    "Featured environmental modules",
    "Explore",
    "The homepage uses the same card style and visual rhythm as the rest of the dashboard.",
)

photo_cols = st.columns(3)
with photo_cols[0]:
    render_photo_card(
        "AQI prediction workflow",
        "Estimate air quality from temperature, rainfall, humidity, and wind speed.",
        "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?auto=format&fit=crop&w=1400&q=85",
        "Air",
    )
with photo_cols[1]:
    render_photo_card(
        "Ocean and ice threat",
        "Plan for long-term living safety using coastal, flood, heat, and water-security risk checks.",
        "https://images.unsplash.com/photo-1517783999520-f068d7431a60?auto=format&fit=crop&w=1400&q=85",
        "Climate",
    )
with photo_cols[2]:
    render_photo_card(
        "River water pollution AI",
        "Detect and predict river pollution using water-quality indicators and big-data logic.",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1400&q=85",
        "Water",
    )

render_section(
    "Recommended page order",
    "Navigation",
    "Home, Overview, Predict AQI, Map, Forecast, Analytics, Safety, Report, Ocean + Ice, Water AI.",
)

order_cols = st.columns(2)
with order_cols[0]:
    render_panel(
        "For project presentation",
        "Start with Overview, demonstrate AI Prediction, open Map Intelligence, show Forecast, then explain Analytics and Safety guidance.",
    )
with order_cols[1]:
    render_panel(
        "For environmental action",
        "Use Ocean + Ice and Water AI after the core AQI workflow to show broader climate and river-risk planning.",
    )

render_trust_note()
render_footer()
