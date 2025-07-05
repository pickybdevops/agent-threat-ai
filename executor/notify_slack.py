import requests, os
from dotenv import load_dotenv
load_dotenv()

def notify(message):
    requests.post(os.getenv("SLACK_WEBHOOK_URL"), json={"text": message})
