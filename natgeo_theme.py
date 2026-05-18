from __future__ import annotations

import base64
from html import escape
from mimetypes import guess_type
from pathlib import Path

import streamlit as st


PAGES = [
    {"path": "app.py", "label": "Home", "route": "/"},
    {"path": "pages/1_Overview.py", "label": "Overview", "route": "/Overview"},
    {"path": "pages/2_AI_Prediction.py", "label": "Predict AQI", "route": "/AI_Prediction"},
    {"path": "pages/3_Map_AI_Prediction.py", "label": "Map", "route": "/Map_AI_Prediction"},
    {"path": "pages/4_Time_Series_Forecast.py", "label": "Forecast", "route": "/Time_Series_Forecast"},
    {"path": "pages/5_Model_Analytics.py", "label": "Analytics", "route": "/Model_Analytics"},
    {"path": "pages/6_Business_Impact.py", "label": "Business AI", "route": "/Business_Impact"},
    {"path": "pages/7_Generate_Report.py", "label": "Report", "route": "/Generate_Report"},
    {"path": "pages/8_Ocean_Ice_Threat.py", "label": "Ocean + Ice", "route": "/Ocean_Ice_Threat"},
    {"path": "pages/9_Water_Pollution_Prediction.py", "label": "Water AI", "route": "/Water_Pollution_Prediction"},
]

PRIMARY_NAV_LABELS = {"Home", "Predict AQI", "Map", "Business AI", "Water AI", "Report"}


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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        :root {
            --ie-ink: #0d1f1a;
            --ie-muted: #657a72;
            --ie-green: #0f5132;
            --ie-green-2: #166534;
            --ie-teal: #0b7285;
            --ie-cyan: #0ea5b7;
            --ie-mint: #e9f9ef;
            --ie-mist: #f3fbf7;
            --ie-line: #cfe7d8;
            --ie-white: #ffffff;
            --ie-shadow: 0 18px 44px rgba(14, 61, 45, 0.09);
            --ie-shadow-strong: 0 26px 60px rgba(10, 43, 34, 0.14);
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background:
                radial-gradient(circle at top left, rgba(15, 81, 50, 0.12), transparent 28rem),
                radial-gradient(circle at top right, rgba(14, 116, 144, 0.10), transparent 26rem),
                linear-gradient(180deg, #f9fcfb 0%, #f2faf7 52%, #fbfefd 100%);
            color: var(--ie-ink);
            font-family: "Inter", system-ui, sans-serif;
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
            padding-top: 1.1rem;
            padding-bottom: 2.2rem;
        }

        [data-testid="stSidebar"],
        [data-testid="stSidebarNav"] {
            display: none;
        }

        .ie-topbar {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(207, 231, 216, 0.95);
            border-radius: 8px;
            box-shadow: var(--ie-shadow);
            margin-bottom: 1rem;
            padding: 0.95rem 1rem;
            position: sticky;
            top: 0.65rem;
            z-index: 20;
            backdrop-filter: blur(14px);
        }

        .ie-topbar-main {
            align-items: center;
            display: grid;
            gap: 0.9rem;
            grid-template-columns: minmax(230px, 320px) minmax(0, 1fr);
        }

        .ie-brand {
            align-items: center;
            display: flex;
            gap: 0.82rem;
            min-width: 0;
        }

        .ie-logo {
            align-items: center;
            background: linear-gradient(145deg, #0f5132, #0ea5b7);
            border-radius: 8px;
            box-shadow: 0 18px 34px rgba(11, 114, 133, 0.18);
            color: #ffffff;
            display: flex;
            flex: 0 0 auto;
            font-size: 0.92rem;
            font-weight: 900;
            height: 52px;
            justify-content: center;
            position: relative;
            width: 62px;
        }

        .ie-logo::after {
            content: "";
            position: absolute;
            inset: 7px;
            border: 1px solid rgba(255, 255, 255, 0.24);
            border-radius: 8px;
        }

        .ie-brand-copy {
            min-width: 0;
        }

        .ie-brand-kicker {
            color: var(--ie-teal);
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.18em;
            text-transform: uppercase;
        }

        .ie-brand-title {
            color: var(--ie-ink);
            font-size: 1.22rem;
            font-weight: 900;
            line-height: 1.1;
            margin-top: 0.18rem;
            text-transform: uppercase;
        }

        .ie-brand-subtitle {
            color: var(--ie-muted);
            font-size: 0.79rem;
            font-weight: 600;
            line-height: 1.45;
            margin-top: 0.18rem;
        }

        .ie-nav {
            align-items: center;
            display: flex;
            flex-wrap: wrap;
            gap: 0.46rem;
            justify-content: flex-end;
            min-width: 0;
        }

        .ie-nav a,
        .ie-nav span {
            border-radius: 999px;
            display: inline-flex;
            font-size: 0.73rem;
            font-weight: 800;
            line-height: 1;
            padding: 0.6rem 0.82rem;
            text-decoration: none;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .ie-nav span {
            background: var(--ie-mint);
            color: var(--ie-green);
        }

        .ie-nav a {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid var(--ie-line);
            color: var(--ie-ink);
        }

        .ie-nav .ie-nav-primary {
            background: linear-gradient(135deg, var(--ie-green), var(--ie-teal));
            border-color: transparent;
            color: #ffffff;
            box-shadow: 0 14px 28px rgba(11, 114, 133, 0.15);
        }

        .ie-flowbar {
            align-items: center;
            border-top: 1px solid rgba(207, 231, 216, 0.9);
            display: flex;
            flex-wrap: wrap;
            gap: 0.48rem;
            margin-top: 0.9rem;
            padding-top: 0.9rem;
        }

        .ie-flowbar-label {
            color: var(--ie-muted);
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.18em;
            margin-right: 0.2rem;
            text-transform: uppercase;
        }

        .ie-flowbar a,
        .ie-flowbar span {
            border-radius: 999px;
            display: inline-flex;
            font-size: 0.75rem;
            font-weight: 700;
            line-height: 1;
            padding: 0.55rem 0.8rem;
            text-decoration: none;
            white-space: nowrap;
        }

        .ie-flowbar a {
            background: #ffffff;
            border: 1px solid rgba(207, 231, 216, 0.95);
            color: var(--ie-muted);
        }

        .ie-flowbar span {
            background: linear-gradient(135deg, var(--ie-mint), #f4fcf7);
            border: 1px solid rgba(180, 230, 201, 0.95);
            color: var(--ie-green);
        }

        .ie-hero {
            background-position: center;
            background-size: cover;
            border-radius: 8px;
            box-shadow: var(--ie-shadow-strong);
            min-height: 470px;
            overflow: hidden;
            position: relative;
        }

        .ie-hero::before {
            background: linear-gradient(94deg, rgba(10, 49, 36, 0.93), rgba(11, 114, 133, 0.66), rgba(10, 49, 36, 0.16));
            content: "";
            inset: 0;
            position: absolute;
        }

        .ie-hero-body {
            color: #ffffff;
            max-width: 790px;
            padding: 4.7rem 2.4rem 2.5rem 2.4rem;
            position: relative;
            z-index: 1;
        }

        .ie-kicker,
        .ie-card-kicker,
        .ie-section-kicker {
            color: #c6f6da;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        .ie-hero h1 {
            color: #ffffff;
            font-size: 3.25rem;
            font-weight: 900;
            line-height: 1.02;
            margin: 0.82rem 0 1rem 0;
            max-width: 780px;
        }

        .ie-hero p {
            color: rgba(255, 255, 255, 0.93);
            font-size: 1.03rem;
            line-height: 1.74;
            margin: 0;
            max-width: 720px;
        }

        .ie-hero-meta {
            background: rgba(255, 255, 255, 0.14);
            border: 1px solid rgba(255, 255, 255, 0.28);
            border-radius: 999px;
            color: #ffffff;
            display: inline-block;
            font-size: 0.76rem;
            font-weight: 800;
            margin-top: 1.15rem;
            padding: 0.66rem 0.92rem;
            text-transform: uppercase;
        }

        .ie-section {
            margin-top: 1.6rem;
        }

        .ie-section-head {
            align-items: end;
            display: grid;
            gap: 1rem;
            grid-template-columns: minmax(0, 0.92fr) minmax(0, 1.08fr);
            margin-bottom: 1rem;
        }

        .ie-section-title {
            color: var(--ie-ink);
            font-size: 2rem;
            font-weight: 900;
            line-height: 1.12;
            margin: 0.28rem 0 0 0;
        }

        .ie-section-copy {
            color: var(--ie-muted);
            font-size: 0.98rem;
            line-height: 1.7;
            margin: 0;
        }

        .ie-card,
        .ie-photo-card,
        .ie-metric-card,
        .ie-panel,
        .kpi-card,
        div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(207, 231, 216, 0.95);
            border-radius: 8px;
            box-shadow: var(--ie-shadow);
            overflow: hidden;
        }

        .ie-card,
        .ie-panel,
        .kpi-card {
            padding: 1.02rem;
        }

        .ie-card,
        .kpi-card,
        .ie-metric-card {
            border-top: 5px solid rgba(15, 81, 50, 0.92);
        }

        .ie-card h3,
        .ie-panel h3,
        .ie-photo-title {
            color: var(--ie-ink);
            font-size: 1.08rem;
            font-weight: 800;
            line-height: 1.34;
            margin: 0.42rem 0;
        }

        .ie-card p,
        .ie-panel p,
        .ie-photo-copy {
            color: var(--ie-muted);
            line-height: 1.6;
            margin: 0.35rem 0 0 0;
        }

        .ie-panel {
            min-height: 126px;
        }

        .ie-status {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, var(--ie-mint) 100%);
            border: 1px solid rgba(207, 231, 216, 0.95);
            border-left: 6px solid var(--ie-teal);
            border-radius: 8px;
            color: var(--ie-ink);
            font-size: 0.95rem;
            font-weight: 700;
            margin: 1rem 0 0 0;
            padding: 0.92rem 1rem;
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
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }

        .ie-metric-value,
        div[data-testid="stMetricValue"] {
            color: var(--ie-green);
            font-size: 1.78rem;
            font-weight: 900;
            margin-top: 0.28rem;
        }

        div[data-testid="stMetric"] {
            padding: 0.95rem;
        }

        div[data-testid="stMetric"] > div {
            color: var(--ie-muted);
        }

        .stButton > button,
        .stDownloadButton > button {
            background: linear-gradient(135deg, var(--ie-green), var(--ie-teal));
            border: 1px solid transparent;
            border-radius: 8px;
            box-shadow: 0 14px 26px rgba(11, 114, 133, 0.16);
            color: #ffffff;
            font-weight: 800;
            min-height: 2.8rem;
            text-transform: uppercase;
            width: 100%;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background: linear-gradient(135deg, var(--ie-green-2), var(--ie-cyan));
            color: #ffffff;
        }

        .stSelectbox [data-baseweb="select"] > div,
        .stNumberInput input,
        .stTextInput input,
        .stTextArea textarea,
        div[data-testid="stSlider"] {
            border-radius: 8px;
        }

        .stSelectbox [data-baseweb="select"] > div,
        .stNumberInput input,
        .stTextInput input,
        .stTextArea textarea {
            border: 1px solid rgba(207, 231, 216, 0.95);
            box-shadow: var(--ie-shadow);
        }

        div[data-testid="stSlider"] {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(207, 231, 216, 0.95);
            padding: 0.8rem 0.9rem;
        }

        div[data-testid="stImage"] img {
            border-radius: 8px;
        }

        .ie-footer {
            background: linear-gradient(135deg, #10382b 0%, #0e5f4e 50%, #0b7285 100%);
            border-radius: 8px;
            box-shadow: var(--ie-shadow-strong);
            color: #ffffff;
            margin-top: 1.9rem;
            padding: 1.4rem;
        }

        .ie-footer-grid {
            display: grid;
            gap: 1.2rem;
            grid-template-columns: 1.25fr 1fr 1fr;
        }

        .ie-footer h3,
        .ie-footer h4 {
            color: #ffffff;
            font-weight: 800;
            margin: 0 0 0.55rem 0;
        }

        .ie-footer p,
        .ie-footer a,
        .ie-footer li {
            color: rgba(233, 248, 238, 0.95);
            line-height: 1.62;
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
            color: rgba(233, 248, 238, 0.95);
            font-size: 0.86rem;
            margin-top: 1rem;
            padding-top: 0.85rem;
        }

        @media (max-width: 1080px) {
            .ie-topbar-main,
            .ie-section-head,
            .ie-footer-grid {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
            }

            .ie-nav {
                justify-content: flex-start;
                width: 100%;
            }
        }

        @media (max-width: 720px) {
            .block-container {
                padding-top: 0.85rem;
            }

            .ie-topbar {
                padding: 0.82rem;
            }

            .ie-logo {
                height: 44px;
                width: 52px;
            }

            .ie-brand-title {
                font-size: 1.02rem;
            }

            .ie-nav a,
            .ie-nav span,
            .ie-flowbar a,
            .ie-flowbar span {
                font-size: 0.68rem;
                padding: 0.5rem 0.68rem;
            }

            .ie-hero {
                min-height: 400px;
            }

            .ie-hero-body {
                padding: 3.2rem 1.2rem 1.8rem 1.2rem;
            }

            .ie-hero h1 {
                font-size: 2.18rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_topbar(active: str = "Environment") -> None:
    primary_links = []
    workflow_links = []
    for page in PAGES:
        href = page["route"]
        label = str(page["label"])
        if label == active:
            workflow_links.append(f"<span>{escape(label)}</span>")
        else:
            workflow_links.append(f'<a href="{escape(href)}" target="_self">{escape(label)}</a>')

        if label in PRIMARY_NAV_LABELS and label != active:
            primary_class = ' class="ie-nav-primary"' if label == "Business AI" else ""
            primary_links.append(f'<a{primary_class} href="{escape(href)}" target="_self">{escape(label)}</a>')

    st.markdown(
        f"""
        <div class="ie-topbar">
            <div class="ie-topbar-main">
                <div class="ie-brand">
                    <div class="ie-logo">IE</div>
                    <div class="ie-brand-copy">
                        <div class="ie-brand-kicker">Environmental AI Suite</div>
                        <div class="ie-brand-title">IEIRAS Impact</div>
                        <div class="ie-brand-subtitle">Professional climate, AQI, business risk, map, and water intelligence dashboard</div>
                    </div>
                </div>
                <div class="ie-nav">
                    <span>{escape(active)}</span>
                    {''.join(primary_links)}
                </div>
            </div>
            <div class="ie-flowbar">
                <div class="ie-flowbar-label">Connected Pages</div>
                {''.join(workflow_links)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_links() -> None:
    st.markdown('<div class="ie-linkbar">', unsafe_allow_html=True)
    max_per_row = 5
    page_links = [(page["path"], page["label"]) for page in PAGES]
    for start in range(0, len(page_links), max_per_row):
        row = page_links[start : start + max_per_row]
        columns = st.columns(len(row))
        for column, (page_path, label) in zip(columns, row):
            with column:
                st.page_link(page_path, label=label)
    st.markdown("</div>", unsafe_allow_html=True)


def render_cta_links() -> None:
    st.markdown('<div class="ie-status">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.page_link("pages/2_AI_Prediction.py", label="Predict AQI")
    with c2:
        st.page_link("pages/3_Map_AI_Prediction.py", label="Open Map")
    with c3:
        st.page_link("pages/6_Business_Impact.py", label="Open Business AI")
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
        "IEIRAS connects AQI prediction, rainfall forecasting, map intelligence, business impact scoring, reporting, ocean risk, and river water analytics in one workflow."
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
                        rainfall monitoring, business impact scoring, map intelligence, ocean risk,
                        water pollution AI, and report generation.
                    </p>
                </div>
                <div>
                    <h4>Workflow</h4>
                    <ul>
                        <li><a href="/Overview" target="_self">Overview</a></li>
                        <li><a href="/AI_Prediction" target="_self">Predict AQI</a></li>
                        <li><a href="/Map_AI_Prediction" target="_self">Map Intelligence</a></li>
                        <li><a href="/Business_Impact" target="_self">Business AI</a></li>
                        <li><a href="/Generate_Report" target="_self">Report</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Project Identity</h4>
                    <p>Developed by Alok Singh<br />MSc AI and Data Science<br />Environmental Intelligence Platform</p>
                </div>
            </div>
            <div class="ie-footer-note">
                Professional environmental dashboard for demonstration, planning, and early decision-support use.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
