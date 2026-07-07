from pathlib import Path

from google.genai import types

from .gemini_client import client


# ==========================================================
# Screenshot Analyzer
# ==========================================================

def analyze_screenshot(image_path: str):

    prompt = """
You are a Senior QA Engineer.

Analyze this UI screenshot.

Provide a detailed report using the following format.

# UI Summary

# Functional Observations

# UI Issues

# Accessibility Issues

# UX Improvements

# Test Scenarios

# Automation Opportunities

# Overall QA Recommendation

Return the response in Markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            types.Part.from_bytes(
                data=Path(image_path).read_bytes(),
                mime_type="image/png",
            ),
        ],
    )

    return response.text