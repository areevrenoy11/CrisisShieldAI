"""
Dataset preprocessing for CrisisShieldAI
"""

import pandas as pd

INPUT_FILE = "data/crisis_rumor_dataset_250.csv"
OUTPUT_FILE = "data/processed_dataset.csv"


def preprocess():

    df = pd.read_csv(INPUT_FILE)

    print("\nOriginal Dataset")
    print(df.head())

    print("\nDataset Shape:", df.shape)

    print("\nMissing Values")
    print(df.isnull().sum())

    # Fill missing values
    df = df.fillna("Unknown")

    # Convert target labels
    # Clean verification_status

    df["verification_status"] = (
        df["verification_status"]
            .astype(str)
            .str.strip()
            .str.upper()
    )

    label_mapping = {
    "TRUE": 0,
    "FALSE": 1,
    "VERIFIED": 0,
    "UNVERIFIED": 1,
    "1": 0,
    "0": 1,
    }

    df["verification_status"] = df["verification_status"].map(label_mapping)

    # Remove rows without labels
    df = df.dropna(subset=["verification_status"])

    df["verification_status"] = df["verification_status"].astype(int)

    # Encode categorical features
    df["source_present"] = (
        df["source_present"]
        .astype(str)
        .str.lower()
        .map({
            "yes": 1,
            "true": 1,
            "1": 1,
            "no": 0,
            "false": 0,
            "0": 0,
            "unknown": 0
        })
        .fillna(0)
        .astype(int)
    )

    df["urgency_words"] = (
        df["urgency_words"]
        .astype(str)
        .str.lower()
        .map({
            "yes": 1,
            "true": 1,
            "1": 1,
            "no": 0,
            "false": 0,
            "0": 0,
            "unknown": 0
        })
        .fillna(0)
        .astype(int)
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nProcessed Dataset Saved!")
    print(df.head())


if __name__ == "__main__":
    preprocess()