# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.output.objects.draft_group import ContestDetails, StartTimeDetails, LeagueDetails, GameDetails, \
    DraftGroupDetails
from draft_kings.output.schema.fields import CustomAwareDateTime


class ContestDetailsSchema(Schema):
    game_type_description = fields.Str(allow_none=True, required=True)
    type_id = fields.Int(allow_none=True, required=True)

    @post_load
    def make_contest_details(self, data, **kwargs):
        return ContestDetails(**data)


class StartTimeDetailsSchema(Schema):
    maximum = CustomAwareDateTime(allow_none=True, required=True)
    minimum = CustomAwareDateTime(allow_none=True, required=True)
    type_description = fields.Str(allow_none=True, required=True)

    @post_load
    def make_start_time_details(self, data, **kwargs):
        return StartTimeDetails(**data)


class LeagueDetailsSchema(Schema):
    abbreviation = fields.Str(allow_none=True, required=True)
    league_id = fields.Int(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)

    @post_load
    def make_league_details(self, data, **kwargs):
        return LeagueDetails(**data)


class GameDetailsSchema(Schema):
    away_team_id = fields.Int(allow_none=True, required=True)
    description = fields.Str(allow_none=True, required=True)
    game_id = fields.Int(allow_none=True, required=True)
    home_team_id = fields.Int(allow_none=True, required=True)
    location = fields.Str(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)
    starts_at = CustomAwareDateTime(allow_none=True, required=True)
    status_description = fields.Str(allow_none=True, required=True)

    @post_load
    def make_game_details(self, data, **kwargs):
        return GameDetails(**data)


class DraftGroupDetailsSchema(Schema):
    contest_details = fields.Nested(ContestDetailsSchema, required=True)
    draft_group_id = fields.Int(allow_none=True, required=True)
    games = fields.List(fields.Nested(GameDetailsSchema, required=True), required=True)
    leagues = fields.List(fields.Nested(LeagueDetailsSchema, required=True), required=True)
    sport = EnumField(Sport, allow_none=True, required=True, by_value=True)
    start_time_details = fields.Nested(StartTimeDetailsSchema, required=True)
    state_description = fields.Str(allow_none=True, required=True)

    @post_load
    def make_draft_group_details(self, data, **kwargs):
        return DraftGroupDetails(**data)

# pylint: enable=unused-argument, no-self-use
