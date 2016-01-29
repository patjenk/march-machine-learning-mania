# A command line tool for reading in and scoring kaggle march machine
# learning mania submissions and scoring.
import argparse


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


def score_submission():
    """
    """



if __name__ == "__main__":
    score_submission()
