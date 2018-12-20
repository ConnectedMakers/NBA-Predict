class Game:
    def __init__(self, game_id, vistor_team, home_team):
        self.game_id = game_id
        self.vistor_team = vistor_team
        self.home_team = home_team

    def __str__(self):
        return "Game(game_id={}, vistor_team={}, \
        home_team={})".format(self.game_id, self.vistor_team, self.home_team)
