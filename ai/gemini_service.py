"""
Gemini Service

Responsible for communicating with Google's Gemini LLM.
All LangGraph agents use this service instead of directly calling Gemini.
"""

import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()


class GeminiService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

    def generate(self, prompt: str) -> str:

        try:

            response = self.model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:

            return f"Gemini Error: {str(e)}"


gemini = GeminiService()


def ask_gemini(prompt: str):

    return gemini.generate(prompt)