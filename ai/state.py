from typing import TypedDict, List, Optional


class CareerState(TypedDict):
    """
    Shared state passed between all LangGraph agents.
    Every agent reads from and updates this state.
    """

    # -------- Input --------
    resume_text: str

    # -------- Resume Analysis --------
    resume_analysis: str
    extracted_skills: List[str]
    education: str
    projects: List[str]
    experience: str

    # -------- Skill Gap --------
    skill_gaps: str

    # -------- Career Recommendation --------
    career_advice: str

    # -------- Learning Roadmap --------
    roadmap: str

    # -------- Error Handling --------
    error: Optional[str]