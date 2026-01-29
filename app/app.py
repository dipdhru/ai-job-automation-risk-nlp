import streamlit as st

from model import analyze_single_job
from options import ALL_SKILLS, ALL_KNOWLEDGE, ALL_ABILITIES

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="AI & Automation Job Risk Analyzer",
    layout="centered"
)

st.title("🤖 AI & Automation Job Risk Analyzer")
st.write(
    "Enter a job profile to estimate its exposure to AI-driven automation."
)

# --------------------------------------------------
# User inputs
# --------------------------------------------------
title = st.text_input("Job Title", placeholder="e.g. Mechanical Technician")

description = st.text_area(
    "Job Description",
    height=150,
    placeholder="Describe the main responsibilities of the job"
)

skills = st.multiselect(
    "Key Skills",
    options=ALL_SKILLS
)

knowledge = st.multiselect(
    "Key Knowledge Areas",
    options=ALL_KNOWLEDGE
)

abilities = st.multiselect(
    "Key Abilities",
    options=ALL_ABILITIES
)

# --------------------------------------------------
# Run analysis
# --------------------------------------------------
if st.button("Analyze Job"):
    if not title or not description:
        st.error("Please provide both Job Title and Job Description.")
    else:
        with st.spinner("Analyzing AI automation risk..."):
            result = analyze_single_job(
                title=title,
                description=description,
                skills=skills,
                knowledge=knowledge,
                abilities=abilities
            )

        st.success("Analysis complete")

        # --------------------------------------------------
        # Results
        # --------------------------------------------------
        st.subheader("🔍 Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Sector**")
            st.write(result["Sector"])

        with col2:
            st.markdown("**AI Proneness (0–1)**")
            st.write(result["AI_Proneness"])

        with col3:
            st.markdown("**Human Resistance Score**")
            st.write(result["Resistance_Factors"])

        # Optional interpretation
        if result["AI_Proneness"] > 0.66:
            st.warning("⚠️ High AI automation risk")
        elif result["AI_Proneness"] > 0.33:
            st.info("🟡 Moderate AI automation risk")
        else:
            st.success("🟢 Low AI automation risk")
