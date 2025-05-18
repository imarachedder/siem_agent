# agent/logger.py
import json
import datetime
import os
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "data" / "logs"
LOG_FILE = LOG_DIR / "traffic_logs.json"

os.makedirs(LOG_DIR, exist_ok=True)

def log_event(domain, triggered=False):
    event = {
        "timestamp": datetime.datetime.now().isoformat(),
        "domain": domain,
        "triggered": triggered,
        "event_type": "visit_vk" if "vk.com" in domain else "blocked_site" if triggered else "normal_traffic",
        "user": os.getenv("USERNAME"),
        "event": {
            "category": "security" if triggered else "network",
            "type": "alert" if triggered else "connection",
            "severity": 7 if triggered else 3,
            "risk_score": 80 if triggered else 20,
            "module": "siem-agent"
        }
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    return event