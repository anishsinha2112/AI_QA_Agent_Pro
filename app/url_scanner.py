import requests
from bs4 import BeautifulSoup
from gemini_client import client




# -------------------------------------
# Website Scanner
# -------------------------------------
def scan_website(url):
    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        forms = len(soup.find_all("form"))
        buttons = len(soup.find_all("button"))
        links = len(soup.find_all("a"))
        inputs = len(soup.find_all("input"))

        return {
            "url": url,
            "forms": forms,
            "buttons": buttons,
            "links": links,
            "inputs": inputs
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------------------
# Generate Test Cases From Website
# -------------------------------------
def generate_website_test_cases(scan_result):

    try:

        prompt = f"""
You are a Senior QA Engineer.

Generate detailed QA test cases based on the following website information:

{scan_result}

Include:
- Positive test cases
- Negative test cases
- UI validation
- Functional validation
- Boundary scenarios

Format:

Test Case ID
Scenario
Steps
Expected Result
Priority
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error generating test cases: {str(e)}"


# -------------------------------------
# Generate Playwright Script
# -------------------------------------
def generate_playwright_from_website(url, scan_result):

    try:

        prompt = f"""
You are a Senior SDET.

Website URL:
{url}

Website Details:
{scan_result}

Generate a Playwright Python automation script.

Requirements:
- Use pytest
- Use Playwright sync API
- Include assertions
- Add comments
- Follow Page Object Model principles where possible

Return only Python code.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
      error = str(e)

    if "RESOURCE_EXHAUSTED" in error:
        return """
⚠️ Gemini API quota exceeded.

Please wait a few minutes and try again.

If the issue continues:
• Use another Gemini project
• Or enable billing
"""

    if "UNAVAILABLE" in error:
        return """
⚠️ Gemini servers are currently busy.

Please try again after a minute.
"""

    return f"Error:\n{error}"