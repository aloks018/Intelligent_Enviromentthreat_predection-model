import os
import sys
import tempfile
from pathlib import Path

import folium
import joblib
import numpy as np
import requests
import streamlit as st
from gtts import gTTS
from openai import OpenAI
from streamlit_folium import st_folium

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
from business_impact import BUSINESS_PROFILES, calculate_business_impact


st.set_page_config(page_title="Map Intelligence | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Map")

render_hero(
    title="Geo-AI Environmental Map",
    summary=(
        "Click a location on the map to generate environmental indicators, AQI simulation, "
        "a business impact score, and an AI-assisted local risk briefing."
    ),
    image="https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=2400&q=90",
    kicker="Spatial intelligence",
    meta="Interactive map analysis",
)

render_section(
    "Interactive map workspace",
    "Map",
    "Select any location to generate a local report with temperature, rainfall, wind, AQI, business impact scoring, and assistant guidance.",
)
render_panel(
    "Map workflow",
    "Click a location, review generated indicators, estimate location-based business impact, then ask the assistant for environmental advice.",
)


api_key = None
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key) if api_key else None


@st.cache_resource
def load_model():
    model_path = ROOT_DIR / "models" / "best_aqi_model.pkl"
    if not model_path.exists():
        return None
    try:
        return joblib.load(model_path)
    except Exception:
        return None


model = load_model()


def create_map():
    map_obj = folium.Map(location=[22.97, 78.65], zoom_start=5)
    folium.TileLayer("OpenStreetMap").add_to(map_obj)
    folium.TileLayer("CartoDB positron").add_to(map_obj)
    folium.LayerControl().add_to(map_obj)
    return map_obj


def get_location(lat, lon):
    try:
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {"lat": lat, "lon": lon, "format": "json"}
        response = requests.get(url, params=params, timeout=5).json()
        address = response.get("address", {})
        return (
            address.get("city")
            or address.get("town")
            or address.get("village")
            or address.get("state")
            or "Unknown"
        )
    except Exception:
        return "Unknown"


def simulate(lat, lon):
    temp = 35 - (abs(lat - 23) * 0.25)
    rain = 50 + (abs(lat - 23) * 1.1)
    hum = 60 + (abs(lat - 23) * 0.4)
    wind = 5 + (abs(lon - 78) * 0.08)

    aqi = 0
    if model:
        aqi = model.predict(np.array([[temp, rain, hum, wind]]))[0]

    return temp, rain, hum, wind, aqi


def ai_response(user_input, context, history):
    if not client:
        return "AI assistant is not configured. Add an OPENAI_API_KEY to enable this feature."

    system = f"""
You are an environmental AI expert.

Location: {context['city']}
AQI: {context['aqi']}
Temperature: {context['temp']}
Rainfall: {context['rain']}
Business impact score: {context.get('business_score', 'Not calculated')}
Business type: {context.get('business_type', 'Not provided')}

Give practical, concise environmental advice.
"""

    messages = [{"role": "system", "content": system}]
    for role, message in history[-5:]:
        messages.append({"role": role, "content": message})
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception:
        return "AI response failed. Check API configuration and network access."


def speak(text):
    try:
        tts = gTTS(text)
        audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(audio_file.name)
        return audio_file.name
    except Exception:
        return None


map_data = st_folium(create_map(), height=550, use_container_width=True)

if map_data and map_data.get("last_clicked"):
    st.session_state.loc = (
        map_data["last_clicked"]["lat"],
        map_data["last_clicked"]["lng"],
    )

if "loc" in st.session_state:
    lat, lon = st.session_state.loc
    city = get_location(lat, lon)
    temp, rain, hum, wind, aqi = simulate(lat, lon)

    render_section("Selected location report", "Location", "Review generated environmental indicators for the selected map point.")
    st.write(f"**Location:** {city}")
    st.write(f"Latitude: {round(lat, 3)} | Longitude: {round(lon, 3)}")

    metric_cols = st.columns(4)
    for col, (label, value) in zip(
        metric_cols,
        [
            ("AQI", f"{float(aqi):.2f}"),
            ("Temperature", f"{temp:.2f} C"),
            ("Rainfall", f"{rain:.2f} mm"),
            ("Wind", f"{wind:.2f} m/s"),
        ],
    ):
        with col:
            render_metric_card(label, value)

    render_section(
        "Location-based business impact score",
        "Business",
        "Turn environmental signals into a business-ready location score using sector-specific risk weights.",
    )
    render_status(
        "This score is a decision-support estimate based on your AQI model output and transparent environmental risk rules for each business sector."
    )

    form_left, form_right = st.columns([1, 1], gap="large")
    with form_left:
        business_type = st.selectbox("Business sector", list(BUSINESS_PROFILES.keys()), index=0)
    with form_right:
        exposure_level = st.selectbox("Risk posture", ["Conservative", "Balanced", "Aggressive"], index=1)

    impact = calculate_business_impact(
        temperature=temp,
        rainfall=rain,
        humidity=hum,
        wind_speed=wind,
        aqi=float(aqi),
        business_type=business_type,
        exposure_level=exposure_level,
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

    detail_left, detail_right = st.columns([1.2, 0.8], gap="large")
    with detail_left:
        render_panel(
            "Business context",
            f"For {business_type.lower()} operations, the current location is most exposed through {str(impact['top_driver']).lower()} and {str(impact['secondary_driver']).lower()}.",
        )
        st.subheader("Risk components")
        for label, value in impact["components"].items():
            st.caption(f"{label}: {value:.1f}/100")
            st.progress(min(max(float(value) / 100.0, 0.0), 1.0))

    with detail_right:
        render_text_card(
            "Operational focus",
            f"This scoring model emphasizes {impact['focus']} for {business_type.lower()} teams.",
            "Business",
        )
        render_text_card(
            "Recommended actions",
            " ".join(impact["recommendations"]),
            "Action",
        )

    render_section("AI environmental assistant", "Chat", "Ask a question about the selected location and generated risk context.")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_input = st.chat_input("Ask about this location")
    if user_input:
        context = {
            "city": city,
            "aqi": aqi,
            "temp": temp,
            "rain": rain,
            "business_score": impact["score"],
            "business_type": business_type,
        }
        response = ai_response(user_input, context, st.session_state.chat)
        st.session_state.chat.append(("user", user_input))
        st.session_state.chat.append(("assistant", response))

        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(response)

        audio = speak(response)
        if audio:
            st.audio(audio)

    for role, message in st.session_state.chat:
        st.chat_message(role).write(message)
else:
    st.info("Click on the map to generate a location report.")

render_footer()
