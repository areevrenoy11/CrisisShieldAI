"""
CrisisShieldAI
Gemini Analyzer — falls back to lighter models on 503
"""

import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError, ClientError

from src.prompts.crisis_prompt import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Try in order; each is a smaller/separate quota pool
MODELS = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
]

_FALLBACK = {
    "claim": "",
    "event_type": "",
    "location": "",
    "date": "Not specified",
    "source_present": False,
    "urgency": "LOW",
    "missing_information": [],
    "recommended_action": "Gemini unavailable. Try again shortly.",
    "safe_response": "Unable to analyze — all models busy.",
}


class LLMAnalyzer:

    def analyze(self, message: str) -> dict:
        prompt = f"{SYSTEM_PROMPT}\n\nMessage:\n{message}"

        for model in MODELS:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                text = response.text.strip()
                if text.startswith("```"):
                    text = text.replace("```json", "").replace("```", "").strip()
                return json.loads(text)

            except ServerError:
                continue
            except ClientError:
                return {**_FALLBACK, "recommended_action": "Gemini API key invalid or expired. Update GEMINI_API_KEY in .env.", "safe_response": "LLM unavailable — API key issue."}
            except json.JSONDecodeError:
                return {**_FALLBACK, "safe_response": response.text.strip()}

        return _FALLBACK


GeminiAnalyzer = LLMAnalyzer


if __name__ == "__main__":
    from pprint import pprint
    pprint(LLMAnalyzer().analyze("BREAKING!! Mumbai Dam has collapsed. Forward immediately."))
