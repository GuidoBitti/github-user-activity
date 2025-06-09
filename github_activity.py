import urllib.request
import json

def get_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:

            data = response.read().decode()

            json_data = json.loads(data)
    except:
        return "user not found"
    return json_data
    