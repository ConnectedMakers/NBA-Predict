class Team:
    def __init__(self, name: str, team_id: str, wins: int,
                 losses: int, line_score: list):
        self.name = name
        self.team_id = team_id
        self.wins = wins
        self.losses = losses
        self.line_score = line_score

    def __str__(self):
        s = "Team(name={}, team_id={}, wins={}, losses={}, line_score={})"
        return s.format(self.name, self.team_id,
                        self.wins, self.losses, self.line_score)
