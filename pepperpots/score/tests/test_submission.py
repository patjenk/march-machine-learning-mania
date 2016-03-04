"""
Test the MarchMachineLearningManiaSubmission class.
"""
from ..submission import MarchMachineLearningManiaSubmission
from os import path
import unittest


class MarchMachineLearningManiaSubmissionTest(unittest.TestCase):
    """
    """
    def test_object_creation(self):
        """
        Test that an object can be created.
        """
        kaggle_submission = MarchMachineLearningManiaSubmission()

    def test_score_game(self):
        """
        test that given the correct input to .score_game
        we will get the expected value.
        """
        kaggle_submission = MarchMachineLearningManiaSubmission()
        kaggle_submission.year = 2030
        kaggle_submission.predictions[1] = {}
        kaggle_submission.predictions[1][2] = 0.50
        self.assertEqual(kaggle_submission.score_game(2030, 1, 2, 1), -0.69314718055994529)
        self.assertEqual(kaggle_submission.score_game(2030, 1, 2, 2), -0.69314718055994529)

    def test_load_submission(self):
        """
        test that given a submission file on disk we can load it in
        """
        kaggle_submission = MarchMachineLearningManiaSubmission()
        kaggle_submission.load(path.join(".", "pepperpots", "score", "tests", "data", "test_submission.001.csv"))
        self.assertEqual(2015, kaggle_submission.year)
        self.assertEqual(66, len(kaggle_submission.predictions))
        self.assertEqual(kaggle_submission.predictions[1][2], 0.5)

    def test_load_submission(self):
        """
        test that when we have a submission file loaded
        and that submission file gives every game a 0.5 probablitity
        that we can correctly calculate the score
        """
        number_of_teams = 68
        kaggle_submission = MarchMachineLearningManiaSubmission()
        kaggle_submission.year = 2015
        total_teams = 68
        for team_id_1 in range(1, total_teams+1):
            kaggle_submission.predictions[team_id_1] = {}
            for team_id_2 in range(team_id_1 + 1, total_teams+1):
                kaggle_submission.predictions[team_id_1][team_id_2] = float('0.5')

        # create game results, just need 63 to be right.
        game_results = []
        team_id_1 = 1
        team_id_2 = team_id_1 + 1
        while len(game_results) < 64:
            game_results.append(("{}_{}_{}".format(kaggle_submission.year, team_id_1, team_id_2), team_id_1))
            team_id_2 += 1
            if team_id_2 > number_of_teams:
                team_id_1 = (len(game_results) / number_of_teams) + 1
                team_id_2 = team_id_1 + 1

        self.assertEqual(0.693147, round(kaggle_submission.score_result(game_results), 6))
