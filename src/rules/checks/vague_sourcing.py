import re

VAGUE_PHRASES = [
    r"heard (from|that)",
    r"someone (told|said)",
    r"people (are |)saying",
    r"apparently",
    r"rumour has it",
    r"not (yet |)confirmed",
    r"no official",
    r"unconfirmed",
    r"i think",
    r"i saw",
    r"my (neighbour|friend|relative|contact)",
    r"word is",
    r"sources say",
]


def check_vague_sourcing(text):
    count = sum(bool(re.search(p, text)) for p in VAGUE_PHRASES)
    if count >= 2:
        return 30, "Multiple unverified sourcing phrases"
    if count:
        return 20, "Vague / unverified source"
    return 0, None
