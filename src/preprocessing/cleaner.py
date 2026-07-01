"""
Text Cleaning Module

This module prepares incoming crisis messages for
analysis by the Rule Engine, ML model and LLM.
"""

import re


class TextCleaner:
    """Utility class for cleaning input messages."""

    @staticmethod
    def remove_urls(text: str) -> str:
        """Remove URLs from text."""
        return re.sub(r"http\S+|www\.\S+", "", text)

    @staticmethod
    def remove_emojis(text: str) -> str:
        """Remove emojis and non-ASCII characters."""
        return text.encode("ascii", "ignore").decode()

    @staticmethod
    def remove_special_characters(text: str) -> str:
        """
        Remove punctuation while keeping
        letters, numbers and spaces.
        """
        return re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Replace multiple spaces with one."""
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def clean(text: str) -> str:
        """
        Complete preprocessing pipeline.
        """

        text = text.lower()

        text = TextCleaner.remove_urls(text)

        text = TextCleaner.remove_emojis(text)

        text = TextCleaner.remove_special_characters(text)

        text = TextCleaner.normalize_whitespace(text)

        return text