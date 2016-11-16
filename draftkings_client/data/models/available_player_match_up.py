class AvailablePlayerMatchUp:
    def __init__(self, home_team, away_team):
        if not isinstance(home_team, AvailablePlayerTeam):
            raise TypeError('home team is not a valid team')

        if not isinstance(away_team, AvailablePlayerTeam):
            raise TypeError('away team is not a valid team')

        self.home_team = home_team
        self.away_team = away_team


class AvailablePlayerTeam:
    def __init__(self, team_id, team_abbreviation):
        if type(team_id) is not int:
            raise TypeError('team id field is not an int')

        if type(team_abbreviation) is not str:
            raise TypeError('team abbreviation field is not a string')

        self.team_id = team_id
        self.team_abbreviation = team_abbreviation