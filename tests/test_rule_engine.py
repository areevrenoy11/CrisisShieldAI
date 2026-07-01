from src.preprocessing.cleaner import TextCleaner
from src.rules.rule_engine import RuleEngine

sample = """
🚨🚨 BREAKING!!!!

Mumbai Dam has COLLAPSED!!!!

Forward immediately!!!

https://google.com
"""

clean = TextCleaner.clean(sample)

engine = RuleEngine()

result = engine.analyze(sample, clean)

print(result)