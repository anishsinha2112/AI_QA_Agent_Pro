import os
import sys
import requests
import streamlit as st

# ==========================================================
# API URL
# ==========================================================

API_URL = st.secrets["API_URL"]

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

from app.backend.export_utils import (
    export_to_pdf,
    export_to_docx,
    export_to_excel,
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI QA Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI QA Agent")
st.caption(
    "AI Powered Test Case, Automation Script & Failure Analysis Tool"
)

# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📝 Test Generation",
    "🌐 Website Scanner",
    "🐞 Failure Analysis",
    "📋 Test Strategy",
    "🤖 AI QA Assistant"
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

    # ------------------------------------------------------
    # Generate Test Cases
    # ------------------------------------------------------

    with col1:

        if st.button("📝 Generate Test Cases"):

            if requirement:

                with st.spinner("Generating Test Cases..."):

                    try:

                        response = requests.post(
                            f"{API_URL}/generate-testcases",
                            json={
                                "requirement": requirement
                            },
                            timeout=180
                        )

                        if response.status_code == 200:

                            result = response.json()["result"]

                            st.success("✅ Test Cases Generated")

                            st.markdown(result)

                            pdf_file = export_to_pdf(
                                "AI Generated Test Cases",
                                result
                            )

                            docx_file = export_to_docx(
                                "AI Generated Test Cases",
                                result
                            )
                            excel_file = export_to_excel(
                            "AI Generated Test Cases",
                            result
                            )

                            pdf_col, doc_col, excel_col = st.columns(3)

                            with pdf_col:

                                st.download_button(
                                    "📄 Download PDF",
                                    data=pdf_file,
                                    file_name="AI_Test_Cases.pdf",
                                    mime="application/pdf"
                                )

                            with doc_col:

                                st.download_button(
                                    "📝 Download Word",
                                    data=docx_file,
                                    file_name="AI_Test_Cases.docx",
                                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                )

                            with excel_col:

                                st.download_button(
                                   "📊 Download Excel",
                                   data=excel_file,
                                   file_name="AI_Test_Cases.xlsx",
                                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                                )

                        else:

                            st.error(response.text)

                    except Exception as e:

                        st.error(f"Backend Error\n\n{e}")

            else:

                st.warning("Please enter a requirement.")

    # ------------------------------------------------------
    # Generate Playwright Script
    # ------------------------------------------------------

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
                            timeout=180
                        )

                        if response.status_code == 200:

                            result = response.json()["result"]

                            st.success("✅ Playwright Script Generated")

                            st.code(
                                result,
                                language="python"
                            )

                            st.download_button(
                                "📥 Download Python Script",
                                data=result,
                                file_name="generated_playwright.py",
                                mime="text/x-python"
                            )

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

    # ------------------------------------------------------
    # Analyze Website
    # ------------------------------------------------------

    if st.button("🔍 Analyze Website"):

        if url:

            with st.spinner("Scanning Website..."):

                scan_result = scan_website(url)

            st.success("✅ Website Scan Completed")

            st.json(scan_result)

        else:

            st.warning("Please enter a website URL.")

    # ------------------------------------------------------
    # Generate Test Cases From Website
    # ------------------------------------------------------

    if st.button("📝 Generate Test Cases From Website"):

        if url:

            with st.spinner("Generating AI Test Cases..."):

                scan_result = scan_website(url)

                result = generate_website_test_cases(
                    scan_result
                )

            st.success("✅ Test Cases Generated")

            st.markdown(result)

            pdf_file = export_to_pdf(
                "Website Test Cases",
                result
            )

            docx_file = export_to_docx(
                "Website Test Cases",
                result
            )

            col1, col2 = st.columns(2)

            with col1:

                st.download_button(
                    "📄 Download PDF",
                    data=pdf_file,
                    file_name="Website_Test_Cases.pdf",
                    mime="application/pdf"
                )

            with col2:

                st.download_button(
                    "📝 Download Word",
                    data=docx_file,
                    file_name="Website_Test_Cases.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

        else:

            st.warning("Please enter a website URL.")

    # ------------------------------------------------------
    # Generate Playwright Script
    # ------------------------------------------------------

    if st.button("⚡ Generate Playwright Script From Website"):

        if url:

            with st.spinner("Generating Playwright Script..."):

                scan_result = scan_website(url)

                result = generate_playwright_from_website(
                    url,
                    scan_result
                )

            st.success("✅ Playwright Script Generated")

            st.code(
                result,
                language="python"
            )

            st.download_button(
                "📥 Download Python Script",
                data=result,
                file_name="website_playwright.py",
                mime="text/x-python"
            )

        else:

            st.warning("Please enter a website URL.")

# ==========================================================
# TAB 3 - FAILURE ANALYSIS
# ==========================================================

with tab3:

    st.subheader("🐞 AI Failure Analysis")

    failure_log = st.text_area(
        "Paste Selenium / Playwright / Appium / API Error Log",
        height=250,
        placeholder="Paste automation failure logs here..."
    )

    if st.button("🔍 Analyze Failure"):

        if failure_log:

            with st.spinner("Analyzing Failure..."):

                result = classify_failure(failure_log)

            st.success("✅ Failure Analysis Completed")

            st.markdown(result)

            pdf_file = export_to_pdf(
                "Failure Analysis Report",
                result
            )

            docx_file = export_to_docx(
                "Failure Analysis Report",
                result
            )

            col1, col2 = st.columns(2)

            with col1:

                st.download_button(
                    "📄 Download PDF",
                    data=pdf_file,
                    file_name="Failure_Analysis_Report.pdf",
                    mime="application/pdf"
                )

            with col2:

                st.download_button(
                    "📝 Download Word",
                    data=docx_file,
                    file_name="Failure_Analysis_Report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

        else:

            st.warning("Please paste the failure log.")

# ==========================================================
# TAB 4 - TEST STRATEGY
# ==========================================================

with tab4:

    st.subheader("📋 AI Test Strategy Generator")

    strategy_requirement = st.text_area(
        "Software Requirement",
        height=200,
        placeholder="""
Example:
Build an Online Banking Application with Login,
Fund Transfer,
Transaction History,
Bill Payments,
Admin Portal,
Notification Service.
"""
    )

    if st.button("📋 Generate Test Strategy"):

        if strategy_requirement:

            with st.spinner("Generating AI Test Strategy..."):

                try:

                    response = requests.post(
                        f"{API_URL}/generate-test-strategy",
                        json={
                            "requirement": strategy_requirement
                        },
                        timeout=240
                    )

                    if response.status_code == 200:

                        result = response.json()["result"]

                        st.success("✅ Test Strategy Generated Successfully")

                        st.markdown(result)

                        # -----------------------------------------
                        # Export Files
                        # -----------------------------------------

                        pdf_file = export_to_pdf(
                            "AI Test Strategy",
                            result
                        )

                        docx_file = export_to_docx(
                            "AI Test Strategy",
                            result
                        )

                        col1, col2, col3 = st.columns(3)

                        with col1:

                            st.download_button(
                                "📄 Download PDF",
                                data=pdf_file,
                                file_name="AI_Test_Strategy.pdf",
                                mime="application/pdf"
                            )

                        with col2:

                            st.download_button(
                                "📝 Download Word",
                                data=docx_file,
                                file_name="AI_Test_Strategy.docx",
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            )

                        with col3:

                            st.download_button(
                                "📥 Download Markdown",
                                data=result,
                                file_name="AI_Test_Strategy.md",
                                mime="text/markdown"
                            )

                    else:

                        st.error(response.text)

                except Exception as e:

                    st.error(f"Backend Error\n\n{e}")

        else:

            st.warning("Please enter a software requirement.")





# ==========================================================
# TAB 5 - AI QA Assistant
# ==========================================================

with tab5:

    st.subheader("🤖 AI QA Assistant")

    st.write(
        "Ask anything related to QA, Selenium, Playwright, APIs, SQL, Python, Appium, Test Strategy, CI/CD, or software testing."
    )

    question = st.text_area(
        "Ask Your Question",
        height=180,
        placeholder="Example: Explain Selenium TimeoutException."
    )

    if st.button("🤖 Ask AI"):

        if question.strip():

            with st.spinner("Thinking..."):

                try:

                    response = requests.post(
                        f"{API_URL}/chat",
                        json={"question": question},
                        timeout=180
                    )

                    if response.status_code == 200:

                        result = response.json()["result"]

                        st.success("✅ Response Generated")

                        st.markdown(result)

                    else:

                        st.error(response.text)

                except Exception as e:

                    st.error(f"Backend Error\n\n{e}")

        else:

            st.warning("Please enter a question.")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
### 🚀 AI QA Agent Pro

Built with:

- 🐍 Python
- ⚡ FastAPI
- 🎨 Streamlit
- 🤖 Google Gemini AI
- 🎭 Playwright
- 🧪 Pytest

**Created by Anish Sinha**
"""
)