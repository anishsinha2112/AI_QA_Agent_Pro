import streamlit as st
from url_scanner import (
    scan_website,
    generate_website_test_cases,
    generate_playwright_from_website)
from generators import generate_test_cases, generate_playwright_script
from analyzer import classify_failure

st.write("Scanner Loaded")
st.write(scan_website)
st.write(generate_website_test_cases)
st.write(generate_playwright_from_website)

# Optional - only after creating url_scanner.py
# from url_scanner import scan_website

# Page Configuration
st.set_page_config(
    page_title="AI QA Agent",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 AI QA Agent")
st.caption("AI-Powered Test Case, Automation Script & Failure Analysis Tool")

# Tabs
tab1, tab2, tab3 = st.tabs([
    "📝 Test Generation",
    "🌐 URL Scanner",
    "🐞 Failure Analysis"
])

# ---------------------------------------------------
# TAB 1 - TEST GENERATION
# ---------------------------------------------------
with tab1:

    st.subheader("Generate Test Cases & Automation Scripts")

    requirement = st.text_area(
        "Requirement / User Story",
        placeholder="Enter requirement or user story...",
        height=150
    )

    col1, col2 = st.columns(2)

    # Generate Test Cases
    with col1:

        if st.button("📝 Generate Test Cases"):

            if requirement:

                with st.spinner("Generating Test Cases..."):

                    result = generate_test_cases(requirement)

                st.success("Test Cases Generated Successfully!")

                st.subheader("Generated Test Cases")

                st.write(result)

            else:
                st.warning("Please enter a requirement.")

    # Generate Playwright Script
    with col2:

        if st.button("⚡ Generate Playwright Script"):

            if requirement:

                with st.spinner("Generating Playwright Script..."):

                    result = generate_playwright_script(requirement)

                st.success("Playwright Script Generated!")

                st.subheader("Generated Playwright Script")

                st.code(result, language="python")

            else:
                st.warning("Please enter a requirement.")

# ---------------------------------------------------
# TAB 2 - URL SCANNER
# ---------------------------------------------------
with tab2:

    st.subheader("🌐 Website URL Scanner")

    url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com"
    )

    # Website Scan
    if st.button("🔍 Analyze Website"):

        if url:

            with st.spinner("Scanning Website..."):

                scan_result = scan_website(url)

            st.success("Website Scan Completed!")

            st.json(scan_result)

        else:
            st.warning("Please enter a URL.")

    # AI Test Cases
    if st.button("📝 Generate Test Cases From Website"):

        if url:

            with st.spinner("Generating AI Test Cases..."):

                scan_result = scan_website(url)

                test_cases = generate_website_test_cases(
                    scan_result
                )

            st.success("Test Cases Generated!")

            st.write(test_cases)

            st.download_button(
                label="📥 Download Test Cases",
                data=test_cases,
                file_name="website_test_cases.txt",
                mime="text/plain"
            )

        else:
            st.warning("Please enter a URL.")

    # AI Playwright Script
    if st.button("⚡ Generate Playwright Script From Website"):

        if url:

            with st.spinner("Generating Playwright Script..."):

                scan_result = scan_website(url)

                script = generate_playwright_from_website(
                    url,
                    scan_result
                )

            st.success("Playwright Script Generated!")

            st.code(script, language="python")

            st.download_button(
                label="📥 Download Playwright Script",
                data=script,
                file_name="generated_playwright.py",
                mime="text/plain"
            )

        else:
            st.warning("Please enter a URL.")
# ---------------------------------------------------
# TAB 3 - FAILURE ANALYSIS
# ---------------------------------------------------
with tab3:

    st.subheader("🐞 Failure Analysis")

    failure_log = st.text_area(
        "Paste Failure Log",
        placeholder="Paste Selenium, Playwright, Appium, or API error logs...",
        height=200
    )

    if st.button("Analyze Failure"):

        if failure_log:

            with st.spinner("Analyzing Failure..."):

                result = classify_failure(failure_log)

            st.success("Analysis Completed!")

            st.subheader("Analysis Result")

            st.write(result)

        else:
            st.warning("Please paste a failure log.")

# Footer
st.markdown("---")
st.caption("Created by Anish Sinha | AI QA Agent 🚀")