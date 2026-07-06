import re

PANIC_WORDS = {
    "dead", "death", "explosion", "collapse", "terror", "riot",
    "attack", "bomb", "flood", "fire", "earthquake", "tsunami",
    "trapped", "missing", "casualties", "injured", "killed",
    "destroyed", "wiped out", "massacre",
}


def check_panic(text):
    count = sum(bool(re.search(rf"\b{w}\b", text)) for w in PANIC_WORDS)
    if count >= 2:
        return 25, "Multiple panic-inducing terms"
    if count:
        return 15, "Panic-inducing language"
    return 0, None
