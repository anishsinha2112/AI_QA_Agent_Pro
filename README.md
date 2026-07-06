# 🤖 AI QA Agent Pro

<div align="center">

### 🚀 AI-Powered QA Automation Platform

Generate **Test Cases**, **Playwright Automation Scripts**, **Test Strategies**, **Failure Analysis**, and **Website Test Artifacts** using **Google Gemini AI**.

Built with **Python • FastAPI • Streamlit • Google Gemini AI • Playwright**

---

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.5-blue)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# 🌐 Live Demo

### Frontend (Streamlit)

https://<YOUR_STREAMLIT_URL>

### Backend API (Render)

https://ai-qa-agent-pro.onrender.com

### Swagger Documentation

https://ai-qa-agent-pro.onrender.com/docs

---

# 📌 Overview

AI QA Agent Pro is an intelligent software testing assistant that helps QA Engineers, Automation Engineers, and SDETs accelerate software testing using Generative AI.

Instead of manually writing test cases, automation scripts, and test strategies, users simply provide a requirement, website URL, or failure log, and the application generates high-quality QA artifacts within seconds.

---

# 🚀 Features

## 📝 AI Test Case Generator

Generate detailed QA test cases from business requirements.

### Includes

- Functional Test Cases
- Positive Scenarios
- Negative Scenarios
- Boundary Value Analysis
- Edge Cases
- Priority Assignment

---

## ⚡ AI Playwright Script Generator

Automatically generate Playwright (Python) automation scripts.

Features

- Browser Launch
- Assertions
- Comments
- Best Practices
- Ready-to-run Python Code

---

## 🌐 Website URL Scanner

Analyze any website and automatically detect

- Forms
- Buttons
- Links
- Input Fields

Generate

- Website Test Cases
- Website Playwright Scripts

---

## 🐞 AI Failure Analysis

Analyze automation failures and receive

- Root Cause Analysis
- Technical Explanation
- Suggested Fixes
- Debugging Recommendations

Supports

- Selenium
- Playwright
- API Testing
- Appium
- Python Tracebacks

---

## 📋 AI Test Strategy Generator

Automatically generate complete Test Strategy documents.

Includes

- Project Overview
- Testing Objectives
- Test Scope
- Test Levels
- Functional Testing
- API Testing
- UI Testing
- Database Testing
- Security Testing
- Performance Testing
- Accessibility Testing
- Automation Strategy
- Risk Analysis
- Entry Criteria
- Exit Criteria
- Test Deliverables
- Test Metrics

---

# 📄 Export Reports

Every generated artifact can be exported as

- 📄 PDF
- 📝 Microsoft Word (.docx)
- 📊 Microsoft Excel (.xlsx)
- 📋 Markdown (.md)

---

# 🏗 System Architecture

```text
                     User
                       │
                       ▼
               Streamlit Frontend
                       │
                 REST API Requests
                       │
                       ▼
                 FastAPI Backend
      ┌────────────┬──────────────┬─────────────┐
      │            │              │             │
      ▼            ▼              ▼             ▼
 Test Cases   Playwright     Test Strategy   Failure Analysis
      │
      ▼
 Website Scanner
      │
      ▼
 Google Gemini AI
      │
      ▼
 PDF | Word | Excel Reports
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Google Gemini AI

## Frontend

- Streamlit

## Automation

- Playwright
- Pytest

## AI

- Google Gemini 2.5 Flash

## Utilities

- BeautifulSoup
- Requests
- ReportLab
- python-docx
- openpyxl

## Deployment

- Streamlit Cloud
- Render

---

# 📂 Project Structure

```text
AI_QA_Agent_Pro/
│
├── app/
│
├── backend/
│   ├── analyzer.py
│   ├── export_utils.py
│   ├── generators.py
│   ├── gemini_client.py
│   ├── main.py
│   ├── models.py
│   └── url_scanner.py
│
├── frontend/
│   └── ui.py
│
├── playwright_tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/anishsinha2112/AI_QA_Agent_Pro.git

cd AI_QA_Agent_Pro
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create

```text
.streamlit/secrets.toml
```

Add

```toml
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

API_URL="https://aiappagentpro-cmybkzrcj2rkrmkskhxho3.streamlit.app/"
```

---

# ▶ Running the Application

## Start FastAPI Backend

```bash
uvicorn app.backend.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit Frontend

```bash
python -m streamlit run app/frontend/ui.py
```

Frontend

```
http://localhost:8501
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Health Check |
| POST | /generate-testcases | Generate AI Test Cases |
| POST | /generate-playwright | Generate Playwright Script |
| POST | /generate-test-strategy | Generate AI Test Strategy |

---

# 📈 Proof of Concept (POC)

| Module | Status |
|---------|--------|
| AI Test Case Generation | ✅ PASS |
| Playwright Generator | ✅ PASS |
| Website Scanner | ✅ PASS |
| Failure Analysis | ✅ PASS |
| AI Test Strategy | ✅ PASS |
| PDF Export | ✅ PASS |
| Word Export | ✅ PASS |
| Excel Export | ✅ PASS |
| FastAPI Backend | ✅ PASS |
| Streamlit Frontend | ✅ PASS |
| Render Deployment | ✅ PASS |

---

# 🚀 Roadmap

### Completed

- ✅ AI Test Case Generator
- ✅ Playwright Generator
- ✅ Website Scanner
- ✅ Failure Analysis
- ✅ AI Test Strategy Generator
- ✅ PDF Export
- ✅ Word Export
- ✅ Excel Export
- ✅ FastAPI Backend
- ✅ Streamlit Frontend
- ✅ Render Deployment

---

### Planned

- 🤖 AI QA Assistant Chat
- 📸 Screenshot Analysis (Gemini Vision)
- 🐞 AI Bug Report Generator
- 🔗 Jira Integration
- 📊 Dashboard & Analytics
- 🔐 User Authentication
- 🗄 PostgreSQL
- 🐳 Docker Support
- ⚙ GitHub Actions CI/CD

---

# 👨‍💻 Author

## Anish Sinha

QA Automation Engineer

Skills

- Python
- FastAPI
- Streamlit
- Playwright
- Selenium
- API Testing
- Google Gemini AI

GitHub

https://github.com/anishsinha2112

LinkedIn

(Add your LinkedIn profile URL)

---

# ⭐ Support

If you found this project useful

⭐ Star this repository

🍴 Fork this repository

💡 Open Issues & Feature Requests

---

## Happy Testing 🚀