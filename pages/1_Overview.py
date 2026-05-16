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
    render_status,
    render_text_card,
    render_topbar,
)


st.set_page_config(page_title="Overview | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Overview")

render_hero(
    title="Project Overview and System Purpose",
    summary=(
        "IEIRAS is a unified environmental intelligence platform for AQI prediction, "
        "risk mapping, rainfall forecasting, explainable analytics, report generation, "
        "ocean awareness, and river water pollution prediction."
    ),
    image="https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=2400&q=90",
    kicker="Project foundation",
    meta="Environmental intelligence",
)

render_status("All pages now use one professional layout, navigation system, and visual language.")

render_section(
    "What the system does",
    "Purpose",
    "The dashboard turns environmental inputs into readable predictions, maps, risk summaries, and reports for academic demonstration and decision support.",
)

metric_cols = st.columns(4)
for col, (label, value) in zip(
    metric_cols,
    [
        ("Model focus", "AQI"),
        ("Risk view", "Map"),
        ("Climate view", "Forecast"),
        ("Output", "Report"),
    ],
):
    with col:
        render_metric_card(label, value)

render_section(
    "Core capability sequence",
    "Workflow",
    "Each capability is arranged in the same structure so users can move through the project without relearning the interface.",
)

cols = st.columns(3)
with cols[0]:
    render_text_card(
        "Prediction",
        "Run environmental parameters through the trained model and classify air-quality pressure.",
        "AI",
    )
with cols[1]:
    render_text_card(
        "Spatial intelligence",
        "Use map selections to inspect local environmental context and create location-specific insights.",
        "Geo",
    )
with cols[2]:
    render_text_card(
        "Explainability",
        "Review feature influence and safety guidance so model outputs are easier to trust and present.",
        "Trust",
    )

render_section(
    "Project use cases",
    "Application",
    "IEIRAS can support classroom demonstrations, local awareness dashboards, environmental reports, and early-stage decision-support prototypes.",
)

info_cols = st.columns(2)
with info_cols[0]:
    render_panel(
        "Academic demonstration",
        "Show how AI, maps, charts, and reports can be connected into a single environmental analytics workflow.",
    )
with info_cols[1]:
    render_panel(
        "Public awareness",
        "Explain AQI, rainfall, ocean risk, and river pollution in a clear format for non-technical users.",
    )

render_footer()
