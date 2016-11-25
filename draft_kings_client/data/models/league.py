from enum import Enum


class League(Enum):
    nfl = "nfl"
    nhl = "nhl"
    nba = "nba"
    nascar = "nas"
    soccer = "soc"
    golf = "golf"
    cfl = "cfl"

    def get_id(self):
        return draft_kings_league_ids.get(self)

    @staticmethod
    def from_id(league_id):
        for key, value in draft_kings_league_ids.iteritems():
            if league_id == value:
                return key

        raise ReferenceError('unknown league id')

draft_kings_league_ids = {
    League.nfl: 1,
    League.nhl: 3,
    League.nba: 4,
    League.nascar: 10,
    League.soccer: 12,
    League.golf: 13,
    League.cfl: 14
}
