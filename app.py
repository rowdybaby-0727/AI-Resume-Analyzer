import streamlit as st
import PyPDF2

# Page title
st.set_page_config(page_title="AI Resume Analyzer")

# Title
st.title("📄 AI Resume Analyzer")

st.write("Upload your resume PDF")

# Upload PDF
uploaded_file = st.file_uploader("Choose Resume PDF", type="pdf")

# Function to extract text
def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

# If file uploaded
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Display text
    st.subheader("Resume Content")
    st.text_area("Extracted Text", resume_text, height=300)