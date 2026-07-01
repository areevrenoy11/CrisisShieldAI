from src.rules.checks.urgency import check_urgency
from src.rules.checks.panic import check_panic
from src.rules.checks.forwarding import check_forwarding
from src.rules.checks.capitalization import check_caps
from src.rules.checks.punctuation import check_exclamation


class RuleEngine:

    def analyze(self, original_text: str, cleaned_text: str):

        score = 0
        triggered = []

        checks = [
            check_urgency(cleaned_text),
            check_panic(cleaned_text),
            check_forwarding(cleaned_text),
            check_caps(original_text),
            check_exclamation(original_text),
        ]

        for points, rule in checks:

            score += points

            if rule:
                triggered.append(rule)

        score = min(score, 100)

        if score < 30:
            level = "LOW"
        elif score < 60:
            level = "MEDIUM"
        elif score < 80:
            level = "HIGH"
        else:
            level = "CRITICAL"

        return {
            "rule_score": score,
            "risk_level": level,
            "triggered_rules": triggered,
        }