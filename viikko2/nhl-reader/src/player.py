"""Represent an NHL player and their season statistics."""

class Player:
    """Represents an NHL player with their statistics for a given season."""

    def __init__(self, stats_dict):
        """Initializes a Player instance with data from a dictionary."""
        self.name = stats_dict['name']
        self.nationality = stats_dict['nationality']
        self.goals = stats_dict['goals']
        self.assists = stats_dict['assists']
        self.team = stats_dict['team']
        self.games = stats_dict['games']

    @property
    def points(self):
        """Returns the total points for the player."""

        return self.goals + self.assists

    def __str__(self):
        """Returns a formatted string representation of the player."""

        return (f"{self.name:20} nationality: {self.nationality:5} team: {self.team:5}"
                f"games: {self.games:3} goals: {self.goals:2} assists: {self.assists:2}")
