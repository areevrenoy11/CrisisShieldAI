URGENCY_WORDS = {
    "urgent",
    "immediately",
    "emergency",
    "alert",
    "breaking",
    "evacuate",
    "warning",
}


def check_urgency(text):
    count = sum(word in text for word in URGENCY_WORDS)

    if count:
        return 25, "Urgency words detected"

    return 0, None