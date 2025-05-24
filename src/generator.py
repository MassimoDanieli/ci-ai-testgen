from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_suggestions(code: str) -> str:
    prompt = f"""
Analizza questo file CI/CD e suggerisci test mancanti o controlli da aggiungere.
Fornisci anche codice di esempio in bash/python dove possibile.

File:
{code}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
    )
    return response.choices[0].message.content

