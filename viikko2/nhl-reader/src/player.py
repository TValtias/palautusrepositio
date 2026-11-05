class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.games = dict['games']

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return (f"{self.name:20} nationality: {self.nationality:5} team: {self.team:5}"
                f"games: {self.games:3} goals: {self.goals:2} assists: {self.assists:2}")
