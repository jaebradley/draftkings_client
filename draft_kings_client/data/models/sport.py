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
        for key, value in draft_kings_sport_ids.iteritems():
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
