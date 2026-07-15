"""
CrisisShieldAI — REST API
Run with: python -m uvicorn api.server:app --port 8502 --reload
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi import FastAPI
from pydantic import BaseModel
from src.main_pipeline import CrisisShieldPipeline
from src.database import get_recent, get_full_by_id

app = FastAPI(title="CrisisShieldAI API", version="1.0")
pipeline = CrisisShieldPipeline()


class AnalyzeRequest(BaseModel):
    message: str
    source: str = ""
    analyst: str = ""
    fast: bool = False


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    result = pipeline.run(req.message, source=req.source, analyst=req.analyst, fast=req.fast)
    return result


@app.get("/api/history")
def history(limit: int = 50):
    rows = get_recent(limit=limit)
    return [
        {
            "id": r[0],
            "message_snippet": r[1][:120],
            "source": r[2],
            "analyst": r[3],
            "risk_score": r[4],
            "risk_level": r[5],
            "submitted_at": r[6],
        }
        for r in rows
    ]


@app.get("/api/history/{analysis_id}")
def history_detail(analysis_id: int):
    return get_full_by_id(analysis_id)


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "CrisisShieldAI"}
