import re

URGENCY_WORDS = {
    "urgent", "immediately", "emergency", "alert", "breaking",
    "evacuate", "warning", "danger", "crisis", "critical",
    "disaster", "now", "asap", "hurry", "quickly",
}


def check_urgency(text):
    count = sum(bool(re.search(rf"\b{w}\b", text)) for w in URGENCY_WORDS)
    if count >= 3:
        return 30, "Multiple urgency words detected"
    if count:
        return 15, "Urgency language detected"
    return 0, None
