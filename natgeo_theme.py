from __future__ import annotations

import base64
from html import escape
from mimetypes import guess_type
from pathlib import Path

import streamlit as st


PAGE_LINKS = [
    ("app.py", "Home"),
    ("pages/1_Overview.py", "Overview"),
    ("pages/2_AI_Prediction.py", "Predict AQI"),
    ("pages/3_Map_AI_Prediction.py", "Map"),
    ("pages/4_Time_Series_Forecast.py", "Forecast"),
    ("pages/5_Model_Analytics.py", "Analytics"),
    ("pages/6_SHAP_Explainability.py", "Safety"),
    ("pages/7_Generate_Report.py", "Report"),
    ("pages/8_Ocean_Ice_Threat.py", "Ocean + Ice"),
    ("pages/9_Water_Pollution_Prediction.py", "Water AI"),
]


def _image_src(image: str) -> str:
    path = Path(image)
    if path.exists():
        mime = guess_type(path.name)[0] or "image/jpeg"
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        return f"data:{mime};base64,{data}"
    return image


def inject_natgeo_theme() -> None:
    st.markdown(
        """
        <style>
        :root {
            --ie-ink: #10231a;
            --ie-muted: #62756a;
            --ie-green: #0f5132;
            --ie-green-2: #1f7a4d;
            --ie-teal: #0e7490;
            --ie-mint: #e6f7ed;
            --ie-mist: #f5fbf7;
            --ie-line: #cfe6d7;
            --ie-white: #ffffff;
            --ie-warn: #b45309;
            --ie-danger: #b91c1c;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background:
                radial-gradient(circle at top left, rgba(31, 122, 77, 0.12), transparent 28rem),
                linear-gradient(180deg, #ffffff 0%, #f5fbf7 54%, #ffffff 100%);
            color: var(--ie-ink);
            font-family: Georgia, "Times New Roman", serif;
        }

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }

        h1 {
            display: none;
        }

        h2,
        h3,
        h4,
        p,
        label,
        span {
            letter-spacing: 0;
        }

        .ie-hero h1 {
            display: block;
        }

        .block-container {
            max-width: 1240px;
            padding-top: 1rem;
            padding-bottom: 2.2rem;
        }

        [data-testid="stSidebar"] {
            background: var(--ie-green);
            border-right: 4px solid var(--ie-teal);
        }

        [data-testid="stSidebar"] * {
            color: #ffffff;
        }

        .ie-topbar {
            align-items: center;
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid var(--ie-line);
            border-radius: 8px;
            box-shadow: 0 14px 34px rgba(15, 81, 50, 0.08);
            display: grid;
            gap: 0.85rem;
            grid-template-columns: minmax(210px, 315px) minmax(0, 1fr);
            margin-bottom: 0.75rem;
            padding: 0.82rem 0.9rem;
            position: sticky;
            top: 0.65rem;
            z-index: 20;
        }

        .ie-brand {
            align-items: center;
            display: flex;
            gap: 0.7rem;
            min-width: 0;
        }

        .ie-logo {
            align-items: center;
            background: linear-gradient(135deg, var(--ie-green), var(--ie-teal));
            border-radius: 8px;
            color: #ffffff;
            display: flex;
            flex: 0 0 auto;
            font-size: 0.78rem;
            font-weight: 900;
            height: 42px;
            justify-content: center;
            width: 58px;
        }

        .ie-brand-title {
            color: var(--ie-green);
            font-size: 1.02rem;
            font-weight: 900;
            line-height: 1.05;
            text-transform: uppercase;
        }

        .ie-brand-subtitle {
            color: var(--ie-muted);
            font-size: 0.76rem;
            font-weight: 700;
            margin-top: 0.12rem;
        }

        .ie-nav {
            align-items: center;
            display: flex;
            flex-wrap: wrap;
            gap: 0.42rem;
            justify-content: flex-end;
            min-width: 0;
        }

        .ie-nav a,
        .ie-nav span {
            border-radius: 8px;
            display: inline-flex;
            font-size: 0.72rem;
            font-weight: 900;
            line-height: 1;
            padding: 0.52rem 0.58rem;
            text-decoration: none;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .ie-nav span {
            background: var(--ie-mint);
            color: var(--ie-green);
        }

        .ie-nav a {
            background: #ffffff;
            border: 1px solid var(--ie-line);
            color: var(--ie-ink);
        }

        .ie-nav .ie-nav-primary {
            background: var(--ie-green);
            border-color: var(--ie-green);
            color: #ffffff;
        }

        .ie-linkbar {
            background: #ffffff;
            border: 1px solid var(--ie-line);
            border-radius: 8px;
            box-shadow: 0 10px 24px rgba(15, 81, 50, 0.07);
            margin: 0 0 1rem 0;
            padding: 0.45rem;
        }

        .ie-linkbar [data-testid="stHorizontalBlock"] {
            gap: 0.35rem;
            margin-bottom: 0.35rem;
        }

        .ie-linkbar [data-testid="stPageLink"] {
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 800;
        }

        .ie-hero {
            background-position: center;
            background-size: cover;
            border-radius: 8px;
            box-shadow: 0 24px 52px rgba(15, 81, 50, 0.18);
            min-height: 465px;
            overflow: hidden;
            position: relative;
        }

        .ie-hero::before {
            background: linear-gradient(90deg, rgba(15, 81, 50, 0.92), rgba(14, 116, 144, 0.68), rgba(15, 81, 50, 0.10));
            content: "";
            inset: 0;
            position: absolute;
        }

        .ie-hero-body {
            color: #ffffff;
            max-width: 780px;
            padding: 5.1rem 2.7rem 2.6rem 2.7rem;
            position: relative;
            z-index: 1;
        }

        .ie-kicker,
        .ie-card-kicker,
        .ie-section-kicker {
            color: #bff5d2;
            font-size: 0.8rem;
            font-weight: 900;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .ie-hero h1 {
            color: #ffffff;
            font-size: 3.2rem;
            font-weight: 900;
            line-height: 1.03;
            margin: 0.68rem 0 0.9rem 0;
            max-width: 780px;
        }

        .ie-hero p {
            color: #eefaf2;
            font-size: 1.05rem;
            line-height: 1.68;
            margin: 0;
            max-width: 700px;
        }

        .ie-hero-meta {
            background: rgba(255, 255, 255, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.34);
            border-radius: 8px;
            color: #ffffff;
            display: inline-block;
            font-size: 0.78rem;
            font-weight: 900;
            margin-top: 1.1rem;
            padding: 0.62rem 0.78rem;
            text-transform: uppercase;
        }

        .ie-section {
            margin-top: 1.55rem;
        }

        .ie-section-head {
            align-items: end;
            display: grid;
            gap: 1rem;
            grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
            margin-bottom: 1rem;
        }

        .ie-section-title {
            color: var(--ie-ink);
            font-size: 2rem;
            font-weight: 900;
            line-height: 1.14;
            margin: 0.3rem 0 0 0;
        }

        .ie-section-copy {
            color: var(--ie-muted);
            font-size: 0.98rem;
            line-height: 1.62;
            margin: 0;
        }

        .ie-card,
        .ie-photo-card,
        .ie-metric-card,
        .ie-panel,
        .kpi-card,
        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid var(--ie-line);
            border-radius: 8px;
            box-shadow: 0 12px 30px rgba(15, 81, 50, 0.08);
            overflow: hidden;
        }

        .ie-card,
        .ie-panel,
        .kpi-card {
            padding: 1rem;
        }

        .ie-card,
        .kpi-card,
        .ie-metric-card {
            border-top: 5px solid var(--ie-green);
        }

        .ie-card h3,
        .ie-panel h3,
        .ie-photo-title {
            color: var(--ie-ink);
            font-size: 1.12rem;
            font-weight: 900;
            line-height: 1.34;
            margin: 0.42rem 0;
        }

        .ie-card p,
        .ie-panel p,
        .ie-photo-copy {
            color: var(--ie-muted);
            line-height: 1.55;
            margin: 0.35rem 0 0 0;
        }

        .ie-panel {
            min-height: 126px;
        }

        .ie-status {
            background: linear-gradient(135deg, #ffffff 0%, var(--ie-mint) 100%);
            border: 1px solid var(--ie-line);
            border-left: 6px solid var(--ie-teal);
            border-radius: 8px;
            color: var(--ie-ink);
            font-weight: 800;
            margin: 1rem 0 0 0;
            padding: 0.9rem 1rem;
        }

        .ie-photo {
            background-position: center;
            background-size: cover;
            min-height: 230px;
        }

        .ie-photo-body {
            padding: 1rem;
        }

        .ie-metric-card {
            padding: 1rem;
            min-height: 118px;
        }

        .ie-metric-label,
        div[data-testid="stMetricLabel"] {
            color: var(--ie-muted);
            font-size: 0.8rem;
            font-weight: 900;
            text-transform: uppercase;
        }

        .ie-metric-value,
        div[data-testid="stMetricValue"] {
            color: var(--ie-green);
            font-size: 1.7rem;
            font-weight: 900;
            margin-top: 0.24rem;
        }

        div[data-testid="stMetric"] {
            padding: 0.9rem;
        }

        .stButton > button,
        .stDownloadButton > button {
            background: var(--ie-green);
            border: 1px solid var(--ie-green);
            border-radius: 8px;
            color: #ffffff;
            font-weight: 900;
            min-height: 2.75rem;
            text-transform: uppercase;
            width: 100%;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background: var(--ie-green-2);
            border-color: var(--ie-green-2);
            color: #ffffff;
        }

        .stSelectbox [data-baseweb="select"] > div,
        .stNumberInput input,
        .stTextInput input,
        div[data-testid="stSlider"] {
            border-radius: 8px;
        }

        div[data-testid="stSlider"] {
            background: #ffffff;
            border: 1px solid var(--ie-line);
            padding: 0.8rem 0.9rem;
        }

        div[data-testid="stImage"] img {
            border-radius: 8px;
        }

        .ie-footer {
            background: var(--ie-green);
            border-radius: 8px;
            color: #ffffff;
            margin-top: 1.8rem;
            padding: 1.35rem;
        }

        .ie-footer-grid {
            display: grid;
            gap: 1.2rem;
            grid-template-columns: 1.3fr 1fr 1fr;
        }

        .ie-footer h3,
        .ie-footer h4 {
            color: #ffffff;
            font-weight: 900;
            margin: 0 0 0.55rem 0;
        }

        .ie-footer p,
        .ie-footer a,
        .ie-footer li {
            color: #e9f8ee;
            line-height: 1.6;
        }

        .ie-footer ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .ie-footer a {
            text-decoration: none;
        }

        .ie-footer-note {
            border-top: 1px solid rgba(255, 255, 255, 0.22);
            color: #e9f8ee;
            font-size: 0.86rem;
            margin-top: 1rem;
            padding-top: 0.85rem;
        }

        @media (max-width: 980px) {
            .ie-topbar,
            .ie-section-head,
            .ie-footer-grid {
                align-items: flex-start;
                display: flex;
                flex-direction: column;
            }

            .ie-nav {
                justify-content: flex-start;
                width: 100%;
            }
        }

        @media (max-width: 720px) {
            .ie-logo {
                height: 34px;
                width: 48px;
            }

            .ie-brand-title {
                font-size: 0.9rem;
            }

            .ie-nav a,
            .ie-nav span {
                font-size: 0.68rem;
                padding: 0.45rem 0.48rem;
            }

            .ie-hero {
                min-height: 410px;
            }

            .ie-hero-body {
                padding: 3.3rem 1.25rem 1.8rem 1.25rem;
            }

            .ie-hero h1 {
                font-size: 2.2rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_topbar(active: str = "Environment") -> None:
    st.markdown(
        f"""
        <div class="ie-topbar">
            <div class="ie-brand">
                <div class="ie-logo">IE</div>
                <div>
                    <div class="ie-brand-title">IEIRAS Impact</div>
                    <div class="ie-brand-subtitle">Environmental intelligence dashboard</div>
                </div>
            </div>
            <div class="ie-nav">
                <span>{escape(active)}</span>
                <a href="/" target="_self">Home</a>
                <a href="/AI_Prediction" target="_self">Predict AQI</a>
                <a href="/Map_AI_Prediction" target="_self">Map</a>
                <a href="/Water_Pollution_Prediction" target="_self">Water AI</a>
                <a class="ie-nav-primary" href="/Generate_Report" target="_self">Report</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_page_links()


def render_page_links() -> None:
    st.markdown('<div class="ie-linkbar">', unsafe_allow_html=True)
    max_per_row = 5
    for start in range(0, len(PAGE_LINKS), max_per_row):
        row = PAGE_LINKS[start : start + max_per_row]
        columns = st.columns(len(row))
        for column, (page, label) in zip(columns, row):
            with column:
                st.page_link(page, label=label)
    st.markdown("</div>", unsafe_allow_html=True)


def render_cta_links() -> None:
    st.markdown('<div class="ie-status">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.page_link("pages/2_AI_Prediction.py", label="Predict AQI")
    with c2:
        st.page_link("pages/3_Map_AI_Prediction.py", label="Open Map")
    with c3:
        st.page_link("pages/7_Generate_Report.py", label="Generate Report")
    st.markdown("</div>", unsafe_allow_html=True)


def render_hero(title: str, summary: str, image: str, kicker: str, meta: str = "") -> None:
    image = _image_src(image)
    safe_meta = f'<div class="ie-hero-meta">{escape(meta)}</div>' if meta else ""
    st.markdown(
        f"""
        <section class="ie-hero" style="background-image: url('{escape(image)}');">
            <div class="ie-hero-body">
                <div class="ie-kicker">{escape(kicker)}</div>
                <h1>{escape(title)}</h1>
                <p>{escape(summary)}</p>
                {safe_meta}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_section(title: str, kicker: str = "Overview", copy: str = "") -> None:
    copy_html = f'<p class="ie-section-copy">{escape(copy)}</p>' if copy else ""
    st.markdown(
        f"""
        <section class="ie-section">
            <div class="ie-section-head">
                <div>
                    <div class="ie-section-kicker">{escape(kicker)}</div>
                    <div class="ie-section-title">{escape(title)}</div>
                </div>
                {copy_html}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_status(text: str) -> None:
    st.markdown(f'<div class="ie-status">{escape(text)}</div>', unsafe_allow_html=True)


def render_text_card(title: str, body: str, kicker: str = "Environment") -> None:
    st.markdown(
        f"""
        <article class="ie-card">
            <div class="ie-card-kicker">{escape(kicker)}</div>
            <h3>{escape(title)}</h3>
            <p>{escape(body)}</p>
        </article>
        """,
        unsafe_allow_html=True,
    )


def render_photo_card(title: str, body: str, image: str, kicker: str = "Environment") -> None:
    image = _image_src(image)
    st.markdown(
        f"""
        <article class="ie-photo-card">
            <div class="ie-photo" style="background-image: url('{escape(image)}');"></div>
            <div class="ie-photo-body">
                <div class="ie-card-kicker">{escape(kicker)}</div>
                <div class="ie-photo-title">{escape(title)}</div>
                <p class="ie-photo-copy">{escape(body)}</p>
            </div>
        </article>
        """,
        unsafe_allow_html=True,
    )


def render_metric_card(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="ie-metric-card">
            <div class="ie-metric-label">{escape(label)}</div>
            <div class="ie-metric-value">{escape(value)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_panel(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="ie-panel">
            <h3>{escape(title)}</h3>
            <p>{escape(body)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_trust_note() -> None:
    render_status(
        "IEIRAS combines environmental prediction, mapping, forecasting, explainability, reporting, ocean risk, and river water intelligence in one workflow."
    )


def render_footer() -> None:
    st.markdown(
        """
        <div class="ie-footer">
            <div class="ie-footer-grid">
                <div>
                    <h3>IEIRAS Impact</h3>
                    <p>
                        Intelligent Environmental Risk and Analytics System for AQI prediction,
                        rainfall monitoring, map intelligence, ocean risk, water pollution AI,
                        explainability, and report generation.
                    </p>
                </div>
                <div>
                    <h4>Workflow</h4>
                    <ul>
                        <li><a href="/Overview" target="_self">Overview</a></li>
                        <li><a href="/AI_Prediction" target="_self">Predict AQI</a></li>
                        <li><a href="/Map_AI_Prediction" target="_self">Map Intelligence</a></li>
                        <li><a href="/Water_Pollution_Prediction" target="_self">Water AI</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Credits</h4>
                    <p>Developed by Alok Singh<br>MSc AI and Data Science</p>
                </div>
            </div>
            <div class="ie-footer-note">
                Academic environmental intelligence dashboard for demonstration and decision-support use.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
