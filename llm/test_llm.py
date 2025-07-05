# test_llm.py
from llm.ollama_client import query_ollama
print(query_ollama("Summarize CVE-2024-1234 for a SOC analyst."))
