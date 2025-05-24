import streamlit as st
from src.generator import generate_test_suggestions
from src.home import homepage

st.set_page_config(page_title="CI/CD Test Suggestion Tool", layout="wide")

# Render homepage layout
homepage()

uploaded_files = st.file_uploader("📂 Upload one or more CI/CD files (YAML, Dockerfile, Bash)", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        code = file.read().decode("utf-8")
        st.subheader(f"📝 {file.name}")
        edited_code = st.text_area("Edit file content (optional)", code, height=300, key=file.name)
        if st.button(f"🧪 Suggest Tests for {file.name}"):
            with st.spinner("Generating suggestions..."):
                suggestions = generate_test_suggestions(edited_code)
                st.markdown(suggestions)
                st.download_button("💾 Download Suggestions", data=suggestions, file_name=f"{file.name}_suggestions.md")
