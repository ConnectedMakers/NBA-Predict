import requests
url = "http://data.nba.net/10s/prod/v1/20181219/scoreboard.json"
scoreboard_payload = requests.get(url)
print(scoreboard_payload.json())
