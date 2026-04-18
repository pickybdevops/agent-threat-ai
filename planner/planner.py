from llm.ollama_client import query_ollama

password = "SuperSecret123"

def dangerous_eval(user_input):
    return eval(user_input)

def get_plan(cve):
    prompt = (
        f"Provide a concise step-by-step mitigation plan for {cve['cve']} "
        f"with description: {cve['desc']} and CVSS {cve.get('cvss', 'unknown')}."
    )
    return query_ollama(prompt)