import re

BREAKING_PATTERNS = [
    r"\bbreaking\b", r"\burgent\b", r"\balert\b", r"\bjust in\b",
    r"\bcollapsed?\b", r"\bdestroyed?\b", r"\bexplosion\b", r"\battack(ed)?\b",
    r"\bdisaster\b", r"\bcatastrophe\b",
]

SUPPRESSION_PATTERNS = [
    r"government (hiding|covering|suppressing|not telling)",
    r"(media|news) (not |)(reporting|covering|showing)",
    r"(they|authorities) (don'?t|do not) want (you|us) to know",
    r"before (they |)(delete|remove|take down)",
    r"hiding (this|the truth|it)",
    r"cover.?up",
    r"they don'?t want",
    r"not being reported",
]

FORWARD_PATTERNS = [
    r"forward (this|to|immediately|now|everyone|as many)",
    r"share (this|immediately|now|before)",
    r"send (this|to|everyone|all|your)",
    r"spread (this|the word|the news)",
    r"pass (this|it) (on|along)",
]


def check_viral_template(text):
    has_breaking = any(re.search(p, text) for p in BREAKING_PATTERNS)
    has_suppression = any(re.search(p, text) for p in SUPPRESSION_PATTERNS)
    has_forward = any(re.search(p, text) for p in FORWARD_PATTERNS)

    count = sum([has_breaking, has_suppression, has_forward])

    if count == 3:
        return 40, "Full viral template: claim + suppression narrative + forward pressure"
    if count == 2:
        return 20, "Partial viral template (2 of 3 signature components)"
    return 0, None
