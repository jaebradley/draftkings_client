from marshmallow import Schema, fields, EXCLUDE


class ContestDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    game_type = fields.Str(missing=None)
    type_id = fields.Int(missing=None)


class StartsAtDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    maximum = fields.AwareDateTime(missing=None)
    minimum = fields.AwareDateTime(missing=None)
    type_description = fields.Str(missing=None)


class LeagueDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    abbreviation = fields.Str(missing=None)
    league_id = fields.Int(missing=None)
    name = fields.Str(missing=None)


class GameDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    away_team_id = fields.Int(missing=None)
    description = fields.Str(missing=None)
    game_id = fields.Int(missing=None)
    home_team_id = fields.Int(missing=None)
    location = fields.Str(missing=None)
    name = fields.Str(missing=None)
    starts_at = fields.AwareDateTime(missing=None)
    status = fields.Str(missing=None)


class DraftGroupSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    contest_details = fields.Nested(ContestDetailsSchema, required=True)
    draft_group_id = fields.Int(missing=None)
    games = fields.List(fields.Nested(GameDetailsSchema, required=True), missing=[])
    leagues = fields.List(fields.Nested(LeagueDetailsSchema, required=True), missing=None)
    sport = fields.Str(missing=None)
    starts_at = fields.Nested(StartsAtDetailsSchema, required=True)
    state = fields.Str(missing=None)
