"""
Career Advisor Agent

Suggests suitable career paths
based on resume analysis and
identified skill gaps.
"""

from ai.gemini_service import ask_gemini
from ai.prompts import CAREER_ADVISOR_PROMPT


def career_advisor(state):

    prompt = f"""
    {CAREER_ADVISOR_PROMPT}

    Resume Analysis:

    {state["resume_analysis"]}

    Skill Gaps:

    {state["skill_gaps"]}
    """

    response = ask_gemini(prompt)

    state["career_advice"] = response

    return state