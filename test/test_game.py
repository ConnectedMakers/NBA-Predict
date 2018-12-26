import unittest
from src.game import Game
from src.team import Team


class TestGame(unittest.TestCase):
    def set_up(self):
        pass

    def test_game_class(self):
        v_team = Team("Raptors", "1", 70, 2, [22, 22, 22, 22])
        h_team = Team("Spurs", "2", 72, 0, [25, 25, 25, 25])
        game = Game("1234", v_team, h_team, 15179)
        self.assertEqual(game.game_id, '1234')
        self.assertEqual(game.visitor_team.name, "Raptors")
        self.assertEqual(game.home_team.name, "Spurs")
        self.assertEqual(game.home_team.line_scores, [25, 25, 25, 25])
        self.assertEqual(game.visitor_team.line_scores, [22, 22, 22, 22])
        self.assertEqual(game.home_team.team_id, "2")
        self.assertEqual(game.visitor_team.team_id, "1")
        self.assertEqual(game.visitor_team.wins, 70)
        self.assertEqual(game.home_team.wins, 72)
        self.assertEqual(game.visitor_team.losses, 2)
        self.assertEqual(game.home_team.losses, 0)
        self.assertEqual(game.attendance, 15179)


if __name__ == "__main__":
    unittest.main()
