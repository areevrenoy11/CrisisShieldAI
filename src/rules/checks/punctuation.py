def check_exclamation(text):

    if text.count("!") >= 3:
        return 15, "Excessive exclamation marks"

    return 0, None