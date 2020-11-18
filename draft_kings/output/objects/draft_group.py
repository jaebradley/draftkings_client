from datetime import datetime
from typing import Optional, List


class ContestDetails:
    def __init__(self, game_type: Optional[str], type_id: Optional[int]) -> None:
        self.game_type = game_type
        self.type_id = type_id

    def __eq__(self, other) -> bool:
        if type(other) is type(self):
            return self.game_type == other.game_type \
                   and self.type_id == other.type_id

        return False


class StartsAtDetails:
    def __init__(self, maximum: Optional[datetime], minimum: Optional[datetime],
                 type_description: Optional[str]) -> None:
        self.maximum = maximum
        self.minimum = minimum
        self.type_description = type_description

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.maximum == other.maximum \
                   and self.minimum == other.minimum \
                   and self.type_description == other.type_description

        return False


class LeagueDetails:
    def __init__(self, abbreviation: Optional[str], league_id: Optional[int], name: Optional[str]) -> None:
        self.abbreviation = abbreviation
        self.league_id = league_id
        self.name = name

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.abbreviation == other.abbreviation \
                   and self.league_id == other.league_id \
                   and self.name == other.name

        return False


class GameDetails:
    def __init__(self, away_team_id: Optional[int], description: Optional[str], game_id: Optional[str],
                 home_team_id: Optional[int], location: Optional[str], name: Optional[str],
                 starts_at: Optional[datetime], status: Optional[str]) -> None:
        self.away_team_id = away_team_id
        self.description = description
        self.game_id = game_id
        self.home_team_id = home_team_id
        self.location = location
        self.name = name
        self.starts_at = starts_at
        self.status = status

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.away_team_id == other.away_team_id \
                   and self.description == other.description \
                   and self.game_id == other.game_id \
                   and self.home_team_id == other.home_team_id \
                   and self.location == other.location \
                   and self.name == other.name \
                   and self.starts_at == other.starts_at \
                   and self.status == other.status

        return False


class DraftGroupDetails:
    def __init__(self, contest_details: ContestDetails, draft_group_id: Optional[int], games: List[GameDetails],
                 leagues: List[LeagueDetails], sport: Optional[str], starts_at: StartsAtDetails,
                 state: Optional[str]) -> None:
        self.contest_details = contest_details
        self.draft_group_id = draft_group_id
        self.games = games
        self.leagues = leagues
        self.sport = sport
        self.starts_at = starts_at
        self.state = state

    def __eq__(self, other):
        if type(self) is type(other):
            return self.contest_details == other.contest_details \
                and self.draft_group_id == other.draft_group_id \
                and self.games == other.games \
                and self.leagues == other.leagues \
                and self.sport == other.sport \
                and self.starts_at == other.starts_at \
                and self.state == other.state

        return False
