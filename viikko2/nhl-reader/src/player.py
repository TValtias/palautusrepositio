class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']

    def __str__(self):
        return (f"{self.name:20} nationality {self.nationality: 5} team {self.team:5} id {self.id:8} games {self.games:3}"
                f"points {self.points():3} goals {self.goals:2} assists {self.assists:2}")
