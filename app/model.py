import os
import pickle
import json
import csv
from sentence_transformers import SentenceTransformer
from ai_resistance import (
    low_ai_resistance,
    medium_ai_resistance,
    high_ai_resistance
)

# paths
BASE_DIR = os.path.dirname(__file__)
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")

# load frozen artifacts
kmeans = pickle.load(open(os.path.join(ARTIFACTS_DIR, "kmeans.pkl"), "rb"))

# Load cluster scores using csv module (no pandas needed)
cluster_scores_dict = {}
with open(os.path.join(ARTIFACTS_DIR, "cluster_scores.csv"), 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cluster_scores_dict[row['cluster_label']] = float(row['AI_Proneness_Normalized'])

cluster_names = json.load(open(os.path.join(ARTIFACTS_DIR, "cluster_names.json")))

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# resistance logic
AI_WEIGHTS = {"low": 0, "medium": 1, "high": 2}

LOW_SET = set(low_ai_resistance)
MED_SET = set(medium_ai_resistance)
HIGH_SET = set(high_ai_resistance)

def score_user_inputs(skills, knowledge, abilities):
    score = 0

    for s in skills:
        if f"Skill: {s}" in HIGH_SET:
            score += AI_WEIGHTS["high"]
        elif f"Skill: {s}" in MED_SET:
            score += AI_WEIGHTS["medium"]

    for k in knowledge:
        if f"Knowledge: {k}" in HIGH_SET:
            score += AI_WEIGHTS["high"]
        elif f"Knowledge: {k}" in MED_SET:
            score += AI_WEIGHTS["medium"]

    for a in abilities:
        if f"Ability: {a}" in HIGH_SET:
            score += AI_WEIGHTS["high"]
        elif f"Ability: {a}" in MED_SET:
            score += AI_WEIGHTS["medium"]

    return score

def analyze_single_job(title, description, skills, knowledge, abilities):
    text = (
        f"{title.lower()} is a job whose key responsibility is "
        f"{description.lower()}. "
        f"the required skills are {', '.join(skills).lower()}. "
        f"the required knowledge is {', '.join(knowledge).lower()}. "
        f"the required abilities are {', '.join(abilities).lower()}."
    )

    embedding = embedder.encode([text])
    cluster = kmeans.predict(embedding)[0]
    sector = cluster_names[str(cluster)]

    # Get base score from cluster_scores dict
    base_score = cluster_scores_dict.get(sector, 0.5)  # Default to 0.5 if not found

    resistance_bonus = score_user_inputs(skills, knowledge, abilities)
    final_score = max(0, round(base_score - 0.05 * resistance_bonus, 2))

    return {
        "Sector": sector,
        "AI_Proneness": final_score,
        "Resistance_Factors": resistance_bonus
    }