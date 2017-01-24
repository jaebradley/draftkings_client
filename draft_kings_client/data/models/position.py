from enum import Enum

from sport import Sport


class Position(Enum):
    point_guard = {
        'sport': Sport.nba,
        'abbreviation': 'PG',
        'name': 'Point Guard'
    }
    shooting_guard = {
        'sport': Sport.nba,
        'abbreviation': 'SG',
        'name': 'Shooting Guard'
    }
    small_forward = {
        'sport': Sport.nba,
        'abbreviation': 'SF',
        'name': 'Small Forward'
    }
    power_forward = {
        'sport': Sport.nba,
        'abbreviation': 'PF',
        'name': 'Power Forward'
    }
    center = {
        'sport': Sport.nba,
        'abbreviation': 'C',
        'name': 'Center'
    }

    @staticmethod
    def get_positions_from_position_group_name(sport, position_group_name):
        return Position.get_positions(sport=sport, abbreviations=position_group_name.split('/'))

    @staticmethod
    def get_positions(sport, abbreviations):
        return [Position.value_of(sport=sport, abbreviation=abbreviation) for abbreviation in abbreviations]

    @staticmethod
    def value_of(sport, abbreviation):
        assert isinstance(sport, Sport)
        assert isinstance(abbreviation, basestring)

        for position in Position:
            if position.value['sport'] == sport and position.value['abbreviation'] == abbreviation:
                return position

        raise ValueError('Unable to identify position for sport: %s and abbreviation: %s', sport, abbreviation)
