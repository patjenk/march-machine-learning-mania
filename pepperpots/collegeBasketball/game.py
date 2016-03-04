


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
        """
        return the id of the winning team
        """
        if team_1_score < team_2_score:
            return team_2_id
        else:
            return team_1_id

    def kaggle_underscore_reprsentation(self):
        """
        return a string with "<submission_year>_<lower team id>_<higher_team_id>"
        """
        lower_team_id = self.team_1_id
        higher_team_id = self.team_2_id
        if self.team_2_id < lower_team_id:
            lower_team_id = self.team_2_id
            higher_team_id = self.team_1_id
        return "{}_{}_{}".format(self.year, lower_team_id, higher_team_id)
