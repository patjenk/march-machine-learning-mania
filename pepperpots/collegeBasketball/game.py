


class CollegeBasketballGame():
    """
    Represents a College Baskebtall Team during a particular sports year.
    """
    team_1_id = None
    team_2_id = None
    team_1_score = None
    team_2_score = None
    home_team_id = None
    datetime = None
    location = None
    number_of_overtimes = None
    year = None
    daynum = None

    def winning_team_id(self):
        if team_1_score < team_2_score:
            return team_2_id
        else:
            return team_1_id
