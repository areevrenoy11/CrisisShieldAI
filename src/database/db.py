import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "analyses.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            message_hash  TEXT UNIQUE,
            message_text  TEXT,
            source        TEXT,
            analyst       TEXT,
            result_json   TEXT,
            risk_score    REAL,
            risk_level    TEXT,
            submitted_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_analysis(message_hash, message_text, source, analyst, result):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        INSERT OR REPLACE INTO analyses
            (message_hash, message_text, source, analyst, result_json, risk_score, risk_level)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        message_hash,
        message_text,
        source or "—",
        analyst or "—",
        json.dumps(result),
        result["final_decision"]["risk_score"],
        result["final_decision"]["risk_level"],
    ))
    conn.commit()
    conn.close()


def get_by_hash(message_hash):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT result_json FROM analyses WHERE message_hash = ?",
        (message_hash,)
    ).fetchone()
    conn.close()
    return json.loads(row[0]) if row else None


def get_recent(limit=100):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT id, message_text, source, analyst, risk_score, risk_level, submitted_at
        FROM analyses
        ORDER BY submitted_at DESC
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()
    return rows


def get_full_by_id(analysis_id):
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT result_json, message_text, source, analyst, submitted_at FROM analyses WHERE id = ?",
        (analysis_id,)
    ).fetchone()
    conn.close()
    if row:
        return {
            "result": json.loads(row[0]),
            "message_text": row[1],
            "source": row[2],
            "analyst": row[3],
            "submitted_at": row[4],
        }
    return None
