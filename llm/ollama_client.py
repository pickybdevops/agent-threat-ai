import requests

def query_ollama(prompt, model="deepseek-coder"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
    )
    return response.json()["response"].strip()
