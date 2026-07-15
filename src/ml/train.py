"""
CrisisShieldAI
ML Training Module
Train multiple ML models on the Kaggle Disaster Tweets dataset
"""

import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

# -------------------------------
# Configuration
# -------------------------------

DATASET_PATH = "data/processed_dataset.csv"
MODEL_PATH = "models/best_model.pkl"
RESULT_PATH = "models/model_comparison.csv"

os.makedirs("models", exist_ok=True)


def load_dataset():
    """Load Kaggle Disaster Tweets dataset"""

    df = pd.read_csv(DATASET_PATH)

    print("=" * 60)
    print("Dataset Loaded Successfully")
    print("=" * 60)

    print("Shape:", df.shape)

    df = df.rename(columns={"message": "text", "verification_status": "target"})

    required_columns = ["text", "target"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.dropna(subset=["text", "target"])
    df["text"] = df["text"].astype(str)
    df["target"] = df["target"].astype(int)

    print("\nClass Distribution")
    print(df["target"].value_counts())

    return df


def train_models():

    df = load_dataset()

    X = df["text"]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Naive Bayes": MultinomialNB(),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42,
        ),
    }

    results = []

    best_model = None
    best_accuracy = 0

    print("\nTraining Models...\n")

    for model_name, classifier in models.items():

        pipeline = Pipeline([
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    max_features=5000,
                    ngram_range=(1, 2),  # unigrams + bigrams
                ),
            ),
            (
                "classifier",
                CalibratedClassifierCV(classifier, cv=3),
            ),
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(
            y_test,
            predictions,
            zero_division=0,
        )
        recall = recall_score(
            y_test,
            predictions,
            zero_division=0,
        )
        f1 = f1_score(
            y_test,
            predictions,
            zero_division=0,
        )

        print(f"{model_name}")
        print("-" * 40)
        print(f"Accuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}\n")

        results.append({
            "Model": model_name,
            "Accuracy": round(accuracy, 4),
            "Precision": round(precision, 4),
            "Recall": round(recall, 4),
            "F1 Score": round(f1, 4),
        })

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = pipeline

    results_df = pd.DataFrame(results)

    results_df.sort_values(
        by="Accuracy",
        ascending=False,
        inplace=True,
    )

    results_df.to_csv(
        RESULT_PATH,
        index=False,
    )

    joblib.dump(
        best_model,
        MODEL_PATH,
    )

    print("=" * 60)
    print("Training Complete")
    print("=" * 60)

    print(results_df)

    print(f"\nBest Accuracy : {best_accuracy:.4f}")
    print(f"Best Model Saved : {MODEL_PATH}")
    print(f"Comparison Saved : {RESULT_PATH}")


if __name__ == "__main__":
    train_models()