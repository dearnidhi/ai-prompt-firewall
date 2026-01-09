# app/agents/logger_agent.py

import json
import time
from app.config import LOG_FILE


def log_attack(prompt, score, reason):
    log_entry = {
        "time": time.time(),
        "prompt": prompt,
        "risk_score": score,
        "reason": reason
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
