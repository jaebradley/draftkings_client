from marshmallow import Schema, fields, post_load

from draft_kings.output.objects.draft_group import ContestDetails, StartTimeDetails, LeagueDetails, GameDetails, \
    DraftGroupDetails
from draft_kings.output.schema.fields import CustomAwareDateTime


class ContestDetailsSchema(Schema):
    game_type_description = fields.Str(missing=None)
    type_id = fields.Int(missing=None)

    @post_load
    def make_contest_details(self, data, **kwargs):
        return ContestDetails(**data)


class StartTimeDetailsSchema(Schema):
    maximum = CustomAwareDateTime(missing=None)
    minimum = CustomAwareDateTime(missing=None)
    type_description = fields.Str(missing=None)

    @post_load
    def make_start_time_details(self, data, **kwargs):
        return StartTimeDetails(**data)


class LeagueDetailsSchema(Schema):
    abbreviation = fields.Str(missing=None)
    league_id = fields.Int(missing=None)
    name = fields.Str(missing=None)

    @post_load
    def make_league_details(self, data, **kwargs):
        return LeagueDetails(**data)


class GameDetailsSchema(Schema):
    away_team_id = fields.Int(missing=None)
    description = fields.Str(missing=None)
    game_id = fields.Int(missing=None)
    home_team_id = fields.Int(missing=None)
    location = fields.Str(missing=None)
    name = fields.Str(missing=None)
    starts_at = CustomAwareDateTime(missing=None)
    status_description = fields.Str(missing=None)

    @post_load
    def make_game_details(self, data, **kwargs):
        return GameDetails(**data)


class DraftGroupDetailsSchema(Schema):
    contest_details = fields.Nested(ContestDetailsSchema(), required=True)
    draft_group_id = fields.Int(missing=None)
    games = fields.List(fields.Nested(GameDetailsSchema(), required=True), missing=[])
    leagues = fields.List(fields.Nested(LeagueDetailsSchema(), required=True), missing=[])
    sport = fields.Str(missing=None)
    start_time_details = fields.Nested(StartTimeDetailsSchema(), required=True)
    state_description = fields.Str(missing=None)

    @post_load
    def make_draft_group_details(self, data, **kwargs):
        return DraftGroupDetails(**data)
