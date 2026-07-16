from pathlib import Path
import mimetypes

from google.genai import types

from .gemini_client import client


# ==========================================================
# Screenshot Analyzer
# ==========================================================

def analyze_screenshot(
    image_path: str,
    context: str = ""
):

    prompt = f"""
You are a Senior QA Automation Engineer with over 15 years of experience.

Analyze the uploaded application screenshot together with the additional QA context provided below.

===========================================================
Additional QA Context
===========================================================

{context}

===========================================================
Instructions
===========================================================

Generate a professional QA analysis report.

Return the response in Markdown.

Include all of the following sections.

# UI Summary

Provide a brief overview of the screen.

# Functional Components

Identify every visible component such as:

- Buttons
- Forms
- Input Fields
- Dropdowns
- Tables
- Navigation
- Dialogs
- Cards
- Icons

# Functional Observations

Describe how the UI appears to behave based on the screenshot and QA context.

# UI Issues

Identify:

- Alignment
- Spacing
- Fonts
- Colors
- Inconsistent Design
- Missing Elements
- Broken Layouts

# Accessibility Issues

Review using WCAG best practices.

Check for:

- Missing Labels
- Low Contrast
- Small Text
- Keyboard Accessibility
- Focus Visibility
- Screen Reader Concerns

# UX Improvements

Suggest improvements to enhance usability.

# Functional Test Scenarios

Generate useful manual QA test cases.

# Automation Opportunities

Suggest automation using:

- Selenium
- Playwright
- API Testing
- Accessibility Automation

# Risk Assessment

Categorize findings as:

- High Risk
- Medium Risk
- Low Risk

# Overall Recommendation

Summarize the QA findings and recommend the next actions.

If additional QA context has been provided, use it together with the screenshot to produce a more accurate and relevant analysis.

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