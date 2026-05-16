import os
import sys
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from natgeo_theme import (
    inject_natgeo_theme,
    render_footer,
    render_hero,
    render_panel,
    render_section,
    render_topbar,
)


st.set_page_config(page_title="Model Analytics | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Analytics")

render_hero(
    title="Model Analytics and Feature Influence",
    summary=(
        "Inspect which environmental variables influence AQI prediction so the model "
        "can be explained clearly in presentations and reports."
    ),
    image="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2400&q=90",
    kicker="Model transparency",
    meta="Feature importance",
)

render_section(
    "Understand model influence",
    "Analytics",
    "The chart and table show how strongly each environmental feature contributes to the AQI prediction model.",
)
render_panel(
    "Interpretation guide",
    "Higher magnitude means stronger influence. Positive values raise predicted AQI and negative values reduce it.",
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
features = ["Temperature", "Rainfall", "Humidity", "WindSpeed"]

if model is None:
    st.warning(model_error)
else:
    try:
        if hasattr(model, "coef_"):
            importance = model.coef_
        elif hasattr(model, "feature_importances_"):
            importance = model.feature_importances_
        else:
            st.warning("Model does not expose feature importance. Showing zero baseline.")
            importance = [0, 0, 0, 0]

        importance_df = pd.DataFrame({"Feature": features, "Importance": importance})
        render_section("Feature importance", "Result", "Compare variables by their contribution to AQI prediction.")
        st.bar_chart(importance_df.set_index("Feature"), height=340)
        st.dataframe(importance_df, use_container_width=True)

        insight_cols = st.columns(2)
        with insight_cols[0]:
            render_panel(
                "Strongest signal",
                f"{importance_df.iloc[importance_df['Importance'].abs().idxmax()]['Feature']} has the largest model coefficient by magnitude.",
            )
        with insight_cols[1]:
            render_panel(
                "Report usage",
                "Use this page before generating the PDF report to explain why the prediction changed.",
            )
    except Exception as exc:
        st.error(f"Error during analysis: {exc}")

render_footer()
