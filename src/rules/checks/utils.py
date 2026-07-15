NEGATION_WORDS = {
    "no", "not", "never", "none", "without", "zero",
    "didn't", "don't", "won't", "hasn't", "haven't",
    "isn't", "aren't", "wasn't", "weren't", "can't", "cannot",
}


def is_negated(text: str, match_start: int, window: int = 4) -> bool:
    words_before = text[:match_start].split()[-window:]
    return any(w.lower().rstrip(",.") in NEGATION_WORDS for w in words_before)
