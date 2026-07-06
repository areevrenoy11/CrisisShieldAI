def check_exclamation(text):
    count = text.count("!")
    if count >= 5:
        return 20, "Extreme punctuation overuse"
    if count >= 3:
        return 10, "Excessive exclamation marks"
    return 0, None
