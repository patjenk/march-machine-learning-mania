"""
Test the MarchMachineLearningManiaResults class.
"""
from ..results import MarchMachineLearningManiaResults
from os import path
import unittest


class MarchMachineLearningManiaResultsTest(unittest.TestCase):
    """
    """

    def test_object_creation(self):
        """
        Test that we can create a results object.
        """
        game_results = MarchMachineLearningManiaResults()

    def test_load_submission_compact(self):
        """
        Test that we can load the compact sample game results file from kaggle.
        """
        game_results = MarchMachineLearningManiaResults()
        game_results.load(path.join("..", "data-files", "tourney_compact_results_thru_2015.csv"))
        self.assertEqual(len(game_results.game_scores.keys()), 31)
        self.assertEqual(len(game_results.game_scores[2015].keys()), 12)

    def test_load_submission_detailed(self):
        """
        Test that we can load the detailed sample game results file from kaggle.
        """
        game_results = MarchMachineLearningManiaResults()
        game_results.load(path.join("..", "data-files", "tourney_detailed_results_thru_2015.csv"))
        self.assertEqual(len(game_results.game_scores.keys()), 13)
        self.assertEqual(len(game_results.game_scores[2015].keys()), 12)
