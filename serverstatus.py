import time
import requests
import datetime
import json

with open('auth.json') as json_obj:
    header = json.load(json_obj)
    json_obj.close()


def get_server_status():
    now = datetime.datetime.now()
    now = now.strftime("%I:%M %p")

    endpoint = "https://firstlight.newworldstatus.com/ext/v1/worlds/neno-kuni"
    headers = header

    r = requests.get(endpoint, headers=headers)
    response = r.json()

    r.raise_for_status()
    if r.status_code != 200:
        return r.json()

    data = response['message']

    status = data['status_enum']
    if status != 'ACTIVE':
        return False
    else:
        players = data['players_current']
        total = data['players_maximum']
        queue = data['queue_current']
        wait = data['queue_wait_time_minutes']
        server_stats = f"Server Status for **Neno Kuni** \n{now} PST\nPlayers: {players}/{total}\nEstimated wait: {wait}m \nStatus: {status}\n"

    return server_stats
# Loop indefinitely until server goes down


def const_server_up():
    while stats != False:
        print(stats)
        time.sleep(60)
        stats = get_server_status()

# Get patch notes when server comes online
