import streamlit as st
from src.generator import generate_test_suggestions

st.set_page_config(page_title="CI/CD Test Suggestion Tool", layout="wide")

st.title("🧠 AI Test Generator for CI/CD Pipelines")

uploaded_files = st.file_uploader("📂 Carica uno o più file YAML, Dockerfile o Bash", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        code = file.read().decode("utf-8")
        st.subheader(f"📝 {file.name}")
        edited_code = st.text_area("Modifica il contenuto del file (opzionale)", code, height=300, key=file.name)
        if st.button(f"🧪 Suggerisci Test per {file.name}"):
            with st.spinner("Generazione suggerimenti..."):
                suggestions = generate_test_suggestions(edited_code)
                st.markdown(suggestions)
                st.download_button("💾 Scarica suggerimenti", data=suggestions, file_name=f"{file.name}_suggestions.md")
