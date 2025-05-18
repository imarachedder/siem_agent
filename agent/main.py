# agent/main.py
from agent.network_monitor import get_active_domains
from agent.trigger_handler import check_triggers
from agent.logger import log_event
import time

def run_agent(interval=5):
    print("[*] Запуск SIEM-агента...")
    while True:
        domains = get_active_domains()
        for domain in domains:
            triggered = check_triggers(domain)
            event = log_event(domain, triggered)
            if triggered:
                print(f"[!] Триггер сработал: {event}")
        time.sleep(interval)

if __name__ == "__main__":
    run_agent()