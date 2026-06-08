# AI QA Agent 🚀

AI QA Agent is an intelligent testing assistant built using Python, Streamlit, Playwright, and Generative AI. It helps QA Engineers and Test Automation Engineers generate test cases, automation scripts, and improve testing productivity.

## Features

### Test Case Generation

* Generate detailed QA test cases from business requirements
* Positive test scenarios
* Negative test scenarios
* Edge case coverage

### Playwright Script Generation

* Generate Playwright Python automation scripts
* Reduce manual scripting effort
* Accelerate automation development

### Failure Analysis

* Analyze test execution failures
* Identify possible root causes
* Assist in debugging automation issues

### AI-Powered Testing

* Uses Generative AI (Gemini)
* Converts requirements into actionable test artifacts

---

## Tech Stack

* Python
* Streamlit
* Playwright
* Gemini AI
* Git & GitHub

---

## Project Structure

```text
AI_QA_Agent_Pro/
│
├── app/
│   ├── __init__.py
│   ├── ui.py
│   ├── generators.py
│   ├── analyzer.py
│
├── playwright_tests/
│   └── sample_test.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/anishsinha2112/AI_QA_Agent_Pro.git
cd AI_QA_Agent_Pro
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create:

```text
C:\Users\<username>\.streamlit\secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## Run Application

```bash
streamlit run app/ui.py
```

Application will launch at:

```text
http://localhost:8501
```

---

## Sample Use Case

Requirement:

```text
Verify user signup functionality for the website.
```

AI QA Agent can:

* Generate QA Test Cases
* Generate Playwright Automation Script
* Provide testing recommendations

---

## Future Enhancements

* URL-based Test Case Generation
* Jira Integration
* Excel Export
* Defect Report Generation
* Root Cause Analysis
* AI-powered Regression Suite Generation

---

## Author

Anish Sinha

QA Automation Engineer | Python | Playwright | AI-Powered Testing

GitHub:
https://github.com/anishsinha2112


