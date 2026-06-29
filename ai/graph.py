"""
LangGraph Workflow

Resume
   │
   ▼
Resume Analyzer
   │
   ▼
Skill Gap Analyzer
   │
   ▼
Career Advisor
   │
   ▼
Roadmap Generator
"""

from langgraph.graph import END
from langgraph.graph import StateGraph

from ai.state import CareerState

from ai.nodes.resume_analyzer import resume_analyzer
from ai.nodes.skill_gap_analyzer import skill_gap_analyzer
from ai.nodes.career_advisor import career_advisor
from ai.nodes.roadmap_generator import roadmap_generator


def build_graph():

    workflow = StateGraph(CareerState)

    workflow.add_node(
        "resume_analyzer",
        resume_analyzer,
    )

    workflow.add_node(
        "skill_gap_analyzer",
        skill_gap_analyzer,
    )

    workflow.add_node(
        "career_advisor",
        career_advisor,
    )

    workflow.add_node(
        "roadmap_generator",
        roadmap_generator,
    )

    workflow.set_entry_point(
        "resume_analyzer"
    )

    workflow.add_edge(
        "resume_analyzer",
        "skill_gap_analyzer",
    )

    workflow.add_edge(
        "skill_gap_analyzer",
        "career_advisor",
    )

    workflow.add_edge(
        "career_advisor",
        "roadmap_generator",
    )

    workflow.add_edge(
        "roadmap_generator",
        END,
    )

    return workflow.compile()