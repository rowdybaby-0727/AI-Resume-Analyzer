import streamlit as st
import PyPDF2
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get ATS score, "
    "skill analysis and improvement suggestions."
)

# -----------------------------------
# LOAD SKILLS CSV
# -----------------------------------

skills_df = pd.read_csv("skills.csv")

skills_db = skills_df["Skill"].str.lower().tolist()

# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Choose Resume PDF",
    type="pdf"
)

# -----------------------------------
# PDF TEXT EXTRACTION
# -----------------------------------

def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text.lower()

# -----------------------------------
# MAIN PROCESS
# -----------------------------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # -----------------------------------
    # RESUME CONTENT
    # -----------------------------------

    st.subheader("📑 Resume Content")

    st.text_area(
        "Extracted Resume Text",
        resume_text,
        height=250
    )

    # -----------------------------------
    # SKILL DETECTION
    # -----------------------------------

    found_skills = []

    for skill in skills_db:

        if skill in resume_text:

            found_skills.append(skill.title())

    # -----------------------------------
    # DISPLAY SKILLS
    # -----------------------------------

    st.subheader("💡 Skills Detected")

    if found_skills:

        st.success("Skills Found Successfully")

        st.write(found_skills)

    else:

        st.warning("No skills detected")

    # -----------------------------------
    # ATS SCORE
    # -----------------------------------

    ats_score = int(
        (len(found_skills) / len(skills_db)) * 100
    )

    st.subheader("📊 ATS Score")

    st.progress(ats_score)

    st.write(f"### ATS Score: {ats_score}%")

    # -----------------------------------
    # ATS FEEDBACK
    # -----------------------------------

    if ats_score >= 80:

        st.success("Excellent ATS Resume")

    elif ats_score >= 60:

        st.warning("Good Resume. Can improve more.")

    else:

        st.error("Resume needs improvement")

    # -----------------------------------
    # MISSING SKILLS
    # -----------------------------------

    st.subheader("🚀 Missing Skills")

    missing_skills = []

    for skill in skills_db:

        if skill.title() not in found_skills:

            missing_skills.append(skill.title())

    if missing_skills:

        st.write(
            "Consider adding these skills:"
        )

        st.write(missing_skills)

    else:

        st.success(
            "Excellent Skill Coverage"
        )

    # -----------------------------------
    # RESUME ANALYSIS
    # -----------------------------------

    st.subheader("📈 Resume Analysis")

    total_words = len(resume_text.split())

    total_skills = len(found_skills)

    analysis_data = {

        "Metric": [
            "Total Words",
            "Skills Found",
            "Missing Skills",
            "ATS Score"
        ],

        "Value": [
            total_words,
            total_skills,
            len(missing_skills),
            f"{ats_score}%"
        ]
    }

    analysis_df = pd.DataFrame(
        analysis_data
    )

    st.table(analysis_df)

    # -----------------------------------
    # RESUME SUGGESTIONS
    # -----------------------------------

    st.subheader("🧠 AI Suggestions")

    suggestions = []

    if total_words < 200:

        suggestions.append(
            "Increase resume content."
        )

    if ats_score < 60:

        suggestions.append(
            "Add more technical skills."
        )

    if "project" not in resume_text:

        suggestions.append(
            "Add project section."
        )

    if "internship" not in resume_text:

        suggestions.append(
            "Add internship experience."
        )

    if len(suggestions) == 0:

        st.success(
            "Your resume looks professional."
        )

    else:

        for suggestion in suggestions:

            st.write("✅", suggestion)

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.write(
    "Developed by Prasanna R 🚀"
)