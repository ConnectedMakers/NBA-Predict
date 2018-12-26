from datetime import datetime
import requests
import json
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from src.team import Team
from src.game import Game


def get_current_date():
    return datetime.today().strftime('%Y%m%d')


def get_vistor_team_info(game_payload):
    return get_team_info(game_payload, "vTeam")


def get_home_team_info(game_payload):
    return get_team_info(game_payload, "hTeam")


def get_team_info(game_payload, teamSide):
    team_payload = game_payload[teamSide]
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

game = games[0]
game_id = game["gameId"]
v_team = get_vistor_team_info(game)
h_team = get_home_team_info(game)
attendance = game["attendance"]

today_game = Game(game_id, v_team, h_team, attendance)

print(today_game)
