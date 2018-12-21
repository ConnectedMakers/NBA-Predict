class Team:
    def __init__(self, name: str, team_id: str, wins: int,
                 losses: int, line_scores: list):
        self.name = name
        self.team_id = team_id
        self.wins = wins
        self.losses = losses
        self.line_scores = line_scores

    def __str__(self):
        s = "Team(name={}, team_id={}, wins={}, losses={}, line_scores={})"
        return s.format(self.name, self.team_id,
                        self.wins, self.losses, self.line_scores)
