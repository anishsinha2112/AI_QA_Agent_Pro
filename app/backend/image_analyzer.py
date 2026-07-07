from pathlib import Path
import mimetypes

from google.genai import types

from .gemini_client import client


# ==========================================================
# Screenshot Analyzer
# ==========================================================

def analyze_screenshot(image_path: str):

    prompt = """
You are a Senior QA Automation Engineer with 15 years of experience.

Analyze this application screenshot.

Generate a professional QA report.

Include the following sections.

# UI Summary

Provide a brief description.

# Functional Components

Identify all visible UI controls.

# UI Issues

Mention alignment, spacing, fonts, colors, consistency.

# Accessibility Issues

Check for:

- Missing labels
- Low contrast
- Small text
- Keyboard accessibility concerns
- WCAG observations

# UX Improvements

Suggest improvements.

# Functional Test Scenarios

Generate useful manual test cases.

# Automation Opportunities

Suggest:

- Playwright
- Selenium
- API Testing
- Accessibility Automation

# Risk Assessment

High

Medium

Low

# Overall Recommendation

Summarize the QA findings.

Return Markdown only.
"""

    mime_type, _ = mimetypes.guess_type(image_path)

    if mime_type is None:
        mime_type = "image/png"

    with open(image_path, "rb") as image_file:

        image_bytes = image_file.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type,
            ),
        ],
    )

    return response.text