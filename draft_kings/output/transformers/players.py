from datetime import datetime
from typing import Callable, Optional

from draft_kings.output.objects.players import TeamSeriesDetails, PlayersDetails, DraftDetails, \
    PlayerTeamSeriesDetails, PositionDetails, PlayerDetails, ExceptionalMessageDetails, ExceptionalMessageTypeDetails
from draft_kings.response.objects.players import TeamSeries as ResponsePlayerTeamSeries, PlayersDetails as \
    ResponsePlayersDetails, Player as ResponsePlayerDetails, ExceptionalMessage as ResponseExceptionalMessage, \
    ExceptionalMessageType as ResponseExceptionalMessageType


def transform_exceptional_message_type(
        exceptional_message_type: ResponseExceptionalMessageType
) -> ExceptionalMessageTypeDetails:
    return ExceptionalMessageTypeDetails(name=exceptional_message_type.name)


class ExceptionalMessageTransformer:
    def __init__(self, message_type_transformer: Callable[[ResponseExceptionalMessageType],
                                                          ExceptionalMessageTypeDetails]):
        self.message_type_transformer = message_type_transformer

    def transform(self, exception_message: ResponseExceptionalMessage) -> ExceptionalMessageDetails:
        return ExceptionalMessageDetails(
            message=exception_message.message,
            priority_value=exception_message.priority,
            type_details=self.message_type_transformer(exception_message.message_type) if
            exception_message.message_type is not None else None
        )


class TeamSeriesTransformer:
    def __init__(self, formatted_datetime_translator: Callable[[str], datetime]):
        self.formatted_datetime_translator = formatted_datetime_translator

    def transform(self, team_series_id: Optional[int],
                  team_series_response: ResponsePlayerTeamSeries) -> TeamSeriesDetails:
        return TeamSeriesDetails(
            away_team_id=team_series_response.away_team_id,
            home_team_id=team_series_response.home_team_id,
            starts_at=self.formatted_datetime_translator(team_series_response.starts_at) if
            team_series_response.starts_at is not None else None,
            status_description=team_series_response.status,
            team_series_id=int(team_series_id) if team_series_id is not None else None,
            weather_description=team_series_response.weather
        )


class DraftDetailsTransformer:
    def __init__(self, unix_milliseconds_translator: Callable[[int], datetime]):
        self.unix_milliseconds_translator = unix_milliseconds_translator

    def transform(self, player_details: ResponsePlayerDetails) -> DraftDetails:
        return DraftDetails(
            is_draftable=player_details.is_disabled_from_drafting is False,
            salary=player_details.salary,
            starts_at=self.unix_milliseconds_translator(player_details.draft_group_start_time) if
            player_details.draft_group_start_time is not None else None
        )


def transform_player_team_series_details(player_details: ResponsePlayerDetails) -> PlayerTeamSeriesDetails:
    return PlayerTeamSeriesDetails(
        away_team_id=player_details.away_team_id,
        home_team_id=player_details.home_team_id,
        opposition_rank=player_details.opposition_rank,
        team_series_id=player_details.team_series_id
    )


def transform_player_position(player_details: ResponsePlayerDetails) -> PositionDetails:
    return PositionDetails(
        name=player_details.position_name,
        position_id=player_details.position_id
    )


class PlayerDetailsTransformer:
    def __init__(self, draft_details_transformer: DraftDetailsTransformer,
                 player_team_series_details_transformer: Callable[[ResponsePlayerDetails], PlayerTeamSeriesDetails],
                 player_position_transformer: Callable[[ResponsePlayerDetails], PositionDetails],
                 exceptional_message_transformer: ExceptionalMessageTransformer):
        self.draft_details_transformer = draft_details_transformer
        self.player_team_series_details_transformer = player_team_series_details_transformer
        self.player_position_transformer = player_position_transformer
        self.exceptional_message_transformer = exceptional_message_transformer

    def transform(self, player_details: ResponsePlayerDetails) -> PlayerDetails:
        return PlayerDetails(
            draft_details=self.draft_details_transformer.transform(player_details),
            exceptional_messages=list(
                map(
                    self.exceptional_message_transformer.transform,
                    player_details.exceptional_messages
                )
            ),
            first_name=player_details.first_name,
            jersey_number=player_details.jersey_number,
            last_name=player_details.last_name,
            player_id=player_details.player_id,
            points_per_game=float(player_details.points_per_game)
            if player_details.points_per_game is not None else None,
            position_details=self.player_position_transformer(player_details),
            team_id=player_details.team_id,
            team_series_details=self.player_team_series_details_transformer(player_details)
        )


class PlayersDetailsTransformer:
    def __init__(self, team_series_transformer: TeamSeriesTransformer,
                 player_details_transformer: PlayerDetailsTransformer):
        self.team_series_transformer = team_series_transformer
        self.player_details_transformer = player_details_transformer

    def transform(self, players_details_response: ResponsePlayersDetails) -> PlayersDetails:
        return PlayersDetails(
            players=list(map(
                self.player_details_transformer.transform,
                players_details_response.players
            )),
            team_series=list(map(
                lambda team_series_item:
                self.team_series_transformer.transform(
                    team_series_id=team_series_item[0],
                    team_series_response=team_series_item[1]
                ),
                players_details_response.team_series.items()
            ))
        )
