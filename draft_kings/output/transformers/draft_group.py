from typing import Callable

from dateutil.parser import parse as parse_datetime

from draft_kings.data import Sport
from draft_kings.output.objects.draft_group import ContestDetails, StartTimeDetails, LeagueDetails, GameDetails, \
    DraftGroupDetails
from draft_kings.response.objects.draft_group import ContestType as ResponseContestType, League as ResponseLeague, \
    Game as ResponseGame, DraftGroup as ResponseDraftGroup


def transform_contest(contest_type: ResponseContestType) -> ContestDetails:
    return ContestDetails(game_type=contest_type.game_type, type_id=contest_type.contest_type_id)


def transform_league(response_league: ResponseLeague) -> LeagueDetails:
    return LeagueDetails(
        abbreviation=response_league.league_abbreviation,
        league_id=response_league.league_id,
        name=response_league.league_name
    )


def transform_draft_group_starts_at(response_draft_group: ResponseDraftGroup) -> StartTimeDetails:
    return StartTimeDetails(
        maximum=parse_datetime(response_draft_group.max_start_time)
        if response_draft_group.max_start_time is not None else None,
        minimum=parse_datetime(response_draft_group.min_start_time)
        if response_draft_group.min_start_time is not None else None,
        type_description=response_draft_group.start_time_type,
    )


def transform_game(response_game: ResponseGame) -> GameDetails:
    return GameDetails(
        away_team_id=response_game.away_team_id,
        description=response_game.description,
        game_id=response_game.game_id,
        home_team_id=response_game.home_team_id,
        location=response_game.location,
        name=response_game.name,
        starts_at=parse_datetime(response_game.start_date),
        status=response_game.status
    )


class DraftGroupDetailsTransformer:
    def __init__(self, contest_transformer: Callable[[ResponseContestType], ContestDetails],
                 game_transformer: Callable[[ResponseGame], GameDetails],
                 league_transformer: Callable[[ResponseLeague], LeagueDetails],
                 sport_id_transformer: Callable[[int], Sport],
                 starts_at_transformer: Callable[[ResponseDraftGroup], StartTimeDetails]) -> None:
        self.contest_transformer = contest_transformer
        self.game_transformer = game_transformer
        self.league_transformer = league_transformer
        self.sport_id_transformer = sport_id_transformer
        self.starts_at_transformer = starts_at_transformer

    def transform(self, draft_group: ResponseDraftGroup) -> DraftGroupDetails:
        return DraftGroupDetails(
            contest_details=self.contest_transformer(draft_group.contest_type),
            draft_group_id=draft_group.draft_group_id,
            games=[self.game_transformer(game) for game in draft_group.games],
            leagues=[self.league_transformer(league) for league in draft_group.leagues],
            sport=self.sport_id_transformer(draft_group.sport_id),
            starts_at=self.starts_at_transformer(draft_group),
            state=draft_group.draft_group_state
        )