try:
    import spacy
    _nlp = spacy.load("en_core_web_sm")
except Exception:
    _nlp = None

CREDIBLE_TYPES = {"ORG", "GPE", "LOC", "DATE", "TIME", "CARDINAL", "PERSON", "FAC", "NORP"}


def check_specificity(text):
    if _nlp is None:
        return 0, None

    doc = _nlp(text)
    entities = [e for e in doc.ents if e.label_ in CREDIBLE_TYPES]
    words = [t for t in doc if not t.is_punct and not t.is_space]

    if len(words) < 10:
        return 0, None

    density = len(entities) / len(words)

    if density >= 0.15:
        return -25, "High specificity — dense named entities (credible)"
    if density >= 0.08:
        return -10, "Moderate specificity — some verifiable details"
    if density < 0.03:
        return 20, "Low specificity — few verifiable facts in message"
    return 0, None
