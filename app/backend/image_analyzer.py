from pathlib import Path
import mimetypes

from google.genai import types

from .gemini_client import client


# ==========================================================
# Screenshot Analyzer
# ==========================================================

def analyze_screenshot(image_path: str):

    prompt = """
You are a Senior QA Engineer.

Analyze this UI screenshot.

Provide the report in the following format:

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