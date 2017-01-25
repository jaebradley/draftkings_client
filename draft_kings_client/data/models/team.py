from enum import Enum

from sport import Sport


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
        'id': 684
    }
    denver_nuggets = {
        'sport': Sport.nba,
        'id': 685
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
        'id': 692
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
        'id': 700
    }
    philadelphia_76ers = {
        'sport': Sport.nba,
        'id': 701
    }
    phoenix_suns = {
        'sport': Sport.nba,
        'id': 702
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
