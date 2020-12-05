# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load

from draft_kings.output.objects.players import TeamSeriesDetails, DraftDetails, PlayerTeamSeriesDetails, \
    PositionDetails, PlayerDetails, PlayersDetails, ExceptionalMessageTypeDetails, ExceptionalMessageDetails
from draft_kings.output.schema.fields import CustomDateTime


class TeamSeriesDetailsSchema(Schema):
    away_team_id = fields.Integer(allow_none=True, required=True)
    home_team_id = fields.Integer(allow_none=True, required=True)
    starts_at = CustomDateTime(allow_none=True, required=True)
    status_description = fields.Str(allow_none=True, required=True)
    team_series_id = fields.Integer(allow_none=True, required=True)
    weather_description = fields.Str(allow_none=True, required=True)

    @post_load
    def make_team_series_details(self, data, **kwargs):
        return TeamSeriesDetails(**data)


class DraftDetailsSchema(Schema):
    is_draftable = fields.Bool(allow_none=True, required=True)
    salary = fields.Float(allow_none=True, required=True)
    starts_at = CustomDateTime(allow_none=True, required=True)

    @post_load
    def make_draft_details(self, data, **kwargs):
        return DraftDetails(**data)


class PlayerTeamSeriesDetailsSchema(Schema):
    away_team_id = fields.Integer(allow_none=True, required=True)
    home_team_id = fields.Integer(allow_none=True, required=True)
    opposition_rank = fields.Integer(allow_none=True, required=True)
    team_series_id = fields.Integer(allow_none=True, required=True)

    @post_load
    def make_player_team_series_details(self, data, **kwargs):
        return PlayerTeamSeriesDetails(**data)


class PositionDetailsSchema(Schema):
    name = fields.Str(allow_none=True, required=True)
    position_id = fields.Integer(allow_none=True, required=True)

    @post_load
    def make_player_position_details(self, data, **kwargs):
        return PositionDetails(**data)


class ExceptionalMessageTypeDetailsSchema(Schema):
    name = fields.Str(allow_none=True, required=True)

    @post_load
    def make_exceptional_message_type(self, data, **kwargs):
        return ExceptionalMessageTypeDetails(**data)


class ExceptionalMessageDetailsSchema(Schema):
    message = fields.Str(allow_none=True, required=True)
    priority_value = fields.Int(allow_none=True, required=True)
    type_details = fields.Nested(ExceptionalMessageTypeDetailsSchema, allow_none=True, required=True)

    @post_load
    def make_exceptional_message_details(self, data, **kwargs):
        return ExceptionalMessageDetails(**data)


class PlayerDetailsSchema(Schema):
    draft_details = fields.Nested(DraftDetailsSchema, required=True)
    exceptional_messages = fields.List(fields.Nested(ExceptionalMessageDetailsSchema, required=True), required=True)
    first_name = fields.Str(allow_none=True, required=True)
    jersey_number = fields.Integer(allow_none=True, required=True)
    last_name = fields.Str(allow_none=True, required=True)
    player_id = fields.Integer(allow_none=True, required=True)
    points_per_game = fields.Float(allow_none=True, required=True)
    position_details = fields.Nested(PositionDetailsSchema, required=True)
    team_id = fields.Integer(allow_none=True, required=True)
    team_series_details = fields.Nested(PlayerTeamSeriesDetailsSchema, required=True)

    @post_load
    def make_player(self, data, **kwargs):
        return PlayerDetails(**data)


class PlayersDetailsSchema(Schema):
    players = fields.List(fields.Nested(PlayerDetailsSchema, required=True), required=True)
    team_series = fields.List(fields.Nested(TeamSeriesDetailsSchema, required=True), required=True)

    @post_load
    def make_players_details(self, data, **kwargs):
        return PlayersDetails(**data)

# pylint: enable=unused-argument, no-self-use
