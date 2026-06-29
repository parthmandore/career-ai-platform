"""
Roadmap Generator Agent

Generates a personalized learning
roadmap based on resume analysis,
career advice and skill gaps.
"""

from ai.gemini_service import ask_gemini
from ai.prompts import ROADMAP_PROMPT


def roadmap_generator(state):

    prompt = f"""
    {ROADMAP_PROMPT}

    Resume Analysis:

    {state["resume_analysis"]}

    Skill Gaps:

    {state["skill_gaps"]}

    Career Advice:

    {state["career_advice"]}
    """

    response = ask_gemini(prompt)

    state["roadmap"] = response

    return state