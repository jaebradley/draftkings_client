from typing import Optional, List


class ContestType:
    def __init__(self, contest_type_id: Optional[int], game_type: Optional[str]):
        self.contest_type_id = contest_type_id
        self.game_type = game_type

    def __eq__(self, other):
        if type(other) is type(self):
            return self.contest_type_id == other.contest_type_id \
                and self.game_type == other.game_type

        return False


class League:
    def __init__(self, league_abbreviation: Optional[str], league_id: Optional[int], league_name: Optional[str]):
        self.league_abbreviation = league_abbreviation
        self.league_id = league_id
        self.league_name = league_name

    def __eq__(self, other):
        if type(other) is type(self):
            return self.league_abbreviation == other.league_abbreviation \
                and self.league_id == other.league_id \
                and self.league_name == other.league_name

        return False


class Game:
    def __init__(self, away_team_id: Optional[int], description: Optional[str], game_id: Optional[int],
                 home_team_id: Optional[int], location: Optional[str], name: Optional[str],
                 start_date: Optional[str], status: Optional[str]) -> None:
        self.away_team_id = away_team_id
        self.description = description
        self.game_id = game_id
        self.home_team_id = home_team_id
        self.location = location
        self.name = name
        self.start_date = start_date
        self.status = status

    def __eq__(self, other):
        if type(other) is type(self):
            return self.away_team_id == other.away_team_id \
                and self.description == other.description \
                and self.game_id == other.game_id \
                and self.home_team_id == other.home_team_id \
                and self.location == other.location \
                and self.name == other.name \
                and self.start_date == other.start_date \
                and self.status == other.status

        return False


class DraftGroup:
    def __init__(self, contest_type: ContestType, draft_group_id: Optional[int], draft_group_state: Optional[str],
                 games: List[Game], leagues: List[League], max_start_time: Optional[str],
                 min_start_time: Optional[str], sport_id: Optional[int], start_time_type: Optional[str]) -> None:
        self.contest_type = contest_type
        self.draft_group_id = draft_group_id
        self.draft_group_state = draft_group_state
        self.games = games
        self.leagues = leagues
        self.max_start_time = max_start_time
        self.min_start_time = min_start_time
        self.sport_id = sport_id
        self.start_time_type = start_time_type

    def __eq__(self, other):
        if type(other) is type(self):
            return self.contest_type == other.contest_type \
                and self.draft_group_id == other.draft_group_id \
                and self.draft_group_state == other.draft_group_state \
                and self.games == other.games \
                and self.leagues == other.leagues \
                and self.max_start_time == other.max_start_time \
                and self.min_start_time == other.min_start_time \
                and self.sport_id == other.sport_id \
                and self.start_time_type == other.start_time_type

        return False


class DraftGroupResponse:
    def __init__(self, draft_group: DraftGroup):
        self.draft_group = draft_group
