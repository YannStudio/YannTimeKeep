import json
from datetime import datetime
from pathlib import Path

#Functions to load an save data in json file

DATA_FILE = Path("data/sessions.json")

def load_data():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
