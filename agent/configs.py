import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent / "config" / "domains.yaml"

def load_triggers():
    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f)
    return data.get("triggers", [])