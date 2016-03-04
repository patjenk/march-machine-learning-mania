# A command line tool for reading in and scoring kaggle march machine
# learning mania submissions and scoring.
import argparse
from kagglescoring.submission import MarchMachineLearningManiaSubmission
from kagglescoring.results import MarchMachineLearningManiaResults


parser = argparse.ArgumentParser(description="Compute the logloss score for a Kaggle March Machine Learning Mania Submission")
parser.add_argument("-v", "--verbose",
                    action="store_true",
                    default=False,
                    dest="verbose",
                    help="Print out more detailed scoring information.")
parser.add_argument("-s", "--submission",
                    action="store",
                    dest="submission_filename",
                    help="Path to properly formatted kaggle submission.")
parser.add_argument("-r", "--results",
                    action="store",
                    dest="results_filename",
                    help="The name of the results file to use. If not provided the canonical Kaggle result will be used.")
parser.add_argument("-d", "--start-day",
                    action="store",
                    type=int,
                    dest="tournament_start_day",
                    help="The day number of the start of the tournament.")
args = parser.parse_args()


def score_submission():
    """
    """
    kaggle_submission = MarchMachineLearningManiaSubmission()
    kaggle_submission.load(args.submission_filename)

    game_results = MarchMachineLearningManiaResults()
    game_results.load(args.results_filename)

    game_days = []
    for daynum in game_results.game_scores[kaggle_submission.year]:
        if daynum >= args.tournament_start_day:
            game_days.append(daynum)

    games_to_score = []
    for daynum in game_days:
        for game in game_results.game_scores[kaggle_submission.year][daynum]:
            games_to_score.append((game.kaggle_underscore_representation(), game.winning_team_id()))

    print round(kaggle_submission.score_result(games_to_score), 6)

if __name__ == "__main__":
    score_submission()
