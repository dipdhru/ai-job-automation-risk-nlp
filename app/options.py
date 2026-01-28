"""
This file prepares dropdown options for the Streamlit UI.
It converts ONET-style labels into clean, user-selectable values.
"""

from ai_resistance import (
    low_ai_resistance,
    medium_ai_resistance,
    high_ai_resistance
)

def split_options(items):
    skills = []
    knowledge = []
    abilities = []

    for item in items:
        if item.startswith("Skill:"):
            skills.append(item.replace("Skill: ", "").strip())
        elif item.startswith("Knowledge:"):
            knowledge.append(item.replace("Knowledge: ", "").strip())
        elif item.startswith("Ability:"):
            abilities.append(item.replace("Ability: ", "").strip())

    return skills, knowledge, abilities


# Split each resistance group
low_skills, low_knowledge, low_abilities = split_options(low_ai_resistance)
med_skills, med_knowledge, med_abilities = split_options(medium_ai_resistance)
high_skills, high_knowledge, high_abilities = split_options(high_ai_resistance)

# Merge & deduplicate
ALL_SKILLS = sorted(set(low_skills + med_skills + high_skills))
ALL_KNOWLEDGE = sorted(set(low_knowledge + med_knowledge + high_knowledge))
ALL_ABILITIES = sorted(set(low_abilities + med_abilities + high_abilities))
