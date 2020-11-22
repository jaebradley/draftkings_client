from typing import Callable, Optional

from draft_kings.output.objects.players import TeamSeries, PlayersDetails, DraftDetails, PlayerTeamSeriesDetails, \
    PlayerPosition, Player
from draft_kings.response.objects.players import TeamSeries as ResponsePlayerTeamSeries, PlayersDetails as \
    ResponsePlayersDetails, PlayerDetails as ResponsePlayerDetails
from draft_kings.utilities import translate_formatted_datetime, from_unix_milliseconds_to_datetime


def transform_team_series(team_series_id: Optional[int], team_series_response: ResponsePlayerTeamSeries) -> TeamSeries:
    return TeamSeries(
        away_team_id=team_series_response.away_team_id,
        home_team_id=team_series_response.home_team_id,
        starts_at=translate_formatted_datetime(team_series_response.starts_at),
        status=team_series_response.status,
        team_series_id=int(team_series_id),
        weather_description=team_series_response.weather
    )


def transform_draft_details(player_details: ResponsePlayerDetails) -> DraftDetails:
    return DraftDetails(
        exceptional_messages=player_details.exceptional_messages,
        is_draftable=player_details.is_disabled_from_drafting is False,
        salary=player_details.salary,
        starts_at=from_unix_milliseconds_to_datetime(player_details.draft_group_start_time)
    )


def transform_player_team_series_details(player_details: ResponsePlayerDetails) -> PlayerTeamSeriesDetails:
    return PlayerTeamSeriesDetails(
        away_team_id=player_details.away_team_id,
        home_team_id=player_details.home_team_id,
        opposition_rank=player_details.opposition_rank,
        team_series_id=player_details.team_series_id
    )


def transform_player_position(player_details: ResponsePlayerDetails) -> PlayerPosition:
    return PlayerPosition(
        name=player_details.position_name,
        position_id=player_details.position_id
    )


class PlayerDetailsTransformer:
    def __init__(self, draft_details_transformer: Callable[[ResponsePlayerDetails], DraftDetails],
                 player_team_series_details_transformer: Callable[[ResponsePlayerDetails], PlayerTeamSeriesDetails],
                 player_position_transformer: Callable[[ResponsePlayerDetails], PlayerPosition]):
        self.draft_details_transformer = draft_details_transformer
        self.player_team_series_details_transformer = player_team_series_details_transformer
        self.player_position_transformer = player_position_transformer

    def transform(self, player_details: ResponsePlayerDetails) -> Player:
        return Player(
            draft_details=self.draft_details_transformer(player_details),
            first_name=player_details.first_name,
            jersey_number=player_details.jersey_number,
            last_name=player_details.last_name,
            player_id=player_details.player_id,
            points_per_game=float(player_details.points_per_game),
            position=self.player_position_transformer(player_details),
            team_id=player_details.team_id,
            team_series=self.player_team_series_details_transformer(player_details)
        )


class PlayersDetailsTransformer:
    def __init__(self, team_series_transformer: Callable[[Optional[int], ResponsePlayerTeamSeries], TeamSeries],
                 player_details_transformer: PlayerDetailsTransformer):
        self.team_series_transformer = team_series_transformer
        self.player_details_transformer = player_details_transformer

    def transform(self, players_details_response: ResponsePlayersDetails) -> PlayersDetails:
        return PlayersDetails(
            players=[
                self.player_details_transformer.transform(player_details)
                for player_details in players_details_response.players
            ],
            team_series=[
                self.team_series_transformer(team_series_id=team_series_id, team_series_response=details)
                for team_series_id, details in players_details_response.team_series.items()
            ]
        )