"""This module includes PlayerReader class"""

import requests
from player import Player

class PlayerReader:
    """Fetch player data from a URL and create Player objects."""

    def __init__(self, url):
        """defines url from input"""

        self._url = url

    def get_players(self):
        """returns a list of players"""
        response = requests.get(self._url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players