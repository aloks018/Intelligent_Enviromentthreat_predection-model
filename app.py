import pandas as pd
import streamlit as st

from natgeo_theme import (
    inject_natgeo_theme,
    render_footer,
    render_metric_card,
    render_panel,
    render_status,
    render_text_card,
    render_topbar,
    render_trust_note,
)


st.set_page_config(
    page_title="IEIRAS | Environmental Intelligence",
    page_icon="IE",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_natgeo_theme()
render_topbar("Dashboard")

st.markdown(
    """
    <style>
    .ie-dashboard-shell {
        background:
            linear-gradient(135deg, rgba(8, 43, 31, 0.92), rgba(8, 94, 111, 0.82)),
            url("https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=2400&q=90");
        background-position: center;
        background-size: cover;
        border: 1px solid var(--ie-line);
        border-radius: 8px;
        box-shadow: 0 24px 52px rgba(15, 81, 50, 0.16);
        overflow: hidden;
        padding: 1.15rem;
    }

    .ie-dashboard-head {
        align-items: center;
        color: #ffffff;
        display: flex;
        gap: 1rem;
        justify-content: space-between;
        margin-bottom: 1rem;
        padding: 0.35rem 0.35rem 0.65rem 0.35rem;
    }

    .ie-dashboard-kicker {
        color: #bff5d2;
        font-size: 0.82rem;
        font-weight: 900;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .ie-dashboard-title {
        color: #ffffff;
        font-size: 2.35rem;
        font-weight: 900;
        line-height: 1.06;
        margin: 0.45rem 0 0 0;
        max-width: 700px;
    }

    .ie-dashboard-summary {
        color: rgba(255, 255, 255, 0.92);
        font-size: 0.95rem;
        line-height: 1.7;
        margin: 0.55rem 0 0 0;
        max-width: 720px;
    }

    .ie-dashboard-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        justify-content: flex-end;
    }

    .ie-dashboard-tag {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 999px;
        color: #ffffff;
        font-size: 0.76rem;
        font-weight: 900;
        padding: 0.58rem 0.8rem;
        text-transform: uppercase;
    }

    @media (max-width: 980px) {
        .ie-dashboard-head {
            align-items: flex-start;
            display: block;
        }

        .ie-dashboard-tags {
            justify-content: flex-start;
            margin-top: 0.9rem;
        }

        .ie-dashboard-title {
            font-size: 2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="ie-dashboard-shell">
        <div class="ie-dashboard-head">
            <div>
                <div class="ie-dashboard-kicker">AI environmental command center</div>
                <div class="ie-dashboard-title">AI Environmental Intelligence Platform</div>
                <p class="ie-dashboard-summary">
                    One premium dashboard for AQI prediction, rainfall analytics, water pollution monitoring,
                    geospatial intelligence, and climate risk awareness.
                </p>
            </div>
            <div class="ie-dashboard-tags">
                <div class="ie-dashboard-tag">AQI</div>
                <div class="ie-dashboard-tag">Forecast</div>
                <div class="ie-dashboard-tag">Water</div>
                <div class="ie-dashboard-tag">Maps</div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

render_status("Single dashboard active. Extra homepage dashboard sections removed.")

trend_data = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "AQI": [88, 82, 75, 71, 76, 69],
        "Water Health": [61, 66, 70, 73, 76, 80],
        "Forecast Confidence": [72, 74, 78, 81, 84, 87],
    }
)

risk_data = pd.DataFrame(
    {
        "Region": ["North", "Central", "Coastal", "River Belt", "Urban South"],
        "Risk Index": [58, 42, 71, 64, 49],
    }
)

main_col, side_col = st.columns([1.35, 0.65], gap="large")

with main_col:
    metric_cols = st.columns(4)
    dashboard_metrics = [
        ("AQI Accuracy", "96.4%"),
        ("Live Sensors", "1,260"),
        ("Forecast Range", "120h"),
        ("Active Alerts", "18"),
    ]
    for col, (label, value) in zip(metric_cols, dashboard_metrics):
        with col:
            render_metric_card(label, value)

    render_panel(
        "Unified environmental analytics",
        "Track air-quality signals, water-system health, and forecast confidence inside one balanced dashboard view.",
    )
    st.line_chart(trend_data.set_index("Month"), height=360, use_container_width=True)

    module_cols = st.columns(3)
    modules = [
        (
            "AQI Prediction",
            "Forecast urban air quality from temperature, humidity, rainfall, and wind inputs.",
            "Air",
        ),
        (
            "Live Map Intelligence",
            "Inspect geospatial risk, field conditions, and climate signals on the map page.",
            "Map",
        ),
        (
            "Business AI Impact",
            "Score business continuity, branch risk, and site reliability using environmental conditions.",
            "Business",
        ),
    ]
    for col, (title, body, kicker) in zip(module_cols, modules):
        with col:
            render_text_card(title, body, kicker)

    business_cols = st.columns([1.1, 0.9], gap="large")
    with business_cols[0]:
        render_panel(
            "New business intelligence page",
            "Business AI is now the page-6 replacement for the old SHAP page. Use it to evaluate operational risk, location suitability, and business continuity from environmental conditions.",
        )
    with business_cols[1]:
        st.page_link("pages/6_Business_Impact.py", label="Open Business AI")

    support_cols = st.columns(2)
    support_modules = [
        (
            "Water Pollution AI",
            "Monitor nitrate, pH, turbidity, and contamination patterns in river systems.",
            "Water",
        ),
        (
            "Forecast and Reporting",
            "Combine environmental trends with reports for clients, operations, and risk planning.",
            "Reporting",
        ),
    ]
    for col, (title, body, kicker) in zip(support_cols, support_modules):
        with col:
            render_text_card(title, body, kicker)

with side_col:
    render_panel(
        "Operational priorities",
        "This right-side panel is the only side dashboard now. The extra top dashboard block has been removed.",
    )
    st.bar_chart(risk_data.set_index("Region"), height=230, use_container_width=True)
    render_panel(
        "Recommended flow",
        "Home, Predict AQI, Map, Business AI, Forecast, Analytics, Report, Ocean + Ice, Water AI.",
    )
    render_panel(
        "Current focus",
        "High coastal alert, improving AQI confidence, stable river health, and rising forecast certainty across monitored regions.",
    )

render_trust_note()
render_footer()
