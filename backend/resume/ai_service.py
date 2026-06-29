from ai.resume_parser import extract_resume_text
from ai.graph import graph


def analyze_resume(pdf_path):

    resume_text = extract_resume_text(pdf_path)

    initial_state = {
        "resume_text": resume_text,

        "extracted_skills": [],
        "education": "",
        "projects": [],
        "experience": "",

        "resume_analysis": "",
        "skill_gaps": "",

        "career_advice": "",
        "roadmap": "",

        "error": None,
    }

    result = graph.invoke(initial_state)

    return result