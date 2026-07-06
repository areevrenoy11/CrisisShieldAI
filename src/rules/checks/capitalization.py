def check_caps(text):
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0, None
    ratio = sum(c.isupper() for c in letters) / len(letters)
    if ratio > 0.5:
        return 20, "Excessive capitalisation (shouting tone)"
    if ratio > 0.3:
        return 10, "High capitalisation ratio"
    return 0, None
