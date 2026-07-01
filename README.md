# 🛡️ CrisisShieldAI
## Enterprise Hybrid AI Crisis Rumor Verification Platform

> An AI-powered platform that verifies crisis-related messages using a Hybrid AI Engine combining Rule-Based Analysis, Machine Learning, and Google's Gemini AI.

---

# 📖 Project Overview

CrisisShieldAI is an enterprise-inspired AI application designed to analyze crisis-related messages such as disaster alerts, health advisories, strike notices, flood warnings, and viral social media forwards.

The platform combines three independent AI systems:

- Rule-Based Risk Detection
- Machine Learning Classification
- Gemini AI Semantic Analysis

These outputs are merged using a Decision Fusion Engine to generate a final risk score and a safe recommendation.

---

# 🚀 Features

- Hybrid AI Architecture
- Rule Engine
- Machine Learning Model
- Gemini AI Integration
- Decision Fusion
- Risk Score Generation
- Safe Response Generator
- Streamlit Enterprise Dashboard
- Analysis Logging
- Modular Project Structure

### Stretch Goals

- 🌍 Multilingual Rumor Detection
- 🔁 Duplicate Rumor Detection

---

# 🏗️ Project Architecture

```
User Input
     │
     ▼
Text Cleaning
     │
 ┌───┼──────────────┐
 ▼   ▼              ▼
Rule ML          Gemini AI
Engine Model
 └──────┬───────────┘
        ▼
Decision Fusion
        ▼
Final Risk Report
```

---

# 📂 Folder Structure

```
CrisisShieldAI/
│
├── app/
│   ├── app.py
│   ├── components.py
│   └── assets/
│
├── data/
├── docs/
├── logs/
├── models/
├── notebooks/
├── src/
│   ├── preprocessing/
│   ├── rules/
│   ├── ml/
│   ├── llm/
│   ├── fusion/
│   ├── database/
│   └── main_pipeline.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

# 💻 Technology Stack

### Backend

- Python

### AI / ML

- Scikit-Learn
- Logistic Regression
- TF-IDF
- Google Gemini 2.5 Flash

### Frontend

- Streamlit
- Plotly
- Streamlit Lottie

### Database

- SQLite

### Others

- Pandas
- NumPy
- Joblib
- python-dotenv

---

# 📊 Dataset

Primary Dataset

Natural Language Processing with Disaster Tweets

Synthetic Dataset

crisis_rumor_dataset_250.csv

---

# ⚙️ Installation Guide

## Step 1

Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

or download the ZIP and extract it.

---

## Step 2

Open the project

```bash
cd CrisisShieldAI
```

---

## Step 3

Create Virtual Environment

Mac/Linux

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

---

## Step 4

Activate Virtual Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Step 5

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Get your Gemini API Key from:

https://aistudio.google.com/app/apikey

---

## Step 7

Train the ML Model (first time only)

```bash
python -m src.ml.train
```

This creates:

```
models/best_model.pkl
```

---

## Step 8

Run the application

```bash
streamlit run app/app.py
```

Open:

```
http://localhost:8501
```

---

# 🧪 Running Tests

```bash
python -m tests.test_cleaner

python -m tests.test_rule_engine

python -m tests.test_predict

python -m tests.test_llm

python -m tests.test_fusion
```

---

# 📸 Sample Output

Input

```
BREAKING!!

Mumbai Dam has collapsed.

Forward immediately!!
```

Output

```
Risk Score : 75%

Risk Level : Medium

Recommendation :

Verify through official authorities before forwarding.
```

---

# ⚠️ Limitations

- AI predictions are probabilistic.
- Internet connection is required for Gemini AI.
- Does not replace official emergency services.

---

# 🚀 Future Improvements

- Multilingual Support
- Duplicate Rumor Detection
- Voice Input
- PDF Reports
- Live News Verification
- WhatsApp Bot
- Mobile App

---

# 👨‍💻 Team

- Areevv Renoyy
- Bhavya Sethia
- Malhar Satishkumar
- Ayush Bhagat

---

# 📄 License

Educational Project