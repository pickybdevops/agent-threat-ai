"""Planning layer for the threat-response demo.

This module is intentionally kept small so it is easy to understand during the
first DevSecOps learning block.

What you should learn from this file:
- It contains normal application logic (`get_plan`)
- It also contains a deliberately unsafe helper (`dangerous_eval`) so CodeQL can
  demonstrate how SAST tools reason about risky code patterns.

Important:
- There is NO hardcoded password in this file anymore.
- That is intentional, because we want Gitleaks to pass by default and let you
  focus on CodeQL behavior first.
"""

from llm.ollama_client import query_ollama


def dangerous_eval(expr: str):
    """Deliberately unsafe helper used for CodeQL learning.

    Why this exists:
    - `eval` on untrusted input is a classic code execution risk.
    - CodeQL is much more useful when you can point it at a real unsafe sink.

    Why this does NOT fail Gitleaks:
    - There are no secret-like strings here.
    """
    return eval(expr)


def get_plan(cve):
    """Generate a concise mitigation plan for a CVE.

    In CI, the underlying Ollama client falls back to a mock response so the
    pipeline remains stable even when no local LLM is available.
    """
    prompt = (
        f"Provide a concise step-by-step mitigation plan for {cve['cve']} "
        f"with description: {cve['desc']} and CVSS {cve.get('cvss', 'unknown')}."
    )
    return query_ollama(prompt)
