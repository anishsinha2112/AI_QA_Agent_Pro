from fastapi import FastAPI

from .models import RequirementRequest
from .generators import (
    generate_test_cases,
    generate_playwright_script,
    generate_test_strategy
)

print("🚀 LOADING NEW MAIN.PY")
print("generate_test_strategy imported successfully")

app = FastAPI(
    title="AI QA Agent API",
    version="1.0.0"
)


# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():
    return {
        "message": "AI QA Agent Backend Running 🚀"
    }


# ==========================================================
# Generate Test Cases
# ==========================================================

@app.post("/generate-testcases")
def generate_tc(request: RequirementRequest):

    result = generate_test_cases(request.requirement)

    return {
        "status": "success",
        "result": result
    }


# ==========================================================
# Generate Playwright Script
# ==========================================================

@app.post("/generate-playwright")
def generate_pw(request: RequirementRequest):

    result = generate_playwright_script(request.requirement)

    return {
        "status": "success",
        "result": result
    }


# ==========================================================
# Generate Test Strategy
# ==========================================================

@app.post("/generate-test-strategy")
def generate_strategy(request: RequirementRequest):

    result = generate_test_strategy(request.requirement)

    return {
        "status": "success",
        "result": result
    }