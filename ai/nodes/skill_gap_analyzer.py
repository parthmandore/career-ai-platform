"""
Skill Gap Analyzer Agent

Analyzes the resume analysis and identifies
missing technical skills, certifications,
and learning opportunities.
"""

from ai.gemini_service import ask_gemini
from ai.prompts import SKILL_GAP_PROMPT


def skill_gap_analyzer(state):

    prompt = f"""
    {SKILL_GAP_PROMPT}

    Resume Analysis:

    {state["resume_analysis"]}
    """

    response = ask_gemini(prompt)

    state["skill_gaps"] = response

    return state