from datetime import datetime

from position import Position
from sport import Sport
from team import Team


class AvailablePlayer:
    def __init__(self, player_id, first_name, last_name, jersey_number, position_group, draft_group_start_time,
                 team, match_up, is_disabled_from_drafting, exceptional_messages, salary, draftkings_points_per_contest,
                 opposition_rank):
        if type(player_id) is not int:
            raise TypeError('player id field is not an int')

        if type(first_name) is not unicode:
            raise TypeError('first name field is not a string')

        if type(last_name) is not unicode:
            raise TypeError('last name field is not a string')

        if type(jersey_number) is not int:
            raise TypeError('jersey number field is not an int')

        if not isinstance(position_group, AvailablePlayerPositionGroup):
            raise TypeError('position group is not valid')

        if type(draft_group_start_time) is not datetime:
            raise TypeError('draft group start timestamp field is not a datetime')

        if not isinstance(team, Team):
            raise TypeError('team field is not valid')

        if not isinstance(match_up, MatchUp):
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
        self.position_group = position_group
        self.jersey_number = jersey_number
        self.last_name = last_name
        self.first_name = first_name
        self.draft_group_start_timestamp = draft_group_start_time
        self.team = team
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


class AvailablePlayerPositionGroup:
    def __init__(self, position_group_id, positions):
        if type(position_group_id) is not int:
            raise TypeError('position group id: %s is not an int', position_group_id)

        if type(positions) is not list:
            raise TypeError('positions field: %s is not a list', positions)

        self.position_group_id = position_group_id
        self.positions = positions

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

    @staticmethod
    def value_of(sport, position_group_id, position_group_name):
        if not isinstance(sport, Sport):
            raise TypeError('sport: %s is not a Sport', sport)

        if type(position_group_id) is not int:
            raise TypeError('position group id: %s is not an int', position_group_id)

        if type(position_group_name) is not basestring:
            raise TypeError('position group name: %s is not a string', position_group_name)

        positions = Position.get_positions(sport=sport, abbreviations=position_group_name.split('/'))
        return AvailablePlayerPositionGroup(position_group_id=position_group_id, positions=positions)


class MatchUp:
    def __init__(self, match_up_id, home_team, away_team):
        if not type(match_up_id) is int:
            raise TypeError('match up id: %s is not a number', match_up_id)

        if not isinstance(home_team, Team):
            raise TypeError('home team is not a valid team')

        if not isinstance(away_team, Team):
            raise TypeError('away team is not a valid team')

        self.match_up_id = match_up_id
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