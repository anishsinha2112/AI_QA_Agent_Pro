from google import genai
import streamlit as st

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def generate_test_cases(requirement):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate detailed QA test cases for: {requirement}"
    )

    return response.text


def generate_playwright_script(requirement):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate a Playwright Python script for: {requirement}"
    )

    return response.text