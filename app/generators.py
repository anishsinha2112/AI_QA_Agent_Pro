import time
from gemini_client import client



# Generate Test Cases
def generate_test_cases(requirement):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Generate detailed QA test cases in a table format with:

- Test Case ID
- Test Scenario
- Test Steps
- Expected Result
- Priority

Requirement:
{requirement}
"""
)

            return response.text

        except Exception as e:

            if attempt < 2:
                time.sleep(3)

            else:
                return f"""⚠️ Gemini Service Busy

Google AI is experiencing high demand.

Please try again after 30 seconds.

Technical Error:
{str(e)}
"""


# Generate Playwright Script
def generate_playwright_script(requirement):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
Generate a complete Playwright Python automation script for:

{requirement}

Include:
- Imports
- Browser Launch
- Assertions
- Comments
"""
        )

        return response.text

    except Exception as e:
       error = str(e)

    if "RESOURCE_EXHAUSTED" in error:
        return """
⚠️ Gemini API quota reached.

Please wait a few minutes and try again.

If the problem continues:
• Create a new Gemini project
• Or enable billing
"""

    if "UNAVAILABLE" in error:
        return """
⚠️ Gemini servers are currently busy.

Please try again in 30–60 seconds.
"""

    return f"Error:\n{error}"