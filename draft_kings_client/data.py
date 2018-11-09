from enum import Enum


class Sport(Enum):
    NFL = "NFL"
    NHL = "NHL"
    NBA = "NBA"
    NASCAR = "NASCAR"
    SOCCER = "SOCCER"
    GOLF = "GOLF"
    CFL = "CFL"
    COLLEGE_FOOTBALL = "COLLEGE FOOTBALL"
    COLLEGE_BASKETBALL = "COLLEGE BASKETBALL"
    MIXED_MARTIAL_ARTS = "MIXED MARTIAL ARTS"
    EUROLEAGUE_BASKETBALL = "EUROLEAGUE BASKETBALL"
    MLB = "MLB"
    TENNIS = "TENNIS"
    LEAGUE_OF_LEGENDS = "LEAGUE OF LEGENDS"


class Position(Enum):
    point_guard = {
        'sport': Sport.NBA,
        'abbreviation': 'PG',
        'name': 'Point Guard'
    }
    shooting_guard = {
        'sport': Sport.NBA,
        'abbreviation': 'SG',
        'name': 'Shooting Guard'
    }
    small_forward = {
        'sport': Sport.NBA,
        'abbreviation': 'SF',
        'name': 'Small Forward'
    }
    power_forward = {
        'sport': Sport.NBA,
        'abbreviation': 'PF',
        'name': 'Power Forward'
    }
    center = {
        'sport': Sport.NBA,
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
        'sport': Sport.NBA,
        'id': 1
    }
    boston_celtics = {
        'sport': Sport.NBA,
        'id': 2
    }
    brooklyn_nets = {
        'sport': Sport.NBA,
        'id': 17
    }
    charlotte_hornets = {
        'sport': Sport.NBA,
        'id': 5312
    }
    chicago_bulls = {
        'sport': Sport.NBA,
        'id': 4
    }
    cleveland_cavaliers = {
        'sport': Sport.NBA,
        'id': 5
    }
    dallas_mavericks = {
        'sport': Sport.NBA,
        'id': 6
    }
    denver_nuggets = {
        'sport': Sport.NBA,
        'id': 7
    }
    detroit_pistons = {
        'sport': Sport.NBA,
        'id': 8
    }
    golden_state_warriors = {
        'sport': Sport.NBA,
        'id': 9
    }
    houston_rockets = {
        'sport': Sport.NBA,
        'id': 10
    }
    indiana_pacers = {
        'sport': Sport.NBA,
        'id': 11
    }
    los_angeles_clippers = {
        'sport': Sport.NBA,
        'id': 690
    }
    los_angeles_lakers = {
        'sport': Sport.NBA,
        'id': 13
    }
    memphis_grizzlies = {
        'sport': Sport.NBA,
        'id': 29
    }
    miami_heat = {
        'sport': Sport.NBA,
        'id': 14
    }
    milwaukee_bucks = {
        'sport': Sport.NBA,
        'id': 15
    }
    minnesota_timberwolves = {
        'sport': Sport.NBA,
        'id': 16
    }
    new_orleans_pelicans = {
        'sport': Sport.NBA,
        'id': 3
    }
    new_york_knicks = {
        'sport': Sport.NBA,
        'id': 18
    }
    oklahoma_city_thunder = {
        'sport': Sport.NBA,
        'id': 25
    }
    orlando_magic = {
        'sport': Sport.NBA,
        'id': 19
    }
    philadelphia_76ers = {
        'sport': Sport.NBA,
        'id': 20
    }
    phoenix_suns = {
        'sport': Sport.NBA,
        'id': 21
    }
    portland_trail_blazers = {
        'sport': Sport.NBA,
        'id': 22
    }
    sacramento_kings = {
        'sport': Sport.NBA,
        'id': 23
    }
    san_antonio_spurs = {
        'sport': Sport.NBA,
        'id': 24
    }
    toronto_raptors = {
        'sport': Sport.NBA,
        'id': 28
    }
    utah_jazz = {
        'sport': Sport.NBA,
        'id': 26
    }
    washington_wizards = {
        'sport': Sport.NBA,
        'id': 27
    }

    @staticmethod
    def value_of(draft_kings_id):
        assert isinstance(draft_kings_id, int)

        for team in Team:
            if team.value['id'] == draft_kings_id:
                return team

        raise ValueError('Unable to identify team for id: %s', draft_kings_id)
