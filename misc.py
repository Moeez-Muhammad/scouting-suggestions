import json
import requests
import sys
import os.path
from core import path
from core import wb

def get_event_key(event_search: str) -> str:
    with open(os.path.join(path, 'events.json'), 'r') as events_file:
        events_json = json.load(events_file)

    keys = events_json.keys()
    event = [s for s in keys if event_search.lower() in s.lower()][0]

    event_key = events_json[event]

    return event_key

def update_matches(event_search: str):
    event_key = get_event_key(event_search)

    TBA_URL = "https://www.thebluealliance.com/api/v3/"
    with open(os.path.join(path, 'api_key')) as api_key_file:
        API_KEY = api_key_file.read()
    payload = {'X-TBA-Auth-Key': API_KEY}

    r = requests.get(TBA_URL + 'event/{}/matches/simple'.format(event_key), payload)
    match_data = json.loads(r.text)
    with open(os.path.join(path, 'matches.json'), 'w+') as test_output:
        json.dump(match_data, test_output, indent=4)
    match_data = sorted(match_data, key=lambda match: match["match_number"])
    
    ws = wb["EVENT DATA"]
    for match in match_data:
        if match["comp_level"] == 'qm':
            row = match["match_number"] + 4
            row_data = ws[row]

            red_teams = [int(team[3:]) for team in match["alliances"]["red"]["team_keys"]]
            blue_teams = [int(team[3:]) for team in match["alliances"]["blue"]["team_keys"]]

            row_data[1].value = 'Quals ' + str(match["match_number"])
            row_data[2].value = red_teams[0]
            row_data[3].value = red_teams[1]
            row_data[4].value = red_teams[2]
            print('Quals ' + str(match["match_number"]), end=',')
            print(red_teams[0], end=',')
            print(red_teams[1], end=',')
            print(red_teams[2], end=',')

            row_data[5].value = blue_teams[0]
            row_data[6].value = blue_teams[1]
            row_data[7].value = blue_teams[2]
            print(blue_teams[0], end=',')
            print(blue_teams[1], end=',')
            print(blue_teams[2], end=',')

#argument = sys.argv[1]
#update_matches(argument)

def update_teams(event_search: str):
    event_key = get_event_key(event_search)

    TBA_URL = "https://www.thebluealliance.com/api/v3/"
    with open(os.path.join(path, 'api_key')) as api_key_file:
        API_KEY = api_key_file.read()
    payload = {'X-TBA-Auth-Key': API_KEY}

    r = requests.get(TBA_URL + 'event/{}/teams/simple'.format(event_key), payload)
    team_data = json.loads(r.text)
    with open(os.path.join(path, 'teams.json'), 'w+') as test_output:
        json.dump(team_data, test_output, indent=4)
    
    simple_teams = {}
    for team in team_data:
        simple_teams[team["team_number"]] = team["nickname"]
    
    ws = wb["Scouting Output"]
    old_team_numbers = ws["A": "A"]
    old_team_names = ws["B": "B"]
    
    old_team_numbers = [number.value for number in old_team_numbers][2:]
    old_team_names = [name.value for name in old_team_names][2:]

    old_teams = dict(zip(old_team_numbers, old_team_names))

    all_teams = {**simple_teams, **old_teams}
    filtered_all_teams = {k: v for k, v in all_teams.items() if v is not None}
    for team_number in sorted(filtered_all_teams):
        print(str(team_number), end=",")
        print(filtered_all_teams[team_number], end=",")
    
