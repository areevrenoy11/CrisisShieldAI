"""
CrisisShieldAI
Gemini Analyzer (Google GenAI SDK)
"""

import os
import json

from dotenv import load_dotenv
from google import genai

from src.prompts.crisis_prompt import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiAnalyzer:

    def analyze(self, message: str):

        prompt = f"""
{SYSTEM_PROMPT}

Message:
{message}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:
            return json.loads(text)

        except json.JSONDecodeError:

            return {
                "claim": "",
                "event_type": "",
                "location": "",
                "date": "Not specified",
                "source_present": False,
                "urgency": "LOW",
                "missing_information": [],
                "recommended_action": "Unable to analyze message.",
                "safe_response": text,
            }


if __name__ == "__main__":

    analyzer = GeminiAnalyzer()

    sample = """
    BREAKING!!

    Mumbai Dam has collapsed.

    Forward immediately.

    """

    result = analyzer.analyze(sample)

    from pprint import pprint
    pprint(result)