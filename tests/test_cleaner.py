import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.preprocessing.cleaner import TextCleaner

sample = """
🚨🚨 BREAKING!!!!

Mumbai Dam has COLLAPSED!!!

Forward immediately!!!

https://google.com
"""

print(TextCleaner.clean(sample))