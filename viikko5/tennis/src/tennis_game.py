class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    POINTS_TO_WIN = 4
    WINNING_MARGIN = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tied():
            return self.tied_score()
        elif self.got_winning_point_amount():
            return self.advantage_or_winner_score()

        return self.normal_scoring()

    def is_tied(self):
        return self.player1_score == self.player2_score

    def got_winning_point_amount(self):
        if self.player1_score >= self.POINTS_TO_WIN:
            return True
        if self.player2_score >= self.POINTS_TO_WIN:
            return True
        return False

    def tied_score(self):
        if self.player1_score == self.LOVE:
            return "Love-All"
        elif self.player1_score == self.FIFTEEN:
            return "Fifteen-All"
        elif self.player1_score == self.THIRTY:
            return "Thirty-All"
        else:
            return "Deuce"

    def advantage_or_winner_score(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= self.WINNING_MARGIN:
            return "Win for player1"
        else:
            return "Win for player2"

    def normal_scoring(self):
        player1_points = self.get_point_name(self.player1_score)
        player2_points = self.get_point_name(self.player2_score)

        return player1_points + "-" + player2_points

    def get_point_name(self, points):
        if points == self.LOVE:
            return "Love"
        elif points == self.FIFTEEN:
            return "Fifteen"
        elif points == self.THIRTY:
            return "Thirty"
        else:
            return "Forty"
