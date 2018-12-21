import requests
import json
from datetime import datetime
from team import Team


def get_current_date():
    return datetime.today().strftime('%Y%m%d')


def get_vistor_team_info(game_payload):
    team_payload = game_payload['vTeam']
    tri_code = team_payload['triCode']
    team_id = team_payload['teamId']
    wins = team_payload['win']
    losses = team_payload['loss']
    linescore = team_payload['linescore']
    return Team(tri_code, team_id, wins, losses, linescore)


date = get_current_date()

url = "http://data.nba.net/10s/prod/v1/{}/scoreboard.json".format(date)
scoreboard_payload = requests.get(url)
scoreboard_json = json.loads(scoreboard_payload.text)

games = scoreboard_json['games']

print(get_vistor_team_info(games[0]))
