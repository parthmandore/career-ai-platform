"""
Resume Analyzer Agent

Reads the resume text and generates a structured
analysis using Gemini.
"""

from ai.gemini_service import ask_gemini
from ai.prompts import RESUME_ANALYZER_PROMPT


def resume_analyzer(state):

    resume_text = state["resume_text"]

    prompt = f"""
    {RESUME_ANALYZER_PROMPT}

    Resume:

    {resume_text}
    """

    response = ask_gemini(prompt)

    state["resume_analysis"] = response

    return state