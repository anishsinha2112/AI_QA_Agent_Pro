import time
from .gemini_client import client


# ==========================================================
# Common Gemini Request Function
# ==========================================================

def call_gemini(prompt, retries=3):
    """
    Sends a prompt to Gemini AI with retry logic.
    """

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error = str(e)

            # Retry for temporary server issues
            if "UNAVAILABLE" in error and attempt < retries - 1:
                time.sleep(3)
                continue

            if "RESOURCE_EXHAUSTED" in error:
                return """
⚠️ Gemini API quota exceeded.

Please wait a few minutes and try again.

If the issue continues:
• Create another Gemini Project
• Or enable billing.
"""

            if "UNAVAILABLE" in error:
                return """
⚠️ Gemini servers are currently busy.

Please try again after a minute.
"""

            return f"Error:\n\n{error}"


# ==========================================================
# Generate Test Cases
# ==========================================================

def generate_test_cases(requirement):

    prompt = f"""
Generate detailed QA test cases in a table format with:

- Test Case ID
- Test Scenario
- Test Steps
- Expected Result
- Priority

Requirement:
{requirement}
"""

    return call_gemini(prompt)


# ==========================================================
# Generate Playwright Script
# ==========================================================

def generate_playwright_script(requirement):

    prompt = f"""
Generate a complete Playwright Python automation script for:

{requirement}

Include:

- Imports
- Browser Launch
- Assertions
- Comments
- Best Practices

Return only Python code.
"""

    return call_gemini(prompt)


# ==========================================================
# Generate AI Test Strategy
# ==========================================================

def generate_test_strategy(requirement):

    prompt = f"""
You are a Principal QA Architect with over 15 years of experience.

Prepare a complete Test Strategy document for the following software requirement.

Requirement:
{requirement}

Include the following sections:

# Project Overview

# Testing Objectives

# Testing Scope

## In Scope

## Out of Scope

# Test Levels

- Unit Testing
- Integration Testing
- System Testing
- User Acceptance Testing (UAT)

# Functional Testing Strategy

# API Testing Strategy

# Database Testing Strategy

# UI Testing Strategy

# Mobile Testing Strategy (if applicable)

# Security Testing

# Performance Testing

# Accessibility Testing

# Compatibility Testing

# Regression Testing

# Smoke Testing

# Automation Strategy

Include:
- Recommended Automation Tools
- What should be automated
- What should remain manual

# Risk Analysis

Provide a Risk | Impact | Mitigation table.

# Test Environment

# Entry Criteria

# Exit Criteria

# Test Deliverables

# Defect Management Process

# Test Metrics

Return the response in well-formatted Markdown.
"""

    return call_gemini(prompt)

def chat_with_ai(question):

    prompt = f"""
You are an Expert QA Automation Engineer.

Question:
{question}

Provide:
1. Explanation
2. Best Practices
3. Example
4. Conclusion

Return the response in Markdown.
"""

    return call_gemini(prompt)