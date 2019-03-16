from core import wb
import json
import requests
import sys

def update_matches(event_search: str):
    with open('events.json', 'r') as events_file:
        events_json = json.load(events_file)

    keys = events_json.keys()
    event = [s for s in keys if event_search.lower() in s.lower()][0]

    event_key = events_json[event]

    TBA_URL = "https://www.thebluealliance.com/api/v3/"
    with open('api_key') as api_key_file:
        API_KEY = api_key_file.read()
    payload = {'X-TBA-Auth-Key': API_KEY}

    r = requests.get(TBA_URL + 'event/{}/matches/simple'.format(event_key), payload)
    match_data = json.loads(r.text)
    with open('test.json', 'w+') as test_output:
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
    #wb.save('scouting.xlsx')


if __name__ == "__main__":
    argument = sys.argv[1]
    update_matches(argument)