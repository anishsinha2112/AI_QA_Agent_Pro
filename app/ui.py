
import streamlit as st
from generators import generate_test_cases, generate_playwright_script
from analyzer import classify_failure


st.title("AI QA Agent")

req = st.text_area("Requirement")

if st.button("Generate Test Cases"):
    st.write(generate_test_cases(req))

if st.button("Generate Playwright Script"):
    st.code(generate_playwright_script(req))

error = st.text_area("Failure Log")

if st.button("Analyze Failure"):
    st.write(classify_failure(error))
