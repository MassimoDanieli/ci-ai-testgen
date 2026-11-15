> [!WARNING]
> **Progetto archiviato (novembre 2026).** Questo prototipo del 2025 chiamava `gpt-3.5-turbo`, che OpenAI ha spento il 23 ottobre 2026: non funziona più.
> Le sue funzioni ora vivono in **[ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit)**: proposte di test eseguibili per i file cambiati in una PR (`aikit testgen` / workflow `ai-testgen.yml`), con qualsiasi fornitore (Anthropic, OpenAI o un modello locale).
>
> *Archived (November 2026): this 2025 prototype called `gpt-3.5-turbo`, shut down by OpenAI on 23 October 2026. Its features live on in [ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit) (`aikit testgen`).*

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
