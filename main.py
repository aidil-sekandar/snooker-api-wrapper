import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("X_REQUESTED_BY")

snooker_api = "https://api.snooker.org/"


#### HELPER FUNCTIONS ####


def load_cache(path):
    with open(f"./{path}", "r") as file:
        data = json.load(file)
        return data


def request_json(params):
    response = requests.get(
        snooker_api, headers={"X-Requested-By": api_key}, params=params
    )
    response.raise_for_status()
    return response.json()


def save_cache(path, raw_data):
    with open(f"./{path}", "w") as file:
        json.dump(raw_data, file, indent=2)


#### SNOOKER WRAPPER FUNCTIONS ####


def get_player(player_id):
    path = Path(f"./data/raw/player_{player_id}.json")
    if path.exists():
        return load_cache(path)[0]

    raw_data = request_json({"p": player_id})

    if not raw_data:
        raise ValueError(f"Player with ID {player_id} not found")

    save_cache(path, raw_data)

    return raw_data[0]


ronnie = get_player(5)
judd = get_player(12)

print(ronnie["FirstName"])
