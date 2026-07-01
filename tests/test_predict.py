from src.ml.predict import MLPredictor

predictor = MLPredictor()

message = """
BREAKING!!

Mumbai Dam has collapsed.

Forward immediately.

Residents are asked to evacuate.
"""

result = predictor.predict(message)

print(result)