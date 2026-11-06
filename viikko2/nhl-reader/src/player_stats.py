"""This module includes PlayerStats class"""

class PlayerStats:
    """Provide statistics about players, including nationality and scoring rankings."""

    def __init__(self, reader):
        """Initializes PlayerStats with a PlayerReader instance and fetches player data."""
        self._players = reader.get_players()

    def nationalities(self):
        """Returns a sorted list of unique nationalities from the player data."""
        return sorted({player.nationality for player in self._players})

    def teams(self):
        """Returns a sorted list of unique teams from the player data."""
        return sorted({player.team for player in self._players})

    def top_scorers_by_nationality(self, nationality):
        """Returns a list of top scorers, sorted by nationality and total points."""
        players_of_nationality = [
            player for player in self._players
            if player.nationality == nationality
        ]

        return sorted(
            players_of_nationality,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

    def top_scorers_by_team(self, team):
        """Returns a team's players sorted by total points."""
        players_of_team = [
            player for player in self._players
            if player.team == team
        ]

        return sorted(players_of_team, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa pelaajat maalien mukaan laskevassa järjestyksessä."""
        return sorted(self._players, key=lambda player: player.goals, reverse=True)[:how_many]
