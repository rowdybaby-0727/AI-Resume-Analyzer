import streamlit as st
import PyPDF2
import pandas as pd

# Page config
st.set_page_config(page_title="AI Resume Analyzer")

# Title
st.title("📄 AI Resume Analyzer")

st.write("Upload your resume PDF")

# Skill database
skills_db = [
    "python",
    "java",
    "c",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "deep learning",
    "tensorflow",
    "streamlit",
    "react",
    "nodejs",
    "mongodb",
    "git",
    "github"
]

# Upload PDF
uploaded_file = st.file_uploader("Choose Resume PDF", type="pdf")

# Extract text function
def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text.lower()

# If uploaded
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract resume text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Show extracted text
    st.subheader("📑 Resume Content")

    st.text_area("Extracted Text", resume_text, height=250)

    # Skill extraction
    found_skills = []

    for skill in skills_db:
        if skill in resume_text:
            found_skills.append(skill)

    # Display skills
    st.subheader("💡 Skills Found")

    if found_skills:
        st.write(found_skills)
    else:
        st.warning("No skills detected")

    # ATS Score
    ats_score = int((len(found_skills) / len(skills_db)) * 100)

    st.subheader("📊 ATS Score")

    st.progress(ats_score)

    st.write(f"ATS Score: {ats_score}%")

    # Suggestions
    st.subheader("🚀 Suggestions")

    missing_skills = []

    for skill in skills_db:
        if skill not in found_skills:
            missing_skills.append(skill)

    if missing_skills:
        st.write("Consider adding these skills:")
        st.write(missing_skills)

    else:
        st.success("Excellent Resume!")