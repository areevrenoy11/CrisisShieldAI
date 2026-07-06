import re

AUTHORITY_SOURCES = [
    r"ndma", r"national disaster",
    r"imd", r"meteorological department",
    r"seismolog",
    r"district collector", r"district administration",
    r"police (confirm|state|announce|said)",
    r"government (confirm|announc|state)",
    r"official(ly|s| statement| source)",
    r"ministry of",
    r"confirmed by",
    r"press release",
    r"according to (the |)(police|government|authority|ndma|imd)",
]


def check_authority(text):
    count = sum(bool(re.search(p, text)) for p in AUTHORITY_SOURCES)
    if count >= 2:
        return -35, "Multiple named authorities cited (credible)"
    if count:
        return -20, "Named authority source cited"
    return 0, None
