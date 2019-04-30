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