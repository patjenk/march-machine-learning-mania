patjenk's March Machine Learning Mania
======================================

Contest Details
---------------
https://www.kaggle.com/c/march-machine-learning-mania-2016

Test Suite
----------
To run the test suite, use `nosetests`.

Scoring Submissions
-------------------
`python computekagglescore.py --submission <filename-of-kaggle-submission> --results <filename-with-game-results> --start-day <day-the-tournament-starts>`

Example:

python computekagglescore.py --submission ../data-files/net-prophets.2015-public.submission --results ../data-files/tourney_detailed_results_thru_2015.csv --start-day=136
