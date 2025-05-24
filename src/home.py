import streamlit as st

def homepage():
    st.markdown("""
    <style>
    .big-title {
        font-size: 28px;
        font-weight: bold;
        color: #4B8BBE;
        text-align: center;
    }
    .sub-title {
        font-size: 18px;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>

    <div class="big-title">🧠 CI/CD AI Test Generator</div>
    <div class="sub-title">Upload your CI files and let GPT suggest test cases for pipelines, Docker, and shell scripts</div>
    """, unsafe_allow_html=True)

    with st.expander("📘 What does this app do?"):
        st.markdown("""
        - Upload a `.yml`, `Dockerfile`, or `bash` script
        - The AI will suggest:
            - Tests to verify each command
            - Error handling checks
            - Example test code in bash or pytest
        - Then you can download a `.md` file with all suggestions
        """)

    col1, col2 = st.columns([2, 1])

    with col2:
        st.markdown("### 🚀 How to use")
        st.markdown("""
        1. Upload your CI/CD file(s)
        2. (Optional) Edit the content
        3. Click “Suggest Tests”
        4. Review and download the results
        """)
