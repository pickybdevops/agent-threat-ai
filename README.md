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


## DevSecOps learning block 1

This repo has been annotated to teach the first set of LCRA-relevant skills:

1. GitHub Actions pipeline structure
2. CodeQL static analysis (advanced YAML setup)
3. Secret scanning with a custom Gitleaks rule
4. Dependency scanning with `pip-audit`
5. Understanding the difference between:
   - CodeQL alerts uploaded to GitHub
   - Direct workflow failures from tools like Gitleaks

### What to expect when you push

- `CodeQL` should run and upload results to GitHub code scanning.
- `Gitleaks` should pass by default because there is no hardcoded password.
- `pip-audit` will fail only if vulnerable dependencies are present.

### How to force a Gitleaks failure later

Add a line like this to any tracked file:

```python
password placeholder example removed
```

Then push again. The custom Gitleaks rule should fail the workflow.

### How to study CodeQL behavior

The file `vuln-test/vuln-test.py` contains intentionally unsafe Flask routes:
- `eval(request.args.get(...))`
- `os.system(request.args.get(...))`
- `subprocess.run(..., shell=True)`

These are there so you can study how CodeQL handles realistic insecure data flows.
