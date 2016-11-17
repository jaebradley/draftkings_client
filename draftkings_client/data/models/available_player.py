class AvailablePlayer:
    def __init__(self, player_id, team_series_id, first_name, last_name, jersey_number, position,
                 draft_group_start_timestamp, team_id, match_up,
                 is_disabled_from_drafting, exceptional_messages, salary,
                 draftkings_points_per_contest, opposition_rank):
        if type(player_id) is not int:
            raise TypeError('player id field is not an int')

        if type(team_series_id) is not int:
            raise TypeError('team series id field is not an int')

        if type(first_name) is not unicode:
            raise TypeError('first name field is not a string')

        if type(last_name) is not unicode:
            raise TypeError('last name field is not a string')

        if type(jersey_number) is not int:
            raise TypeError('jersey number field is not an int')

        if not isinstance(position, AvailablePlayerPosition):
            raise TypeError('position is not valid')

        if type(draft_group_start_timestamp) is not long:
            raise TypeError('draft group start timestamp field is not a long')

        if type(team_id) is not int:
            raise TypeError('team id field is not an int')

        if not isinstance(match_up, AvailablePlayerMatchUp):
            raise TypeError('match up field is not valid')

        if type(is_disabled_from_drafting) is not bool:
            raise TypeError('is disabled from drating field is not a boolean')

        if type(exceptional_messages) is not list:
            raise TypeError('exceptional messages field is not a list')

        if type(salary) is not float:
            raise TypeError('salary field is not a float')

        if type(draftkings_points_per_contest) is not float:
            raise TypeError('draftkings points per contest field is not a field')

        if type(opposition_rank) is not int:
            raise TypeError('opposition rank field is not an int')

        self.player_id = player_id
        self.team_series_id = team_series_id
        self.position = position
        self.jersey_number = jersey_number
        self.last_name = last_name
        self.first_name = first_name
        self.draft_group_start_timestamp = draft_group_start_timestamp
        self.team_id = team_id
        self.match_up = match_up
        self.is_disabled_from_drafting = is_disabled_from_drafting
        self.exceptional_messages = exceptional_messages
        self.salary = salary
        self.draftkings_points_per_game = draftkings_points_per_contest
        self.opposition_rank = opposition_rank

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class AvailablePlayerPosition:
    def __init__(self, position_id, position_name):
        if type(position_id) is not int:
            raise TypeError('position id field is not an int')

        if type(position_name) is not unicode:
            raise TypeError('position name field is not a string')

        self.position_id = position_id
        self.position_name = position_name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class AvailablePlayerMatchUp:
    def __init__(self, home_team, away_team):
        if not isinstance(home_team, AvailablePlayerTeam):
            raise TypeError('home team is not a valid team')

        if not isinstance(away_team, AvailablePlayerTeam):
            raise TypeError('away team is not a valid team')

        self.home_team = home_team
        self.away_team = away_team

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class AvailablePlayerTeam:
    def __init__(self, team_id, team_abbreviation):
        if type(team_id) is not int:
            raise TypeError('team id field is not an int')

        if type(team_abbreviation) is not unicode:
            raise TypeError('team abbreviation field is not a string')

        self.team_id = team_id
        self.team_abbreviation = team_abbreviation

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))