from csv import DictReader
from collegeBasketball.game import CollegeBasketballGame


class MarchMachineLearningManiaResults():
    """
    Encapsulates game results used for scoring the kaggle competition
    """

    # This is a dictionary of years with a dictionary of day numbers to
    # a list of game results
    game_scores = None

    def __init__(self):
        self.game_scores = {}

    def load(self, filename):
        """
        Load one of the compact or detailed results file provided by kaggle.
        """
        fh = open(filename, 'r')
        reader = DictReader(fh)
        for row in reader:
            new_game = CollegeBasketballGame()
            new_game.year = int(row['season'])
            new_game.daynum = int(row['daynum'])
            winning_team_id = int(row['wteam'])
            winning_score = int(row['wscore'])
            losing_team_id = int(row['lteam'])
            losing_score = int(row['lscore'])
            if winning_team_id < losing_team_id:
                new_game.team_1_id = winning_team_id
                new_game.team_2_id = losing_team_id
                new_game.team_1_score = winning_score
                new_game.team_2_score = losing_score
            else:
                new_game.team_2_id = winning_team_id
                new_game.team_1_id = losing_team_id
                new_game.team_2_score = winning_score
                new_game.team_1_score = losing_score
            if new_game.year not in self.game_scores:
                self.game_scores[new_game.year] = {}
            if new_game.daynum not in self.game_scores[new_game.year]:
                self.game_scores[new_game.year][new_game.daynum] = []
            self.game_scores[new_game.year][new_game.daynum].append(new_game)
