from enum import Enum


class Sport(Enum):
    nfl = "nfl"
    nhl = "nhl"
    nba = "nba"
    nascar = "nas"
    soccer = "soc"
    golf = "golf"
    cfl = "cfl"

    def get_id(self):
        return draft_kings_sport_ids.get(self)

    @staticmethod
    def from_id(sport_id):
        for key, value in draft_kings_sport_ids.items():
            if sport_id == value:
                return key

        raise ReferenceError('unknown sport id')


draft_kings_sport_ids = {
    Sport.nfl: 1,
    Sport.nhl: 3,
    Sport.nba: 4,
    Sport.nascar: 10,
    Sport.soccer: 12,
    Sport.golf: 13,
    Sport.cfl: 14
}


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
        assert isinstance(abbreviation, str)

        for position in Position:
            if position.value['sport'] == sport and position.value['abbreviation'] == abbreviation:
                return position

        raise ValueError('Unable to identify position for sport: %s and abbreviation: %s', sport, abbreviation)


class Team(Enum):
    atlanta_hawks = {
        'sport': Sport.nba,
        'id': 1
    }
    boston_celtics = {
        'sport': Sport.nba,
        'id': 2
    }
    brooklyn_nets = {
        'sport': Sport.nba,
        'id': 17
    }
    charlotte_hornets = {
        'sport': Sport.nba,
        'id': 5312
    }
    chicago_bulls = {
        'sport': Sport.nba,
        'id': 4
    }
    cleveland_cavaliers = {
        'sport': Sport.nba,
        'id': 5
    }
    dallas_mavericks = {
        'sport': Sport.nba,
        'id': 6
    }
    denver_nuggets = {
        'sport': Sport.nba,
        'id': 7
    }
    detroit_pistons = {
        'sport': Sport.nba,
        'id': 8
    }
    golden_state_warriors = {
        'sport': Sport.nba,
        'id': 9
    }
    houston_rockets = {
        'sport': Sport.nba,
        'id': 10
    }
    indiana_pacers = {
        'sport': Sport.nba,
        'id': 11
    }
    los_angeles_clippers = {
        'sport': Sport.nba,
        'id': 690
    }
    los_angeles_lakers = {
        'sport': Sport.nba,
        'id': 13
    }
    memphis_grizzlies = {
        'sport': Sport.nba,
        'id': 29
    }
    miami_heat = {
        'sport': Sport.nba,
        'id': 14
    }
    milwaukee_bucks = {
        'sport': Sport.nba,
        'id': 15
    }
    minnesota_timberwolves = {
        'sport': Sport.nba,
        'id': 16
    }
    new_orleans_pelicans = {
        'sport': Sport.nba,
        'id': 3
    }
    new_york_knicks = {
        'sport': Sport.nba,
        'id': 18
    }
    oklahoma_city_thunder = {
        'sport': Sport.nba,
        'id': 25
    }
    orlando_magic = {
        'sport': Sport.nba,
        'id': 19
    }
    philadelphia_76ers = {
        'sport': Sport.nba,
        'id': 20
    }
    phoenix_suns = {
        'sport': Sport.nba,
        'id': 21
    }
    portland_trail_blazers = {
        'sport': Sport.nba,
        'id': 22
    }
    sacramento_kings = {
        'sport': Sport.nba,
        'id': 23
    }
    san_antonio_spurs = {
        'sport': Sport.nba,
        'id': 24
    }
    toronto_raptors = {
        'sport': Sport.nba,
        'id': 28
    }
    utah_jazz = {
        'sport': Sport.nba,
        'id': 26
    }
    washington_wizards = {
        'sport': Sport.nba,
        'id': 27
    }

    @staticmethod
    def value_of(draft_kings_id):
        assert isinstance(draft_kings_id, int)

        for team in Team:
            if team.value['id'] == draft_kings_id:
                return team

        raise ValueError('Unable to identify team for id: %s', draft_kings_id)
