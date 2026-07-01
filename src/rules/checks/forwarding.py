FORWARD_WORDS = {
    "forward",
    "share",
    "send",
    "everyone",
}


def check_forwarding(text):
    count = sum(word in text for word in FORWARD_WORDS)

    if count:
        return 20, "Forwarding request"

    return 0, None