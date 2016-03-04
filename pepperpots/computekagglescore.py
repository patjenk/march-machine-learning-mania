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
                    dest="tournament_start_day",
                    help="The day number of the start of the tournament.")
parser.add_argument("-y", "--year",
                    action="store",
                    dest="year_to_score",
                    help="The year (or season in kaggle parlance) to grade the submission on. This is useful in case the results file has multiple years included.")
args = parser.parse_args()


def score_submission():
    """
    """
    print args.results_filename
    kaggle_submission = MarchMachineLearningManiaSubmission()
    kaggle_submission.load(args.submission_filename)

    game_results = MarchMachineLearningManiaResults()
    game_results.load(args.results_filename)

    game_days = []
    for daynum in game_results.game_scores[kaggle_submission.year]:
        if daynum >= args.tournament_start_day:
            game_days.append(daynum)

    game_results = []
    for daynum in game_days:
        for game in game_results.game_scores[kaggle_submission.year][daynum]:
            game_results.append((game.kaggle_underscore_representation(), game.winning_team_id()))

    print round(kaggle_submission.score_result(game_results), 6)

if __name__ == "__main__":
    score_submission()