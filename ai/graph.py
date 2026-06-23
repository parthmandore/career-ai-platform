from langgraph.graph import StateGraph

from state import CareerState

from nodes.resume_analyzer import analyze_resume
from nodes.skill_gap_analyzer import analyze_skill_gap
from nodes.roadmap_generator import generate_roadmap

workflow = StateGraph(CareerState)

workflow.add_node(
    "resume_analyzer",
    analyze_resume
)

workflow.add_node(
    "skill_gap_analyzer",
    analyze_skill_gap
)

workflow.add_node(
    "roadmap_generator",
    generate_roadmap
)

workflow.add_edge(
    "resume_analyzer",
    "skill_gap_analyzer"
)

workflow.add_edge(
    "skill_gap_analyzer",
    "roadmap_generator"
)

graph = workflow.compile()
