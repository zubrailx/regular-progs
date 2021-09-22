import requests
import time


def collect_data(name, univ, amount):

    univ = "play" if univ == "" else univ

    params = {
        "playerId": "tr:" + name,
        "universe": univ,
        "n": amount
    }

    req = requests.get("https://data.typeracer.com/games", params=params)

    if req.status_code == 400 or req.status_code == 404:
        print("WI oshiblis'")
    else:
        return req.json()


def seconds_to_normal(sec):
    sec = int(sec)
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sec))
