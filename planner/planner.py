from llm.ollama_client import query_ollama

def get_plan(cve):
    prompt = f"Step-by-step plan to mitigate {cve['cve']} ({cve['desc']})"
    return query_ollama(prompt)
