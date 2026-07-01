"""
CrisisShieldAI
ML Prediction Module

Loads the trained model and predicts whether
an input message is disaster-related.
"""

from pathlib import Path
import joblib


MODEL_PATH = Path("models/best_model.pkl")


class MLPredictor:
    """Machine Learning Predictor"""

    def __init__(self):

        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}\n"
                "Please run train.py first."
            )

        self.model = joblib.load(MODEL_PATH)

    def predict(self, message: str) -> dict:
        """
        Predict disaster probability.

        Args:
            message (str): Input message

        Returns:
            dict: Prediction result
        """

        prediction = int(self.model.predict([message])[0])

        probabilities = self.model.predict_proba([message])[0]

        confidence = float(max(probabilities) * 100)

        return {

            "prediction": prediction,

            "label": (
                "Disaster Related"
                if prediction == 1
                else "Not Disaster Related"
            ),

            "confidence": round(confidence, 2),

            "probabilities": {

                "not_disaster": round(
                    float(probabilities[0]) * 100,
                    2,
                ),

                "disaster": round(
                    float(probabilities[1]) * 100,
                    2,
                ),

            },

        }


if __name__ == "__main__":

    predictor = MLPredictor()

    sample = """
    Earthquake of magnitude 7.8 hits Japan.
    Thousands evacuated immediately.
    """

    result = predictor.predict(sample)

    print(result)