"""
CrisisShieldAI — Main Enterprise Pipeline
"""

import hashlib

from src.preprocessing.cleaner import TextCleaner
from src.rules.rule_engine import RuleEngine
from src.ml.predict import MLPredictor
from src.llm.analyzer import LLMAnalyzer, _FALLBACK
from src.fusion.decision_fusion import DecisionFusion
from src.database import init_db, get_by_hash, save_analysis

init_db()

URGENCY_MAP = {"LOW": 30, "MEDIUM": 60, "HIGH": 90, "CRITICAL": 100}


def _hash(message: str) -> str:
    return hashlib.sha256(message.strip().lower().encode()).hexdigest()


class CrisisShieldPipeline:

    def __init__(self):
        self.cleaner = TextCleaner()
        self.rule_engine = RuleEngine()
        self.ml = MLPredictor()
        self.llm = LLMAnalyzer()
        self.fusion = DecisionFusion()

    def run(self, message: str, source: str = "", analyst: str = "", fast: bool = False):
        key = _hash(message)

        cached = get_by_hash(key)
        if cached:
            cached["cached"] = True
            return cached

        cleaned = self.cleaner.clean(message)
        rule_result = self.rule_engine.analyze(message, cleaned)
        ml_result = self.ml.predict(cleaned)

        if fast:
            llm_result = {**_FALLBACK, "urgency": "LOW"}
            # fuse with rule + ML only, equal weights
            llm_score = ml_result["confidence"]
        else:
            llm_result = self.llm.analyze(message)
            llm_score = URGENCY_MAP.get(llm_result.get("urgency", "LOW").upper(), 50)

        final_report = self.fusion.fuse(
            rule_score=rule_result["rule_score"],
            ml_probability=ml_result["confidence"],
            llm_score=llm_score,
            llm_result=llm_result,
        )

        result = {
            "cleaned_text": cleaned,
            "rule_engine": rule_result,
            "machine_learning": ml_result,
            "llm_analysis": llm_result,
            "final_decision": final_report,
            "fast_mode": fast,
            "cached": False,
        }

        save_analysis(key, message, source, analyst, result)
        return result
