from pathlib import Path
import mimetypes

from google.genai import types

from .gemini_client import client


# ==========================================================
# AI Bug Report Generator
# ==========================================================

def generate_bug_report(image_path: str, error_log: str, requirement: str):

    mime_type, _ = mimetypes.guess_type(image_path)

    if mime_type is None:
        mime_type = "image/png"

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    prompt = f"""
You are a Senior QA Automation Engineer.

Analyze the uploaded screenshot together with the provided error log
and software requirement.

Software Requirement:
{requirement}

Error Log:
{error_log}

Generate a professional bug report.

Return the report in Markdown.

Include these sections:

# Bug Summary

# Description

# Environment

# Preconditions

# Steps to Reproduce

# Expected Result

# Actual Result

# Severity

# Priority

# Possible Root Cause

# Suggested Fix

# Regression Test Suggestions
"""

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