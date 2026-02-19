import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.matcher import match_resume_to_jobs
from utils.skill_gap import get_skill_gap
from utils.visualization import show_score_bar

st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screening System - Professional Version")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF only)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    extracted_text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(extracted_text)

    st.subheader("Top Job Recommendations")

    results = match_resume_to_jobs(cleaned_text)

    for _, row in results.iterrows():

        role = row["role"]
        score = row["score"]

        st.markdown(f"## ⭐ {role}")
        st.write(f"Match Score: {round(score*100,2)}%")

        # Upgrade 2 — Visual Bar
        show_score_bar(score)

        # Upgrade 1 — Skill Gap
        found, missing = get_skill_gap(cleaned_text, row["skills"])

        st.write("✔ Skills Found:", ", ".join(found) if found else "None")
        st.write("❌ Missing Skills:", ", ".join(missing) if missing else "None")

        st.markdown("---")
