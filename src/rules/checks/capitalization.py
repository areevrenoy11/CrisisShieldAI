def check_caps(text):

    upper = sum(c.isupper() for c in text)

    if upper > 20:
        return 15, "Excessive capital letters"

    return 0, None