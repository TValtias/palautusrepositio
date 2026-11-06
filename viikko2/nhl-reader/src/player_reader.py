"""This module includes PlayerReader class"""

import requests
from player import Player

class PlayerReader:
    """returns a list of players"""

    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players