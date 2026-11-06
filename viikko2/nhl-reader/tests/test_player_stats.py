import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "goals": 4,
                "assists": 12,
                "team": "EDM",
                "games": 80,
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "goals": 45,
                "assists": 54,
                "team": "PIT",
                "games": 80,
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "goals": 37,
                "assists": 53,
                "team": "EDM",
                "games": 80,
            }),
            Player({
                "name": "Yzerman",
                "nationality": "CAN",
                "goals": 42,
                "assists": 56,
                "team": "DET",
                "games": 80,
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "goals": 35,
                "assists": 89,
                "team": "EDM",
                "games": 80,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_nationalities_are_sorted_and_unique(self):
        self.assertEqual(self.stats.nationalities(), ["CAN", "FIN"])

    def test_teams_are_sorted_and_unique(self):
        self.assertEqual(self.stats.teams(), ["DET", "EDM", "PIT"])

    def test_top_scorers_by_nationality_are_sorted_by_points(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"],
        )

    def test_top_scorers_by_team_are_sorted_by_points(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"],
        )

    def test_top_goal_scorers_returns_requested_number(self):
        players = self.stats.top_goal_scorers(3)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"],
        )


if __name__ == "__main__":
    unittest.main()
