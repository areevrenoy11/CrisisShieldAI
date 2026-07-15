import re
from src.rules.checks.utils import is_negated

URGENCY_WORDS = {
    "urgent", "immediately", "emergency", "alert", "breaking",
    "evacuate", "warning", "danger", "crisis", "critical",
    "disaster", "now", "asap", "hurry", "quickly",
}


def check_urgency(text):
    count = 0
    for w in URGENCY_WORDS:
        m = re.search(rf"\b{w}\b", text)
        if m and not is_negated(text, m.start()):
            count += 1
    if count >= 3:
        return 30, "Multiple urgency words detected"
    if count:
        return 15, "Urgency language detected"
    return 0, None
