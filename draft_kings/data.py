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
    ARENA_FOOTBALL_LEAGUE = "ARENA FOOTBALL LEAGUE"

"""
https://api.draftkings.com/sites/US-DK/sports/v1/sports?format=json
"""
SPORT_ID_TO_SPORT = {
    1: Sport.NFL,
    2: Sport.MLB,
    3: Sport.NHL,
    4: Sport.NBA,
    6: Sport.COLLEGE_BASKETBALL,
    5: Sport.COLLEGE_FOOTBALL,
    9: Sport.MIXED_MARTIAL_ARTS,
    10: Sport.NASCAR,
    11: Sport.LEAGUE_OF_LEGENDS,
    12: Sport.SOCCER,
    13: Sport.GOLF,
    14: Sport.CFL,
    15: Sport.EUROLEAGUE_BASKETBALL,
    16: Sport.TENNIS,
    17: Sport.ARENA_FOOTBALL_LEAGUE,
}


class CountryData:
    def __init__(self, country_id, code, name, licensed):
        self.country_id = country_id
        self.code = code
        self.name = name
        self.licensed = licensed

    def asdict(self):
        return {
            "id": self.country_id,
            "code": self.code,
            "name": self.name,
            "licensed": self.licensed
        }

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, CountryData):
            return self.country_id == other.country_id \
                and self.code == other.code \
                and self.name == other.name \
                and self.licensed == other.licensed
        return False

    def __repr__(self):
        return "Country id: {id} | code: {code} | name: {name} | licensed: {licensed}".format(
            id=self.country_id, code=self.code, name=self.name, licensed=self.licensed
        )

    def __str__(self):
        return "Country {name}".format(name=self.name)
