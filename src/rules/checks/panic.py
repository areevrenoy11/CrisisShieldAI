import re
from src.rules.checks.utils import is_negated

PANIC_WORDS = {
    "dead", "death", "explosion", "collapse", "terror", "riot",
    "attack", "bomb", "flood", "fire", "earthquake", "tsunami",
    "trapped", "missing", "casualties", "injured", "killed",
    "destroyed", "wiped out", "massacre",
}


def check_panic(text):
    count = 0
    for w in PANIC_WORDS:
        m = re.search(rf"\b{w}\b", text)
        if m and not is_negated(text, m.start()):
            count += 1
    if count >= 2:
        return 25, "Multiple panic-inducing terms"
    if count:
        return 15, "Panic-inducing language"
    return 0, None
