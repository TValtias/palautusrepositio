class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = [
            player for player in self._players
            if player.nationality == nationality
        ]

        return sorted(
            players_of_nationality,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )