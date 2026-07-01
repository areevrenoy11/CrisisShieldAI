"""
Constants used by the Rule Engine.
"""

URGENCY_WORDS = [
    "urgent",
    "immediately",
    "breaking",
    "alert",
    "emergency",
    "warning",
    "evacuate",
]

PANIC_WORDS = [
    "dead",
    "death",
    "explosion",
    "bomb",
    "collapsed",
    "flood",
    "earthquake",
    "fire",
    "tsunami",
    "terrorist",
]

FORWARD_PHRASES = [
    "forward immediately",
    "share now",
    "share immediately",
    "forward this",
    "send to everyone",
]

TRUSTED_DOMAINS = [
    "gov.in",
    "ndma.gov.in",
    "who.int",
    "nic.in",
]