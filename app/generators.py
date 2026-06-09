from google import genai
import streamlit as st

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def generate_test_cases(requirement):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
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
        return f"⚠️ Gemini Service Busy. Please try again in a few minutes.\n\nError: {str(e)}"


def generate_playwright_script(requirement):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
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
        return f"⚠️ Unable to generate Playwright script.\n\nError: {str(e)}"