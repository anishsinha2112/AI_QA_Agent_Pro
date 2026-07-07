import os

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

from fastapi import FastAPI

from fastapi import FastAPI, UploadFile, File

from .image_analyzer import analyze_screenshot



from .models import (
    RequirementRequest,
    ChatRequest
)
from .generators import (
    generate_test_cases,
    generate_playwright_script,
    generate_test_strategy,
    chat_with_ai
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

# ==========================================================
# AI QA Assistant
# ==========================================================

@app.post("/chat")
def chat(request: ChatRequest):

    result = chat_with_ai(request.question)

    return {
        "status": "success",
        "result": result
    }

# ==========================================================
# Screenshot Analyzer
# ==========================================================

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = analyze_screenshot(file_path)

    return {
        "status": "success",
        "result": result
    }