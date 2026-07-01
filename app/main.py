import sys
import time
from pathlib import Path

# ---------------------------------
# Fix Python Path
# ---------------------------------
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# ---------------------------------
# Imports
# ---------------------------------
import streamlit as st

from src.main_pipeline import CrisisShieldPipeline
from app.components import shield, loading

# ---------------------------------
# Initialize Pipeline
# ---------------------------------
pipeline = CrisisShieldPipeline()

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="CrisisShieldAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# Load CSS
# ---------------------------------
css_file = ROOT / "app" / "assets" / "style.css"

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:

    st.title("🛡️ CrisisShieldAI")

    st.markdown("---")

    st.success("System Status")

    st.write("🟢 Hybrid AI Engine Online")

    st.write("🤖 Gemini Connected")

    st.write("🧠 ML Model Loaded")

    st.write("📚 Rule Engine Ready")

    st.markdown("---")

    st.caption("Version 1.0")

# ---------------------------------
# Header
# ---------------------------------
left, right = st.columns([3, 1])

with left:

    st.title("🛡️ CrisisShieldAI")

    st.subheader(
        "Enterprise Hybrid AI Rumor Verification Platform"
    )

    st.write(
        """
        Detect crisis rumors using a Hybrid AI Engine combining:

        • Rule-Based Analysis

        • Machine Learning

        • Gemini AI

        • Decision Fusion
        """
    )

with right:

    shield()

# ---------------------------------
# Input
# ---------------------------------

st.markdown("---")

message = st.text_area(
    "📩 Paste Crisis Message",
    height=220,
    placeholder="Paste a forwarded WhatsApp message, tweet or news text..."
)

# ---------------------------------
# Analyze Button
# ---------------------------------

if st.button("🚀 Analyze Message", use_container_width=True):

    if not message.strip():

        st.warning("Please enter a message.")

    else:

        status = st.empty()

        status.info("🧹 Cleaning message...")
        time.sleep(0.5)

        status.info("📚 Running Rule Engine...")
        time.sleep(0.5)

        status.info("🤖 Running Machine Learning...")
        time.sleep(0.5)

        status.info("🧠 Consulting Gemini AI...")
        loading()

        result = pipeline.run(message)

        status.success("✅ Analysis Complete")

        st.markdown("---")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🧹 Rule Engine",
                "🤖 ML Model",
                "🧠 Gemini AI",
                "🎯 Final Decision"
            ]
        )

        # -----------------------------
        # Rule Engine
        # -----------------------------

        with tab1:

            st.subheader("Rule Engine Analysis")

            st.json(result["rule_engine"])

        # -----------------------------
        # ML
        # -----------------------------

        with tab2:

            st.subheader("Machine Learning")

            st.metric(
                "Confidence",
                f'{result["machine_learning"]["confidence"]}%'
            )

            st.json(result["machine_learning"])

        # -----------------------------
        # Gemini
        # -----------------------------

        with tab3:

            st.subheader("Gemini AI")

            st.json(result["llm_analysis"])

        # -----------------------------
        # Final Decision
        # -----------------------------

        with tab4:

            final = result["final_decision"]

            score = final["risk_score"]

            st.metric(
                "Final Risk Score",
                f"{score}%"
            )

            if score >= 80:
                st.error("🔴 HIGH RISK")

            elif score >= 50:
                st.warning("🟠 MEDIUM RISK")

            else:
                st.success("🟢 LOW RISK")

            st.markdown("### 📌 Claim")

            st.info(final["claim"])

            st.markdown("### 📍 Location")

            st.write(final["location"])

            st.markdown("### ⚠ Missing Information")

            for item in final["missing_information"]:
                st.write("•", item)

            st.markdown("### ✅ Recommended Action")

            st.success(final["recommended_action"])

            st.markdown("### 🛡 Safe Response")

            st.info(final["safe_response"])