import requests
import json
import os

CONFIG_FILE = "config.json"


def save_config(ip, username):
    """Saves the IP and username to a JSON file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump({"ip": ip, "username": username}, f)


def load_config():
    """Loads config from file. Returns None if it doesn't exist."""
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def create_user(ip):
    """
    Press the bridge button BEFORE calling this function.
    It sends a POST request to create an API user.
    """
    url = f"http://{ip}/api"
    payload = {"devicetype": "hue_cli#python"}

    response = requests.post(url, json=payload)
    data = response.json()

    if "error" in data[0]:
        raise Exception("Failed to create user. Make sure you pressed the button on the bridge.")

    username = data[0]["success"]["username"]

    return ip, username
