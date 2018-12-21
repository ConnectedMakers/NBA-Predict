from src.team import Team


class Game:
    def __init__(self, game_id: str, visitor_team: Team, home_team: Team):
        self.game_id = game_id
        self.visitor_team = visitor_team
        self.home_team = home_team

    def __str__(self):
        return "Game(game_id={}, visitor_team={}, \
        home_team={})".format(self.game_id, self.visitor_team, self.home_team)
