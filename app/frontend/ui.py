import os
import sys

import requests
import streamlit as st

# ==========================================================
# API URL
# ==========================================================

API_URL = st.secrets["https://ai-qa-agent-pro.onrender.com"]

# ==========================================================
# Add Project Root
# ==========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Backend Imports
# ==========================================================

from app.backend.url_scanner import (
    scan_website,
    generate_website_test_cases,
    generate_playwright_from_website,
)

from app.backend.analyzer import classify_failure


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI QA Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI QA Agent")
st.caption("AI Powered Test Case, Automation Script & Failure Analysis Tool")


# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Test Generation",
    "🌐 URL Scanner",
    "🐞 Failure Analysis",
    "📋 Test Strategy"
])


# ==========================================================
# TAB 1 - TEST GENERATION
# ==========================================================

with tab1:

    st.subheader("Generate Test Cases & Automation Scripts")

    requirement = st.text_area(
        "Requirement / User Story",
        height=180,
        placeholder="Example: Login page with Email and Password"
    )

    col1, col2 = st.columns(2)

    # --------------------------------------------------
    # Generate Test Cases
    # --------------------------------------------------

    with col1:

        if st.button("📝 Generate Test Cases"):

            if requirement:

                with st.spinner("Generating Test Cases..."):

                    try:

                        response = requests.post(
                         f"{API_URL}/generate-testcases",
                         json={"requirement": requirement},
                         timeout=120
                        )
                        if response.status_code == 200:

                            result = response.json()["result"]

                            st.success("✅ Test Cases Generated")

                            st.write(result)

                        else:

                            st.error(response.text)

                    except Exception as e:

                        st.error(f"Backend Error\n\n{e}")

            else:

                st.warning("Please enter a requirement.")

    # --------------------------------------------------
    # Generate Playwright Script
    # --------------------------------------------------

    with col2:

        if st.button("⚡ Generate Playwright Script"):

            if requirement:

                with st.spinner("Generating Playwright Script..."):

                    try:

                        response = requests.post(
                            f"{API_URL}/generate-playwright",
                            json={
                                "requirement": requirement
                            },
                            timeout=120
                        )

                        if response.status_code == 200:

                            result = response.json()["result"]

                            st.success("✅ Playwright Script Generated")

                            st.code(result, language="python")

                        else:

                            st.error(response.text)

                    except Exception as e:

                        st.error(f"Backend Error\n\n{e}")

            else:

                st.warning("Please enter a requirement.")


# ==========================================================
# TAB 2 - WEBSITE SCANNER
# ==========================================================

with tab2:

    st.subheader("🌐 Website URL Scanner")

    url = st.text_input(
        "Website URL",
        placeholder="https://example.com"
    )

    if st.button("🔍 Analyze Website"):

        if url:

            with st.spinner("Scanning Website..."):

                result = scan_website(url)

            st.success("Website Scan Completed")

            st.json(result)

        else:

            st.warning("Please enter a website URL.")

    if st.button("📝 Generate Test Cases From Website"):

        if url:

            with st.spinner("Generating Test Cases..."):

                scan_result = scan_website(url)

                result = generate_website_test_cases(scan_result)

            st.success("Generated Successfully")

            st.write(result)

            st.download_button(
                "📥 Download Test Cases",
                result,
                file_name="website_test_cases.txt"
            )

        else:

            st.warning("Please enter a website URL.")

    if st.button("⚡ Generate Playwright Script From Website"):

        if url:

            with st.spinner("Generating Playwright Script..."):

                scan_result = scan_website(url)

                result = generate_playwright_from_website(
                    url,
                    scan_result
                )

            st.success("Generated Successfully")

            st.code(result, language="python")

            st.download_button(
                "📥 Download Script",
                result,
                file_name="playwright.py"
            )

        else:

            st.warning("Please enter a website URL.")


# ==========================================================
# TAB 3 - FAILURE ANALYSIS
# ==========================================================

with tab3:

    st.subheader("🐞 Failure Analysis")

    log = st.text_area(
        "Paste Failure Log",
        height=250
    )

    if st.button("Analyze Failure"):

        if log:

            with st.spinner("Analyzing Failure..."):

                result = classify_failure(log)

            st.success("Analysis Completed")

            st.write(result)

        else:

            st.warning("Please paste the failure log.")


# ==========================================================
# TAB 4 - TEST STRATEGY
# ==========================================================

with tab4:

    st.subheader("📋 AI Test Strategy Generator")

    strategy_requirement = st.text_area(
        "Software Requirement",
        height=180,
        placeholder="Example: Build an online banking application."
    )

    if st.button("📋 Generate Test Strategy"):

        if strategy_requirement:

            with st.spinner("Generating Test Strategy..."):

                try:

                    response = requests.post(
                        f"{API_URL}/generate-test-strategy",
                        json={
                            "requirement": strategy_requirement
                        },
                        timeout=180
                    )

                    if response.status_code == 200:

                        result = response.json()["result"]

                        st.success("✅ Test Strategy Generated Successfully")

                        st.markdown(result)

                        st.download_button(
                            "📥 Download Strategy",
                            result,
                            file_name="test_strategy.md",
                            mime="text/markdown"
                        )

                    else:

                        st.error(response.text)

                except Exception as e:

                    st.error(f"Backend Error\n\n{e}")

        else:

            st.warning("Please enter a software requirement.")


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")
st.caption("🚀 Created by Anish Sinha | AI QA Agent")