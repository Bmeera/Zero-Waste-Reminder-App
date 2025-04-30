import json
from datetime import datetime

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def get_days_until(expiry_date):
    today = datetime.today().date()
    return (expiry_date - today).days
