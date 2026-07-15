import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import streamlit as st
import streamlit.components.v1 as components

from src.main_pipeline import CrisisShieldPipeline
from app.components import shield

pipeline = CrisisShieldPipeline()

PHI = 1.618

def run_pipeline(message: str, source: str = "", analyst: str = ""):
    return pipeline.run(message, source=source, analyst=analyst)

st.set_page_config(
    page_title="CrisisShieldAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_file = ROOT / "app" / "assets" / "style.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Clear any localStorage entry that cached a collapsed sidebar state
components.html("""
<script>
(function() {
    try {
        var keys = Object.keys(window.parent.localStorage);
        keys.forEach(function(k) {
            if (k.toLowerCase().includes('sidebar')) {
                window.parent.localStorage.removeItem(k);
            }
        });
    } catch(e) {}
})();
</script>
""", height=0)

DEMOS = {
    "🔴 High Risk — Dam Rumor": (
        "BREAKING!! Bhakra Dam has COLLAPSED. Entire downstream area flooding fast. "
        "Government hiding this. FORWARD TO EVERYONE IMMEDIATELY before they delete this!!"
    ),
    "🟠 Medium Risk — Unverified Tremors": (
        "Felt really strong tremors in Mandi around 2am last night. My whole building shook for "
        "like 30 seconds. Heard from neighbours that some houses cracked. No official news yet."
    ),
    "🟢 Low Risk — Official Report": (
        "National Center for Seismology confirms: Magnitude 4.2 earthquake recorded near Bhakra "
        "at 03:14 IST. No structural damage or casualties reported. Situation being monitored."
    ),
}

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
if "demo_message" not in st.session_state:
    st.session_state.demo_message = ""

with st.sidebar:
    st.title("🛡️ CrisisShieldAI")
    st.markdown("---")
    st.success("System Status")
    st.write("🟢 Hybrid AI Engine Online")
    st.write("🤖 Gemini Connected")
    st.write("🧠 ML Model Loaded")
    st.write("📚 Rule Engine Ready")
    st.markdown("---")
    st.subheader("🧪 Demo Messages")
    st.caption("Click to load into the analyzer")
    for label, text in DEMOS.items():
        if st.button(label, use_container_width=True):
            st.session_state.demo_message = text
    st.markdown("---")
    st.caption("Version 1.0")

# --------------------------------------------------
# Header  —  golden ratio: title (φ) | shield (1)
# --------------------------------------------------
h_left, h_right = st.columns([PHI, 1])

with h_left:
    st.title("🛡️ CrisisShieldAI")
    st.subheader("Hybrid AI Rumor Verification Platform")

with h_right:
    shield()

st.markdown("---")

# --------------------------------------------------
# Input
# --------------------------------------------------
message = st.text_area(
    "📩 Paste Crisis Message",
    value=st.session_state.demo_message,
    height=160,
    placeholder="Paste a forwarded WhatsApp message, tweet or news text..."
)

meta_left, meta_right = st.columns(2)
with meta_left:
    analyst = st.text_input("👤 Your Name", placeholder="Journalist / analyst name")
with meta_right:
    source = st.text_input("📌 Source", placeholder="WhatsApp group, Twitter, tip line…")

analyze = st.button("🚀 Analyze Message", use_container_width=True)

# --------------------------------------------------
# Analysis
# --------------------------------------------------
if analyze:
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        status = st.empty()
        status.info("Analyzing…")
        result = run_pipeline(message, source=source, analyst=analyst)
        if result.get("cached"):
            status.success("⚡ Instant result — cached from previous analysis")
        else:
            status.success("✅ Done")

        st.markdown("---")

        final = result["final_decision"]
        ml    = result["machine_learning"]
        llm   = result["llm_analysis"]
        rules = result["rule_engine"]
        score = final["risk_score"]

        # Top row — golden ratio: decision (φ) | verdict stats (1)
        res_left, res_right = st.columns([PHI, 1])

        with res_left:
            st.subheader("🎯 Final Decision")

            if score >= 80:
                st.error(f"🔴 HIGH RISK — {score}%")
            elif score >= 50:
                st.warning(f"🟠 MEDIUM RISK — {score}%")
            else:
                st.success(f"🟢 LOW RISK — {score}%")

            st.progress(score / 100)

            disagreement = final.get("engine_disagreement")
            if disagreement:
                st.warning(f"⚠️ **Engine Conflict:** {disagreement}")

            st.markdown("**📌 Claim**")
            st.info(final.get("claim", "—"))

            st.markdown("**🛡 Safe Response**")
            st.success(final.get("safe_response", final.get("recommended_action", "—")))

        with res_right:
            st.metric("ML Confidence", f"{ml['confidence']}%")
            st.metric("Rule Score", f"{rules.get('rule_score', 0)} / 100")
            st.metric("Urgency", llm.get("urgency", "—"))

        # Details row — two equal columns side by side
        st.markdown("---")
        st.subheader("📊 Details")
        det_left, det_right = st.columns(2)

        with det_left:
            with st.container(border=True):
                st.markdown("**⚡ Triggered Rules**")
                triggered = rules.get("triggered_rules", [])
                if triggered:
                    for t in triggered:
                        st.caption(f"⚡ {t}")
                else:
                    st.caption("✅ No rules triggered")

            with st.container(border=True):
                st.markdown(f"**Event** &nbsp; `{llm.get('event_type', '—')}`", unsafe_allow_html=True)
                st.markdown(f"**Location** &nbsp; `{final.get('location', '—')}`", unsafe_allow_html=True)
                st.markdown(f"**Source** &nbsp; `{llm.get('source_type', '—')}` {'✅' if llm.get('source_present') else '❌'}", unsafe_allow_html=True)

            rumor_flags = llm.get("rumor_indicators", [])
            if rumor_flags:
                with st.container(border=True):
                    st.markdown("**🚩 Rumor Signals**")
                    for item in rumor_flags:
                        st.caption(f"• {item}")

        with det_right:
            cred_flags = llm.get("credibility_indicators", [])
            with st.container(border=True):
                st.markdown("**✅ Credibility Signals**")
                if cred_flags:
                    for item in cred_flags:
                        st.caption(f"• {item}")
                else:
                    st.caption("—")

            missing = final.get("missing_information", [])
            with st.container(border=True):
                st.markdown("**⚠ Missing**")
                if missing:
                    for item in missing:
                        st.caption(f"• {item}")
                else:
                    st.caption("—")

        # Raw details  —  golden ratio: rule (1) | llm (φ)
        st.markdown("---")
        d_left, d_right = st.columns([1, PHI])

        with d_left:
            with st.expander("📚 Rule Engine"):
                st.json(rules)

        with d_right:
            with st.expander("🧠 LLM Output"):
                st.json(llm)
