"""
CrisisShieldAI
Main Enterprise Pipeline
"""

from src.preprocessing.cleaner import TextCleaner
from src.rules.rule_engine import RuleEngine
from src.ml.predict import MLPredictor
from src.llm.analyzer import GeminiAnalyzer
from src.fusion.decision_fusion import DecisionFusion


class CrisisShieldPipeline:

    def __init__(self):

        self.cleaner = TextCleaner()
        self.rule_engine = RuleEngine()
        self.ml = MLPredictor()
        self.llm = GeminiAnalyzer()
        self.fusion = DecisionFusion()

    def run(self, message: str):

        # -------------------------
        # Step 1
        # -------------------------

        cleaned_text = self.cleaner.clean(message)

        # -------------------------
        # Step 2
        # -------------------------

        rule_result = self.rule_engine.analyze(
            message,
            cleaned_text
        )

        # -------------------------
        # Step 3
        # -------------------------

        ml_result = self.ml.predict(cleaned_text)

        # -------------------------
        # Step 4
        # -------------------------

        llm_result = self.llm.analyze(message)

        # -------------------------
        # Step 5
        # -------------------------

        urgency_map = {
            "LOW": 30,
            "MEDIUM": 60,
            "HIGH": 90,
            "CRITICAL": 100
        }

        llm_score = urgency_map.get(
            llm_result.get("urgency", "LOW").upper(),
            50
        )

        # -------------------------
        # Step 6
        # -------------------------

        final_report = self.fusion.fuse(

            rule_score=rule_result["rule_score"],

            ml_probability=ml_result["confidence"],

            llm_score=llm_score,

            llm_result=llm_result

        )

        # -------------------------
        # Complete Report
        # -------------------------

        return {

            "cleaned_text": cleaned_text,

            "rule_engine": rule_result,

            "machine_learning": ml_result,

            "llm_analysis": llm_result,

            "final_decision": final_report

        }


if __name__ == "__main__":

    pipeline = CrisisShieldPipeline()

    sample = """
    BREAKING!!

    Mumbai Dam has collapsed.

    Forward immediately!!

    """

    result = pipeline.run(sample)

    from pprint import pprint

    pprint(result)