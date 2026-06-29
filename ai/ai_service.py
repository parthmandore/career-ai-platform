from ai.resume_parser import extract_resume_text
from ai.graph import build_graph
from ai.state import CareerState


def analyze_resume(pdf_path):

    resume_text = extract_resume_text(pdf_path)

    graph = build_graph()

    state = CareerState(
        resume_text=resume_text,
        extracted_skills=[],
        career_advice="",
        roadmap="",
        skill_gap="",
    )

    result = graph.invoke(state)

    return result