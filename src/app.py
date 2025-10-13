# src/app.py

import streamlit as st
from parser import extract_text_from_pdf
from analyzer import (
    compute_similarity,
    compute_section_scores,
    find_missing_keywords,
    filter_relevant_keywords
)

# ----------------------- Streamlit UI -----------------------

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI-Powered Resume Analyzer")
st.markdown(
    "Upload your resume and paste a job description to see your AI-powered match score and improvement suggestions."
)

uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("🧾 Paste Job Description", height=250)

if st.button("🔍 Analyze Resume"):
    if uploaded_file and job_description.strip():
        with st.spinner("Analyzing your resume... ⏳"):
            resume_text = extract_text_from_pdf(uploaded_file)
            score = compute_similarity(resume_text, job_description)
            section_scores = compute_section_scores(resume_text, job_description)

            # Find missing keywords
            missing = find_missing_keywords(resume_text, job_description)
            relevant_missing = filter_relevant_keywords(missing)


        weighted_score = (
            0.5 * section_scores["Skills"] +
            0.4 * section_scores["Experience"] +
            0.1 * section_scores["Education"]
        )
        # Display results
        # st.subheader(f"✅ Overall Match Score: {score}%")
        st.subheader(f"✅ Weighted Overall Match Score: {round(weighted_score, 2)}%")

        # Section-wise scores
        st.markdown("### 📊 Section-wise Match")
        for sec, s in section_scores.items():
            st.text(f"{sec}: {s}%")
            st.progress(int(s))

        # Missing keywords
        st.markdown("### 🔑 Missing Keywords")
        if relevant_missing:
            st.write(", ".join(relevant_missing))
        else:
            st.success("🎉 Great! No major missing skills detected.")

        # Recommendations
        if score < 60:
            st.info(
                "💡 *Tip:* Consider emphasizing relevant technologies (e.g., Rust, TypeScript, or AI coding tools like Copilot/Codex) "
                "and collaborative engineering experience."
            )
        elif 60 <= score < 80:
            st.info("💡 *Tip:* You have a good base! Adding project results or tools mentioned in the JD could push your score higher.")
        else:
            st.success("🌟 Excellent! Your resume strongly aligns with the job description.")

    else:
        st.warning("⚠️ Please upload a resume and enter a job description to analyze.")
