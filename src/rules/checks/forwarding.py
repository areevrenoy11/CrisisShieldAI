import re

FORWARD_WORDS = {
    "forward", "share", "send", "everyone", "spread",
    "viral", "contacts", "groups", "broadcast",
    "don't ignore", "must read", "please share",
}


def check_forwarding(text):
    count = sum(bool(re.search(rf"\b{w}\b", text)) for w in FORWARD_WORDS)
    if count >= 2:
        return 30, "Strong forwarding pressure"
    if count:
        return 20, "Forwarding request detected"
    return 0, None
