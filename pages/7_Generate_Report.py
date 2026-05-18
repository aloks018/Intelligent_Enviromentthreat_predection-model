import sys
from pathlib import Path

import streamlit as st
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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


st.set_page_config(page_title="Report | IEIRAS", page_icon="IE", layout="wide")
inject_natgeo_theme()
render_topbar("Report")

render_hero(
    title="Environmental Impact Report",
    summary=(
        "Generate a downloadable PDF report with system metadata, model context, "
        "risk summary, business impact context, and project information for review or presentation."
    ),
    image="https://images.unsplash.com/photo-1486825586573-7131f7991bdd?auto=format&fit=crop&w=2400&q=90",
    kicker="PDF generation",
    meta="Local report output",
)

render_section(
    "Generate report",
    "Output",
    "Create the PDF below and download it for review, presentation, or archive.",
)
render_panel(
    "Transparency note",
    "The PDF is generated locally in this project folder and then offered as a Streamlit download.",
)

report_title = st.text_input("Report title", "IEIRAS Environmental Intelligence Report")
author = st.text_input("Prepared by", "Alok Singh")
summary = st.text_area(
    "Summary",
    "IEIRAS integrates AQI prediction, map intelligence, forecasting, business impact scoring, ocean risk, and water pollution AI.",
)

if st.button("Generate Report"):
    file_path = ROOT_DIR / "Environmental_Report.pdf"
    doc = SimpleDocTemplate(str(file_path))
    styles = getSampleStyleSheet()
    elements = [
        Paragraph(report_title, styles["Title"]),
        Spacer(1, 0.35 * inch),
        Paragraph(f"Prepared by: {author}", styles["Normal"]),
        Paragraph("System: IEIRAS Environmental Intelligence Dashboard", styles["Normal"]),
        Paragraph("Model Accuracy: Demonstration value 99.08%", styles["Normal"]),
        Paragraph("Risk Index: Dynamically computed from page-level tools", styles["Normal"]),
        Spacer(1, 0.25 * inch),
        Paragraph(summary, styles["BodyText"]),
    ]
    doc.build(elements)

    with open(file_path, "rb") as file:
        st.download_button(
            "Download PDF",
            file,
            file_name="Environmental_Report.pdf",
            mime="application/pdf",
        )

render_footer()
