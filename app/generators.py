import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_test_cases(requirement):
    response = model.generate_content(
        f"Generate detailed QA test cases for: {requirement}"
    )
    return response.text

def generate_playwright_script(requirement):
    response = model.generate_content(
        f"Generate a Playwright Python script for: {requirement}"
    )
    return response.text