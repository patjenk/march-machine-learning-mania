# A method for scoring entries in the Kaggle March Machine Learning
# Mania competition
#
# https://www.kaggle.com/c/march-machine-learning-mania-2015/details/evaluation
from csv import DictReader
from scipy import log, maximum, minimum, subtract


class MarchMachineLearningManiaSubmission():
    """
    Encapsulates a submission to the Kaggle contest.

    self.predictions is a dictionary of dictionary with the first key
    being the lower team id and the second key being the higher team's
    id. The ending value is the submission's prediction.
    """
    predictions = None
    year = None

    def __init__(self):
        self.predictions = {}

    @staticmethod
    def parse_game_id(game_id):
        """
        take in a game id in the format {year}_{team_id}_{team_id} as
        specificed in the kaggle submission guidelines. Returns a 
        tuple of game year, team id 1, team id 2
        """
        game_year, team_1_id, team_2_id = game_id.split( "_")
        team_1_id = int(team_1_id)
        team_2_id = int(team_2_id)
        if team_1_id >= team_2_id:
            raise Exception("Invalid Id in submission file, team 1 id is greater than or equal to team 2:: {}, {}".format(team_1_id, team_2_id))
        return game_year, team_1_id, team_2_id

    def load(self, filename):
        """
        open the filename and read in the results.
        """
        fh = open(filename, 'r')
        reader = DictReader(fh)
        for row in reader:
            game_year, team_1_id, team_2_id = self.parse_game_id(row['id'])
            game_year = int(game_year)
            if self.year is None:
                self.year = game_year
            elif self.year != game_year:
                raise Exception("Multiple years found in submission Ids: {}, {}".format(self.year, game_year))


            if team_1_id not in self.predictions:
                self.predictions[team_1_id] = {}
            self.predictions[team_1_id][team_2_id] = float(row['pred'])

    def verify(self):
        """
        Return True if the submission contains the correct data.
        """
        pass

    def score_game(self, year, team_1_id, team_2_id, winning_team_id):
        """
        Compute the log loss portion of this game and return.
        https://www.kaggle.com/wiki/LogarithmicLoss
        """
        if team_1_id >= team_2_id:
            raise Exception("Invalid team Ids while calculating score, team 1's id is greater than or equal to team 2. {}, {}".format(team_1_id, team_2_id))
        prediction = self.predictions[team_1_id][team_2_id]
        epsilon = 1e-15
        prediction = maximum(epsilon, prediction)
        prediction = minimum(1-epsilon, prediction)

        y_i = None
        if team_1_id == winning_team_id:
            y_i = 1
        else:
            y_i = 0

        result = y_i * log(prediction) + subtract(1, y_i) * log(subtract(1, prediction))
        return result

    def score_result(self, game_results):
        """
        game_results is a list of tuples where the first item in the 
        tuple is the game id and the second is the winning team id.
        """
        total = float(0)
        for game_id, winning_team_id in game_results:
            game_year, team_1_id, team_2_id = self.parse_game_id(game_id)
            game_score = self.score_game(game_year, team_1_id, team_2_id, winning_team_id)
            total += game_score 
        return (-1/float(len(game_results))) * total
