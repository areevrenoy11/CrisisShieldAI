import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import streamlit as st
from src.database import get_recent, get_full_by_id

st.set_page_config(page_title="Newsroom Feed — CrisisShieldAI", layout="wide", page_icon="📋")

css_file = ROOT / "app" / "assets" / "style.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📋 Newsroom Feed")
st.caption("All past analyses — most recent first")

LEVEL_COLOURS = {"HIGH": "🔴", "MEDIUM": "🟠", "LOW": "🟢"}

filter_col, _ = st.columns([1, 3])
with filter_col:
    level_filter = st.selectbox("Filter by risk", ["All", "HIGH", "MEDIUM", "LOW"])

rows = get_recent(limit=100)

if not rows:
    st.info("No analyses yet. Submit a message on the main page.")
    st.stop()

if level_filter != "All":
    rows = [r for r in rows if r[5] == level_filter]

for row in rows:
    analysis_id, message_text, source, analyst, risk_score, risk_level, submitted_at = row
    badge = LEVEL_COLOURS.get(risk_level, "⚪")
    snippet = message_text[:120] + "…" if len(message_text) > 120 else message_text

    with st.expander(f"{badge} **{risk_level}** — {round(risk_score)}%  |  {submitted_at[:16]}  |  {analyst}  |  {source}"):
        st.caption(f"**Message:** {snippet}")

        detail = get_full_by_id(analysis_id)
        if detail:
            r = detail["result"]
            final = r.get("final_decision", {})
            llm = r.get("llm_analysis", {})
            rules = r.get("rule_engine", {})

            d1, d2, d3 = st.columns(3)
            with d1:
                st.metric("Risk Score", f"{round(risk_score)}%")
                st.metric("ML Confidence", f"{r.get('machine_learning', {}).get('confidence', '—')}%")
            with d2:
                st.metric("Rule Score", f"{rules.get('rule_score', '—')} / 100")
                st.markdown(f"**Event** `{llm.get('event_type', '—')}`")
                st.markdown(f"**Location** `{final.get('location', '—')}`")
            with d3:
                st.markdown(f"**Claim:** {final.get('claim', '—')}")
                triggered = rules.get("triggered_rules", [])
                if triggered:
                    for t in triggered:
                        st.caption(f"⚡ {t}")
