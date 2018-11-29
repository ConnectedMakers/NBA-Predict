import unittest
from src import stats


class TestStats(unittest.TestCase):
    def test_app(self):
        self.assertEqual(stats.get_player_name(), 'Hello')


if __name__ == '__main__':
    unittest.main()
