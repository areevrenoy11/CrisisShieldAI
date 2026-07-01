PANIC_WORDS = {
    "dead",
    "death",
    "explosion",
    "collapse",
    "terror",
    "riot",
    "attack",
    "bomb",
}


def check_panic(text):
    count = sum(word in text for word in PANIC_WORDS)

    if count:
        return 20, "Panic-inducing language"

    return 0, None