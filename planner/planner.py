from llm.ollama_client import query_ollama

# Learning Block 1 note:
# The dangerous_eval function below is intentionally unsafe so CodeQL has a real code path
# to analyze. Do not copy this pattern into production code.

''' This vulnerable code is intentionally included to demonstrate the risks of executing untrusted input. In a real application, never use eval or os.system with user input without proper sanitization and validation. The password variable is included as a placeholder to illustrate that sensitive information could be exposed if the code is exploited.

'''

def dangerous_eval():
    user_input = input("Enter code: ")
    return eval(user_input)

def get_plan(cve):
    prompt = (
        f"Provide a concise step-by-step mitigation plan for {cve['cve']} "
        f"with description: {cve['desc']} and CVSS {cve.get('cvss', 'unknown')}."
    )
    return query_ollama(prompt)