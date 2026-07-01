from src.llm.analyzer import GeminiAnalyzer

message = """
BREAKING!

Mumbai Dam has collapsed.

Forward immediately!!

"""

analyzer = GeminiAnalyzer()

result = analyzer.analyze(message)

print(result)