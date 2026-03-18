import requests
import inquirer

def get_base_url(ip, username):
    return f"http://{ip}/api/{username}"

def get_lights(ip, username):
    """Fetches all lights and returns them as a dictionary."""
    url = get_base_url(ip, username) + "/lights"
    response = requests.get(url)
    return response.json()

def list_lights(ip, username):
    """Prints lights."""
    lights = get_lights(ip, username)

    for id, light in lights.items():
        status = "on" if light["state"]["on"] else "off"
        print(f"[{id}] {light['name']} — {status}")

def pick_lights(ip, username, filter="on"):
    """Prompt the user to select lights interactively."""
    lights = get_lights(ip, username)
    filtered_lights = {id: light for id, light in lights.items() if (filter == "on" and light["state"]["on"]) or (filter == "off" and not light["state"]["on"])}

    if not filtered_lights:
        print("No lights found.")
        return []

    if len(filtered_lights) == 1:
        return [next(iter(filtered_lights))]  # Return the single light's ID

    choices = [(f"[{id}] {light['name']}", id) for id, light in filtered_lights.items()]

    question = [
        inquirer.Checkbox(
            "selected",
            message="Which lights? (space to select, enter to confirm)",
            choices=choices,
        )
    ]

    answers = inquirer.prompt(question)
    return answers["selected"]

def turn_on_off(ip, username, light_id, turn_on=True):
    """
    Sends a PUT request to change a light's state.
    The Hue API expects: PUT /api/{user}/lights/{id}/state
    with a JSON body: {"on": true} or {"on": false}
    """
    url = get_base_url(ip, username) + f"/lights/{light_id}/state"
    payload = {"on": turn_on}
    response = requests.put(url, json=payload)

    result = response.json()[0]
    if "error" in result:
        raise Exception(f"Failed to change light {light_id}: {result['error']['description']}")

    print(f"Light {light_id} turned {'on' if turn_on else 'off'} successfully.")

def set_brightness(ip, username, light_id, value):
    """
    value must be between 0 and 254 (the range accepted by the Hue API).
    """
    # TODO: same idea, but with the "bri" key in the body
    pass