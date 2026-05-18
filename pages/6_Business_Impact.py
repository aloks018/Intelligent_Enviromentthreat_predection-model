import pandas as pd
import streamlit as st

from business_impact import BUSINESS_PROFILES, calculate_business_impact
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


st.set_page_config(page_title="Business Impact | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Business AI")

render_hero(
    title="Location-Based Business Impact Score",
    summary=(
        "Estimate how environmental conditions may affect business continuity, workforce safety, "
        "site reliability, and operating risk for different industry sectors."
    ),
    image="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=2400&q=90",
    kicker="Business intelligence",
    meta="Sector-based risk scoring",
)

render_section(
    "Business location scoring",
    "Impact",
    "Use environmental conditions and sector-specific weights to estimate the operational impact of a location.",
)
render_panel(
    "How this helps business teams",
    "This page converts AQI, heat, rainfall, wind, humidity, and water stress signals into a business-ready location score with practical recommendations.",
)

left, right = st.columns([1, 1], gap="large")
with left:
    location_name = st.text_input("Business location or site name", "Industrial Zone A")
    business_type = st.selectbox("Business sector", list(BUSINESS_PROFILES.keys()), index=0)
    exposure_level = st.selectbox("Risk posture", ["Conservative", "Balanced", "Aggressive"], index=1)
with right:
    temperature = st.slider("Temperature (C)", 15.0, 50.0, 34.0)
    rainfall = st.slider("Rainfall (mm)", 0.0, 180.0, 48.0)
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 62.0)
    wind_speed = st.slider("Wind speed (km/h)", 1.0, 40.0, 12.0)
    aqi = st.slider("AQI", 10.0, 350.0, 92.0)

impact = calculate_business_impact(
    temperature=temperature,
    rainfall=rainfall,
    humidity=humidity,
    wind_speed=wind_speed,
    aqi=aqi,
    business_type=business_type,
    exposure_level=exposure_level,
)

render_status(
    f"Scoring live for {location_name}: business continuity is currently {str(impact['continuity']).lower()} with a {str(impact['category']).lower()} impact profile."
)

score_cols = st.columns(4)
for col, (label, value) in zip(
    score_cols,
    [
        ("Impact Score", f"{impact['score']}/100"),
        ("Risk Class", str(impact["category"])),
        ("Continuity", str(impact["continuity"])),
        ("Top Driver", str(impact["top_driver"])),
    ],
):
    with col:
        render_metric_card(label, value)

main_col, side_col = st.columns([1.2, 0.8], gap="large")

component_df = pd.DataFrame(
    {
        "Risk Component": list(impact["components"].keys()),
        "Score": list(impact["components"].values()),
    }
)

scenario_df = pd.DataFrame(
    [
        {"Scenario": "Today", "Business Score": impact["score"]},
        {
            "Scenario": "Hotter +5C",
            "Business Score": calculate_business_impact(
                temperature=temperature + 5,
                rainfall=rainfall,
                humidity=humidity,
                wind_speed=wind_speed,
                aqi=aqi + 18,
                business_type=business_type,
                exposure_level=exposure_level,
            )["score"],
        },
        {
            "Scenario": "Heavy Rain",
            "Business Score": calculate_business_impact(
                temperature=temperature,
                rainfall=rainfall + 45,
                humidity=min(humidity + 12, 100),
                wind_speed=wind_speed + 4,
                aqi=aqi,
                business_type=business_type,
                exposure_level=exposure_level,
            )["score"],
        },
        {
            "Scenario": "Cleaner Air",
            "Business Score": calculate_business_impact(
                temperature=temperature,
                rainfall=rainfall,
                humidity=humidity,
                wind_speed=wind_speed,
                aqi=max(aqi - 35, 10),
                business_type=business_type,
                exposure_level=exposure_level,
            )["score"],
        },
    ]
)

with main_col:
    render_panel(
        "Risk breakdown",
        f"For {business_type.lower()} operations, the location is most affected by {str(impact['top_driver']).lower()} and {str(impact['secondary_driver']).lower()}.",
    )
    st.bar_chart(component_df.set_index("Risk Component"), height=300, use_container_width=True)

    detail_cols = st.columns(2)
    with detail_cols[0]:
        render_text_card(
            "Operational focus",
            f"This score emphasizes {impact['focus']} for {business_type.lower()} teams.",
            "Business",
        )
    with detail_cols[1]:
        render_text_card(
            "Location note",
            f"{location_name} can be compared with other branches, plants, warehouses, or project sites using the same scoring method.",
            "Location",
        )

with side_col:
    render_panel(
        "Recommended actions",
        " ".join(impact["recommendations"]),
    )
    render_panel(
        "Scenario comparison",
        "Review how this site behaves under hotter, wetter, and cleaner-air conditions.",
    )
    st.line_chart(scenario_df.set_index("Scenario"), height=220, use_container_width=True)

render_section(
    "Best business uses",
    "Use cases",
    "This feature is useful for site selection, branch comparison, factory planning, project risk review, ESG reporting, and operations readiness.",
)

use_cols = st.columns(3)
use_cases = [
    (
        "Site selection",
        "Compare future factory, office, resort, or warehouse locations before investing.",
        "Investment",
    ),
    (
        "Operational planning",
        "Estimate whether today's environmental conditions could affect safety, staff productivity, or logistics.",
        "Operations",
    ),
    (
        "Client reporting",
        "Use the score in presentations and environmental decision reports for stakeholders.",
        "Reporting",
    ),
]
for col, (title, body, kicker) in zip(use_cols, use_cases):
    with col:
        render_text_card(title, body, kicker)

render_footer()
