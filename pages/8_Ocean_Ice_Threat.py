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


st.set_page_config(page_title="Ocean + Ice Threat | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Ocean + Ice")

render_hero(
    title="Ocean Threat and Ice Melt Resilience",
    summary=(
        "Assess how sea-level rise, storm surge, polar ice melt, heat, and water stress "
        "can affect long-term living safety in local areas."
    ),
    image="https://images.unsplash.com/photo-1517783999520-f068d7431a60?auto=format&fit=crop&w=2400&q=90",
    kicker="Climate resilience",
    meta="Long-term living safety",
)

render_section(
    "Ocean and ice systems",
    "Threats",
    "Use this page to connect global ice melt and ocean change with local planning for homes, schools, roads, water, and health.",
)

threat_cols = st.columns(4)
threats = [
    ("Sea-level rise", "Low-lying coastal and river-mouth areas face more frequent flooding and saltwater intrusion.", "Water"),
    ("Storm surge", "Severe weather can push ocean water inland and damage homes, roads, and services.", "Coast"),
    ("Freshwater stress", "Saltwater and rainfall extremes can reduce reliable drinking-water access.", "Water"),
    ("Heat and health", "Heat, humidity, pollution, and stagnant water increase health risk.", "Health"),
]
for col, (title, body, kicker) in zip(threat_cols, threats):
    with col:
        render_text_card(title, body, kicker)

render_section(
    "Risk views",
    "Briefing",
    "The same card and section style is used here as every other IEIRAS page.",
)

photo_cols = st.columns(3)
with photo_cols[0]:
    render_photo_card(
        "Ice melt signal",
        "Polar ice loss is a long-term warning for ocean rise and coastal safety planning.",
        "https://images.unsplash.com/photo-1517783999520-f068d7431a60?auto=format&fit=crop&w=1400&q=85",
        "Ice",
    )
with photo_cols[1]:
    render_photo_card(
        "Coastal buffers",
        "Wetlands, dunes, mangroves, and drainage channels reduce flood damage.",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1400&q=85",
        "Coast",
    )
with photo_cols[2]:
    render_photo_card(
        "Community adaptation",
        "Prepared homes, safe shelters, water storage, and local maps reduce future risk.",
        "https://images.unsplash.com/photo-1470770903676-69b98201ea1c?auto=format&fit=crop&w=1400&q=85",
        "Planning",
    )

render_section(
    "Local area risk preview",
    "Calculator",
    "This educational screening tool helps decide which safety actions should come first.",
)

left, right = st.columns([1, 1], gap="large")
with left:
    area_type = st.selectbox(
        "Area type",
        ["Coastal city", "River delta or low-lying village", "Inland urban area", "Hill or elevated area"],
    )
    distance = st.slider("Distance from sea or tidal river in km", 0, 100, 12)
    elevation = st.slider("Approximate elevation in meters", 0, 100, 8)
    drainage = st.select_slider("Drainage condition", options=["Poor", "Average", "Good"], value="Average")
    green_cover = st.select_slider("Local green cover", options=["Low", "Medium", "High"], value="Medium")

base_scores = {
    "Coastal city": 34,
    "River delta or low-lying village": 40,
    "Inland urban area": 18,
    "Hill or elevated area": 8,
}
score = base_scores[area_type]
score += max(0, 30 - distance) // 2
score += max(0, 15 - elevation)
score += {"Poor": 18, "Average": 8, "Good": 0}[drainage]
score += {"Low": 12, "Medium": 5, "High": 0}[green_cover]
score = min(100, max(0, int(score)))

if score <= 35:
    category = "Lower risk"
    advice = "Focus on awareness, drainage care, heat protection, and local green cover."
elif score <= 65:
    category = "Medium risk"
    advice = "Prioritize flood readiness, water security, insurance, and community response plans."
else:
    category = "Higher risk"
    advice = "Plan stronger adaptation, elevated services, evacuation routes, and long-term relocation options."

with right:
    render_metric_card("Risk Score", f"{score}/100")
    st.progress(score / 100)
    render_panel(category, advice)

render_section(
    "Save your area",
    "Action plan",
    "Use this order for local committees, schools, housing societies, villages, and city wards.",
)

plan_cols = st.columns(4)
plans = [
    ("Know the ground", "Map low elevation zones, drains, flood marks, water points, shelters, and vulnerable households.", "Step 1"),
    ("Build natural protection", "Protect wetlands, ponds, trees, dunes, and open soil wherever possible.", "Step 2"),
    ("Upgrade services", "Raise electrical systems, secure roofs, clean drains, and prepare emergency kits.", "Step 3"),
    ("Plan the future", "Avoid new construction in repeat hazard zones and prepare safe relocation options.", "Step 4"),
]
for col, (title, body, kicker) in zip(plan_cols, plans):
    with col:
        render_text_card(title, body, kicker)

render_section(
    "Timeline",
    "Resilience",
    "A practical adaptation timeline helps turn climate awareness into decisions.",
)

timeline_cols = st.columns(4)
for col, (label, value) in zip(
    timeline_cols,
    [
        ("This month", "Kits and drains"),
        ("This year", "Risk map"),
        ("5 years", "Public upgrades"),
        ("10+ years", "Safe planning"),
    ],
):
    with col:
        render_metric_card(label, value)

render_footer()
