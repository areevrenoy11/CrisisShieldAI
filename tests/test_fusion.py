from src.fusion.decision_fusion import DecisionFusion

fusion = DecisionFusion()

result = fusion.fuse(
    rule_score=70,
    ml_probability=82,
    llm_score=90,
    llm_result={
        "claim":"Mumbai Dam has collapsed",

        "event_type":"Dam Collapse",

        "location":"Mumbai",

        "missing_information":[
            "Official source"
        ],

        "recommended_action":
            "Verify before forwarding.",

        "safe_response":
            "Please verify from official sources."
    }
)

print(result)