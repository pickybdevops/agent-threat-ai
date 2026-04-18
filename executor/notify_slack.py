import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()


def notify(message: str) -> bool:
    """Send a Slack notification when a webhook is configured.

    In CI or local demo environments where a webhook is missing, skip safely.
    """
    webhook: Optional[str] = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook:
        print("[Slack] No webhook configured; skipping notification.")
        return False

    try:
        response = requests.post(webhook, json={"text": message}, timeout=10)
        response.raise_for_status()
        print("[Slack] Notification sent.")
        return True
    except requests.RequestException as exc:
        print(f"[Slack] Notification failed: {exc}")
        return False
