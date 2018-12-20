class Team:
    def __init__(self, name, team_id, wins, losses, linescore):
        self.name = name
        self.team_id = team_id
        self.wins = wins
        self.losses = losses
        self.linescore = linescore

    def __str__(self):
        s = "Team(name={}, team_id={}, wins={}, losses={}, linescore={})"
        return s.format(self.game_id, self.team_id,
                        self.wins, self.losses, self.linescore)
