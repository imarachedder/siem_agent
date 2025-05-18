# agent/trigger_handler.py
from .configs import load_triggers

def check_triggers(domain):
    """
    Проверяет, есть ли триггер на этот домен.
    """
    triggers = load_triggers()
    for trigger in triggers:
        if trigger in domain:
            return True
    return False