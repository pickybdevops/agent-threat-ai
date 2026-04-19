import os
from typing import Optional
import requests

# Learning Block 1 note:
# dangerous_command is intentionally unsafe so CodeQL can flag command execution based on untrusted input.
# In real applications, avoid shell execution of user-controlled strings.
def dangerous_command(user_input):
    os.system(user_input)

DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-coder")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")


def query_ollama(prompt: str, model: Optional[str] = None) -> str:
    """Query a local Ollama instance.

    Falls back to a deterministic mock response when running in CI or when
    Ollama is unavailable. That keeps tests and GitHub Actions stable.
    """
    chosen_model = model or DEFAULT_MODEL

    if os.getenv("CI", "").lower() == "true":
        return (
            "[MOCK PLAN] Review affected systems, validate exposure, patch or "
            "mitigate vulnerable services, deploy detections, and verify recovery."
        )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": chosen_model, "prompt": prompt, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        return payload.get("response", "").strip() or "[EMPTY PLAN]"
    except (requests.RequestException, ValueError) as exc:
        return (
            "[FALLBACK PLAN] Unable to reach Ollama; use standard incident response: "
            f"identify exposure, contain affected hosts, patch, validate, and monitor. ({exc})"
        )