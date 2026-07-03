# 🤖 AI QA Agent Pro

> **AI-Powered QA Automation Assistant** built with **Python, FastAPI, Streamlit, Playwright, and Google Gemini AI**.

AI QA Agent Pro helps QA Engineers, SDETs, and Software Testers accelerate software testing by generating intelligent test artifacts, automation scripts, and failure analysis using Generative AI.

---

# 🚀 Features

## ✅ AI Test Case Generator

Generate comprehensive QA test cases from business requirements.

**Includes**

* Functional Test Cases
* Positive Test Scenarios
* Negative Test Scenarios
* Boundary Value Analysis
* Edge Cases
* Priority Assignment

---

## ⚡ AI Playwright Script Generator

Automatically generate Playwright (Python) automation scripts.

Features include:

* Browser setup
* Assertions
* Comments
* Best practices
* Ready-to-run Python code

---

## 🌐 Website URL Scanner

Analyze a website and automatically detect:

* Forms
* Buttons
* Input Fields
* Links

Generate:

* AI Test Cases
* AI Playwright Automation Scripts

---

## 🐞 AI Failure Analysis

Analyze automation failures and identify:

* Root Cause
* Possible Fixes
* Debugging Recommendations
* Technical Explanation

---

## 🤖 Google Gemini AI

Powered by Google's Gemini Large Language Model to transform requirements into actionable QA artifacts.

---

# 🏗 Architecture

```
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
                REST API Calls
                      │
                      ▼
               FastAPI Backend
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
     Test Generator  Scanner  Failure Analyzer
                      │
                      ▼
                 Google Gemini
```

---

# 🛠 Tech Stack

### Backend

* FastAPI
* Python
* Google Gemini AI

### Frontend

* Streamlit

### Automation

* Playwright
* Pytest

### AI

* Google Gemini 2.5 Flash

### Other

* BeautifulSoup
* Requests
* Git
* GitHub

---

# 📁 Project Structure

```
AI_QA_Agent_Pro/
│
├── app/
│   ├── __init__.py
│   │
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── gemini_client.py
│   │   ├── generators.py
│   │   ├── url_scanner.py
│   │   ├── analyzer.py
│   │   └── export_utils.py
│   │
│   └── frontend/
│       └── ui.py
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

# 🔑 Configure Gemini API

Create the following file:

```
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

---

# ▶ Running the Application

## Start Backend

```bash
uvicorn app.backend.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start Frontend

```bash
python -m streamlit run app/frontend/ui.py
```

Frontend:

```
http://localhost:8501
```

---

# 📊 Current Backend APIs

| Method | Endpoint               | Description                |
| ------ | ---------------------- | -------------------------- |
| GET    | `/`                    | Health Check               |
| POST   | `/generate-testcases`  | Generate AI Test Cases     |
| POST   | `/generate-playwright` | Generate Playwright Script |

---

# 💡 Example

## Requirement

```
Login page with Email, Password and Login button.
```

AI QA Agent Pro generates:

* Detailed QA Test Cases
* Playwright Automation Script
* Testing Recommendations

---

# 📈 Proof of Concept (POC)

The application has been validated against real-world QA scenarios.

### Results

| Module                  | Status |
| ----------------------- | ------ |
| AI Test Case Generation | ✅ PASS |
| Playwright Generation   | ✅ PASS |
| Failure Analysis        | ✅ PASS |
| FastAPI Integration     | ✅ PASS |
| Streamlit Integration   | ✅ PASS |

---

# 🚀 Upcoming Features

* API Test Case Generator (Swagger/OpenAPI)
* Selenium Java Generator
* Accessibility Testing (WCAG)
* AI Test Strategy Generator
* AI Bug Report Generator
* Excel Export
* PDF Reports
* User Authentication (JWT)
* PostgreSQL Database
* Project History
* Docker Support
* CI/CD Pipeline
* Cloud Deployment (Azure/Render)

---

# 👨‍💻 Author

**Anish Sinha**

QA Automation Engineer | Python | Playwright | FastAPI | AI-Powered Testing

GitHub:

https://github.com/anishsinha2112

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

💡 Contribute with ideas and improvements

Happy Testing! 🚀
