"""
Exploratory Data Analysis for CrisisShieldAI
"""

import os
import matplotlib.pyplot as plt
import pandas as pd

INPUT_FILE = "data/processed_dataset.csv"
OUTPUT_DIR = "docs/eda"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nVerification Status Distribution:")
print(df["verification_status"].value_counts())

# Graph 1
plt.figure(figsize=(6,4))
df["verification_status"].value_counts().plot(kind="bar")
plt.title("Verified vs Unverified Messages")
plt.xlabel("Verification Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/verification_distribution.png")
plt.close()

# Graph 2
plt.figure(figsize=(8,4))
df["claimed_location"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Claimed Locations")
plt.xlabel("Location")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/top_locations.png")
plt.close()

print("\nEDA completed successfully!")
print(f"Graphs saved in {OUTPUT_DIR}")