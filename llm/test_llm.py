from llm.ollama_client import query_ollama


if __name__ == "__main__":
    print(query_ollama("Summarize CVE-2024-1234 for a SOC analyst."))
