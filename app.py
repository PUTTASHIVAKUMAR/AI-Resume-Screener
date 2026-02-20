import streamlit as st
import pandas as pd

from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_gap import get_skill_gap
from utils.visualization import show_score_bar

# NEW INDUSTRY IMPORTS
from utils.semantic_matcher import semantic_match
from utils.scoring import calculate_resume_score, get_readiness_level


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screening System - Industry Version")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

# -----------------------------
# MAIN LOGIC
# -----------------------------
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract + clean resume text
    extracted_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(extracted_text)

    # Load job roles dataset
    df = pd.read_csv("data/job_roles.csv")

    # Get job descriptions
    job_descriptions = df["skills"].tolist()
    # -----------------------------
    # SEMANTIC AI MATCHING
    # -----------------------------
    results = semantic_match(cleaned_text, job_descriptions, top_n=3)

    # Extract similarity scores
    similarity_scores = [score for _, score in results]

    # -----------------------------
    # AI RESUME SCORE
    # -----------------------------
    resume_score = calculate_resume_score(similarity_scores)
    readiness = get_readiness_level(resume_score)

    st.subheader("⭐ AI Resume Score")
    st.write(f"**Score:** {round(resume_score,2)}%")
    st.write(f"**Industry Level:** {readiness}")

    st.markdown("---")

    # -----------------------------
    # TOP JOB RECOMMENDATIONS
    # -----------------------------
    st.subheader("🎯 Top Job Recommendations")

    for idx, score in results:

        role = df.iloc[idx]["role"]

        st.markdown(f"## ⭐ {role}")
        st.write(f"Match Score: {round(score*100,2)}%")

        # Visual score bar
        show_score_bar(score)

        # Skill Gap Analysis
        found, missing = get_skill_gap(cleaned_text, df.iloc[idx]["skills"])

        st.write("✔ Skills Found:", ", ".join(found) if found else "None")
        st.write("❌ Missing Skills:", ", ".join(missing) if missing else "None")

        st.markdown("---")