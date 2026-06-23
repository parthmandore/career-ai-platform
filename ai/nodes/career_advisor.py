def career_advisor(state):

    skills = state.get("skills", [])

    return {
        "career_advice":
        f"Based on skills {skills}, recommended roles are Data Analyst, Data Engineer and AI Engineer."
    }
