# 🧠 CI/CD AI Test Generator

Uno strumento basato su Streamlit + GPT per analizzare file di pipeline (GitHub Actions, GitLab, Jenkinsfile, Dockerfile, shell) e suggerire test automatici mancanti.

## 🚀 Come si usa

1. `pip install -r requirements.txt`
2. `streamlit run ci_testgen_app.py`
3. Carica un file `.yml`, `.sh`, `Dockerfile`
4. Premi “🧪 Suggerisci Test”
5. Scarica l’output in `.md`

## 📦 File inclusi

- `ci_testgen_app.py` — App Streamlit
- `src/generator.py` — Modulo AI
- `requirements.txt` — Dipendenze
