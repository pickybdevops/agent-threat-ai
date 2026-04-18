# agent-threat-ai

Proof-of-concept threat response orchestration demo.

## What it does
- Parses a mock CVE feed
- Generates a remediation plan with Ollama or a CI-safe fallback
- Maps threats to affected hosts
- Generates a YARA rule
- Stores threat context in vector memory with ChromaDB when available
- Creates a mock SOAR ticket
- Simulates EDR host isolation
- Sends Slack notifications when a webhook is configured

## Local run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

## CI behavior
When `CI=true`, the LLM layer returns a deterministic mock response so GitHub runners do not require a local Ollama service.
