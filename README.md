<div align="center">

# 🤖 AI Resume Analyzer
### *AI-Powered ATS Resume Screening & Career Optimization Platform*

<p align="center">
  An intelligent resume analysis platform that evaluates resumes using AI, NLP, ATS compatibility scoring, skill extraction, and job-description matching to help candidates optimize their resumes for better hiring success.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/NLP-spaCy-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Resume%20Analysis-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ATS-Compatible-success?style=for-the-badge" />
</p>

<p align="center">
  🔗 <a href="https://ai-resume-analyzer-ravzahlzcxmnkesjpywyzt.streamlit.app/">Live Demo</a> |
  📂 <a href="https://github.com/rowdybaby-0727/AI-Resume-Analyzer">GitHub Repository</a>
</p>

</div>

---

# 📚 Table of Contents

- [🎯 Overview](#-overview)
- [🖼️ Project Showcase](#️-project-showcase)
- [✨ Key Features](#-key-features)
- [🏗️ System Architecture](#️-system-architecture)
- [🧠 NLP Pipeline](#-nlp-pipeline)
- [⚙️ Technology Stack](#️-technology-stack)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage Guide](#-usage-guide)
- [📂 Project Structure](#-project-structure)
- [📊 Results & Analysis](#-results--analysis)
- [📱 Responsive UI](#-responsive-ui)
- [🔧 Configuration](#-configuration)
- [🧪 Troubleshooting](#-troubleshooting)
- [🛣️ Future Enhancements](#️-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

# 🎯 Overview

## 📌 Problem Statement

Many job applicants fail Applicant Tracking Systems (ATS) because their resumes are poorly optimized, missing keywords, or formatted incorrectly. Recruiters also spend significant time manually reviewing resumes.

## 💡 Solution

The **AI Resume Analyzer** uses:

- Natural Language Processing (NLP)
- ATS compatibility analysis
- Skill extraction
- Resume-to-job-description matching
- AI-based recommendations

to help users optimize resumes and improve hiring success rates.

---

# 🖼️ Project Showcase

## 🚀 Hero Banner

<div align="center">

<img width="3584" height="1184" alt="hero banner" src="https://github.com/user-attachments/assets/b0ec3438-b325-443a-a75d-0e7c916945a2" />


</div>

---

## 📊 Analysis Dashboard

<div align="center">

<img width="2816" height="1536" alt="dashboard" src="https://github.com/user-attachments/assets/5991669c-0244-4530-abb9-8c4606937a50" />


</div>

---

## 🧠 Extracted Skills & Competencies

<div align="center">

<img width="2816" height="1536" alt="Extracted Skills   Competencies" src="https://github.com/user-attachments/assets/5193a6bf-85fb-44e0-b728-ac129414296c" />


</div>

---

## 📱 Mobile Responsive Design

<div align="center">

<img width="2816" height="1536" alt="UI design" src="https://github.com/user-attachments/assets/993398a6-d2ca-47db-a1c5-ec01ed0110b5" />


</div>

---

# ✨ Key Features

## 📄 Resume Parsing

- Extract text from PDF/DOCX resumes
- Automatic metadata extraction
- Contact information detection

---

## 🧠 NLP Analysis

- Skill extraction using NLP
- Named Entity Recognition (NER)
- Keyword matching analysis

---

## 📈 ATS Compatibility Scoring

- ATS-friendly formatting checks
- Resume quality scoring
- Keyword density analysis

---

## 🎯 Job Match Analysis

- Compare resume with job descriptions
- Missing skill identification
- Match percentage calculation

---

## 💡 Smart Recommendations

- Resume improvement suggestions
- Formatting optimization
- AI-powered career feedback

---

# 🏗️ System Architecture

<div align="center">

<img width="2816" height="1536" alt="architecture" src="https://github.com/user-attachments/assets/df6d968c-5eeb-4ffe-9658-cfbfcf16a4ae" />


### 📌 AI Resume Analyzer System Architecture

</div>

---

## 🔄 Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
NLP Processing
      ↓
Skill Extraction
      ↓
ATS Analysis
      ↓
Job Matching
      ↓
Dashboard Visualization
      ↓
Recommendations Generation
```

---

# 🧠 NLP Pipeline

<div align="center">

<img width="2816" height="1536" alt="pipeline" src="https://github.com/user-attachments/assets/4fba2629-f477-478d-8749-9e9df9a9ee61" />


</div>

---

# ⚙️ Technology Stack

| Category | Technology | Purpose |
|---|---|---|
| Programming Language | Python | Backend logic |
| Framework | Streamlit | Web application |
| NLP Library | spaCy / NLTK | Natural language processing |
| Data Analysis | Pandas | Resume data handling |
| Visualization | Matplotlib / Plotly | Dashboard analytics |
| PDF Parsing | PyPDF2 / pdfminer | Resume extraction |
| Deployment | Streamlit Cloud | Hosting |

---

# 🚀 Quick Start

## 📋 Prerequisites

Before running the project locally, ensure you have:

- Python 3.10+
- pip package manager
- Git installed

---

## 💻 Clone Repository

```bash
git clone https://github.com/rowdybaby-0727/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🌐 Open in Browser

```text
http://localhost:8501
```

---

# 📖 Usage Guide

## 🏠 Step 1 – Upload Resume

- Upload resume in PDF/DOCX format
- Optionally provide job description

---

## 🧠 Step 2 – AI Analysis

The system performs:

- ATS scoring
- Skill extraction
- NLP analysis
- Job matching

---

## 📊 Step 3 – View Dashboard

Users receive:

- ATS score
- Missing skills
- Recommendations
- Match percentage

---

## 💡 Step 4 – Improve Resume

Apply AI-generated recommendations to optimize resume quality.

---

# 📂 Project Structure

```bash
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── architecture.png
│   ├── dashboard.png
│   ├── extracted-skills.png
│   ├── hero-banner.png
│   ├── pipeline.png
│   ├── workflow.png
│   └── ui-design.png
│
├── models/
├── utils/
├── parser/
├── analysis/
└── recommendations/
```

---

# 📊 Results & Analysis

## 📈 Resume Optimization Comparison

<div align="center">

<img width="2816" height="1536" alt="Resume Optimizations Comparison" src="https://github.com/user-attachments/assets/970fdf4d-1e20-4f3a-a660-bc9bae2137ec" />


</div>

---

## 📊 Resume-to-Job Match Analysis

<div align="center">

<img width="2816" height="1536" alt="visual representation" src="https://github.com/user-attachments/assets/45038002-b8db-4e03-b271-02b679b8a5b3" />

</div>

---

## 💡 Resume Improvement Recommendations

<div align="center">

<img width="2816" height="1536" alt="UI mockup" src="https://github.com/user-attachments/assets/a84afb20-fb9f-4fc6-a907-96e1be5cae1b" />


</div>

---

## 📉 Admin Analytics Dashboard

<div align="center">

<img width="2816" height="1536" alt="Dashboard mockup" src="https://github.com/user-attachments/assets/e434e984-735e-4240-b841-fe8afc47f9d7" />


</div>

---

# 📱 Responsive UI

<div align="center">

<img width="2816" height="1536" alt="workflow" src="https://github.com/user-attachments/assets/e3fc8566-1c88-40cf-8916-dfe4c2fabc61" />


</div>

---

# 🔧 Configuration

## 📦 requirements.txt

```txt
streamlit
pandas
numpy
spacy
nltk
PyPDF2
pdfminer.six
matplotlib
plotly
```

---

## ⚙️ spaCy Model Setup

```bash
python -m spacy download en_core_web_sm
```

---

# 🧪 Troubleshooting

<details>
<summary>❌ ModuleNotFoundError</summary>

### Solution

```bash
pip install -r requirements.txt
```

</details>

---

<details>
<summary>❌ spaCy model missing</summary>

### Solution

```bash
python -m spacy download en_core_web_sm
```

</details>

---

<details>
<summary>❌ PDF text not extracting properly</summary>

### Solution

- Ensure resume is text-based PDF
- Avoid scanned image PDFs
- Use DOCX format if extraction fails

</details>

---

# 🛣️ Future Enhancements

## 🚀 Short-Term Goals

- Improve ATS scoring accuracy
- Add more resume templates
- Improve recommendation engine
- Add exportable reports

---

## 🌟 Long-Term Goals

- AI resume rewriting
- LinkedIn integration
- Real-time recruiter dashboard
- Interview preparation assistant
- Multi-language support
- AI career prediction system

---

# 🤝 Contributing

Contributions are welcome!

## 📌 Steps to Contribute

```bash
# Fork repository

# Create new branch
git checkout -b feature-name

# Commit changes
git commit -m "Added new feature"

# Push changes
git push origin feature-name
```

Then create a Pull Request 🚀

---

# 📄 License

This project is licensed under the MIT License.

```text
MIT License © 2026 AI Resume Analyzer
```

---

# 📬 Contact

## 👨‍💻 Developer Information

- GitHub: https://github.com/rowdybaby-0727
- Repository: https://github.com/rowdybaby-0727/AI-Resume-Analyzer
- Live Demo: https://ai-resume-analyzer-ravzahlzcxmnkesjpywyzt.streamlit.app/

---

# 🙏 Acknowledgments

Special thanks to:

- Streamlit Community
- spaCy NLP Library
- Open-source AI contributors
- Python developer ecosystem

---

# ⭐ Support the Project

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📢 Share with others

<div align="center">

## 🚀 Empowering Careers with AI 🚀

</div>
