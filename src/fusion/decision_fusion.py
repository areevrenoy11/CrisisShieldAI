"""
CrisisShieldAI
Decision Fusion Engine

Combines outputs from:
1. Rule Engine
2. Machine Learning Model
3. Gemini LLM

Produces one final enterprise risk assessment.
"""


class DecisionFusion:

    def __init__(self):

        # Weight assigned to each AI component
        self.rule_weight = 0.30
        self.ml_weight = 0.35
        self.llm_weight = 0.35

    def fuse(
        self,
        rule_score,
        ml_probability,
        llm_score,
        llm_result
    ):
        """
        Combine all scores into one final decision.

        Parameters
        ----------
        rule_score : float
            Score from Rule Engine (0-100)

        ml_probability : float
            Confidence from ML model (0-100)

        llm_score : float
            Urgency score from Gemini (0-100)

        llm_result : dict
            Structured JSON returned by Gemini
        """

        # Final weighted score
        final_score = (
            (rule_score * self.rule_weight)
            + (ml_probability * self.ml_weight)
            + (llm_score * self.llm_weight)
        )

        # Decide Risk Level
        if final_score >= 80:
            risk = "HIGH"

        elif final_score >= 50:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        # Final Enterprise Report
        return {

            "risk_score": round(final_score, 2),

            "risk_level": risk,

            "claim": llm_result.get("claim", ""),

            "event_type": llm_result.get("event_type", ""),

            "location": llm_result.get("location", ""),

            "missing_information": llm_result.get(
                "missing_information",
                []
            ),

            "recommended_action": llm_result.get(
                "recommended_action",
                "Verify the information before sharing."
            ),

            "safe_response": llm_result.get(
                "safe_response",
                "Please verify this information using trusted official sources before forwarding."
            ),

            "component_scores": {
                "rule_engine": round(rule_score, 2),
                "machine_learning": round(ml_probability, 2),
                "gemini_llm": round(llm_score, 2)
            }

        }


if __name__ == "__main__":

    fusion = DecisionFusion()

    sample_llm = {
        "claim": "Mumbai Dam has collapsed",
        "event_type": "Infrastructure Failure",
        "location": "Mumbai",
        "missing_information": [
            "Official source",
            "Time of incident"
        ],
        "recommended_action":
            "Verify through NDMA or local authorities.",
        "safe_response":
            "Do not forward until official confirmation."
    }

    result = fusion.fuse(
        rule_score=70,
        ml_probability=82,
        llm_score=90,
        llm_result=sample_llm
    )

    from pprint import pprint
    pprint(result)