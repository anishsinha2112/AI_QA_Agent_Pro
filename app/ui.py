import streamlit as st
from generators import generate_test_cases, generate_playwright_script
from analyzer import classify_failure

st.set_page_config(
    page_title="AI QA Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI QA Agent")
st.caption("AI Powered Test Case & Automation Script Generator")

tab1, tab2 = st.tabs(["📝 Test Generation", "🔍 Failure Analysis"])

with tab1:
    requirement = st.text_area(
        "Requirement",
        placeholder="Enter requirement or user story...",
        height=150
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Test Cases"):
            if requirement:
                result = generate_test_cases(requirement)
                st.subheader("Generated Test Cases")
                st.write(result)

    with col2:
        if st.button("Generate Playwright Script"):
            if requirement:
                result = generate_playwright_script(requirement)
                st.subheader("Generated Playwright Script")
                st.code(result, language="python")

with tab2:
    failure_log = st.text_area(
        "Failure Log",
        placeholder="Paste failure log here...",
        height=200
    )

    if st.button("Analyze Failure"):
        result = classify_failure(failure_log)
        st.subheader("Analysis Result")
        st.success(result)

st.markdown("---")
st.caption("Created by Anish Sinha | AI QA Agent")

with st.spinner("Generating test cases..."):
    result = generate_test_cases(requirement)

st.success("Generated successfully!")
st.write(result)