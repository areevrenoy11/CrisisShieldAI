import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd
import io

from src.main_pipeline import CrisisShieldPipeline

st.set_page_config(page_title="Bulk Upload — CrisisShieldAI", layout="wide", page_icon="📁")

css_file = ROOT / "app" / "assets" / "style.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📁 Bulk Message Analysis")
st.caption("Upload a CSV with a `message` column. Results are returned as a scored table.")

st.info("**Fast Mode is on by default** — uses Rules + ML only, no Gemini calls. Cached messages always return instantly regardless of mode.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

col1, col2 = st.columns(2)
with col1:
    analyst = st.text_input("👤 Analyst Name", placeholder="Optional")
with col2:
    source = st.text_input("📌 Source", placeholder="Optional")

fast_mode = st.toggle("Fast Mode (no LLM)", value=True)

if uploaded:
    df = pd.read_csv(uploaded)

    if "message" not in df.columns:
        st.error("CSV must have a column named `message`.")
        st.stop()

    st.markdown(f"**{len(df)} messages loaded.** Click Analyze to process.")

    if st.button("🚀 Analyze All", use_container_width=True):
        pipeline = CrisisShieldPipeline()
        results = []
        progress = st.progress(0)
        status = st.empty()

        for i, row in enumerate(df["message"]):
            status.caption(f"Processing {i+1} / {len(df)}…")
            try:
                r = pipeline.run(str(row), source=source, analyst=analyst, fast=fast_mode)
                final = r["final_decision"]
                results.append({
                    "message": str(row)[:100],
                    "risk_level": final.get("risk_level", "—"),
                    "risk_score": round(final.get("risk_score", 0)),
                    "rule_score": r["rule_engine"].get("rule_score", 0),
                    "ml_confidence": r["machine_learning"].get("confidence", 0),
                    "claim": final.get("claim", "—"),
                    "location": final.get("location", "—"),
                    "cached": "⚡" if r.get("cached") else "",
                })
            except Exception as e:
                results.append({"message": str(row)[:100], "risk_level": "ERROR", "risk_score": 0,
                                 "rule_score": 0, "ml_confidence": 0, "claim": str(e),
                                 "location": "—", "cached": ""})
            progress.progress((i + 1) / len(df))

        status.empty()
        progress.empty()

        result_df = pd.DataFrame(results)

        def colour_row(row):
            colours = {"HIGH": "background-color: #3d1a1a", "MEDIUM": "background-color: #3d2e10", "LOW": "background-color: #1a3d1a"}
            return [colours.get(row["risk_level"], "")] * len(row)

        st.dataframe(result_df.style.apply(colour_row, axis=1), use_container_width=True)

        csv_out = result_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Results CSV", csv_out, "crisisai_results.csv", "text/csv", use_container_width=True)

else:
    st.markdown("""
**Expected CSV format:**
```
message
BREAKING!! Bhakra Dam has collapsed...
National Center for Seismology confirms...
Heard from someone that the highway is blocked...
```
""")
