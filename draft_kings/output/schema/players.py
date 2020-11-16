from marshmallow import Schema, fields


class TeamSeriesSchema(Schema):
    away_team_id = fields.Integer(missing=None)
    home_team_id = fields.Integer(missing=None)
    starts_at = fields.DateTime(missing=None)
    status = fields.Str(missing=None)
    team_series_id = fields.Integer(missing=None)
    weather_description = fields.Str(missing=None)


class DraftDetailsSchema(Schema):
    exceptional_messages = fields.List(fields.Nested(fields.Str, missing=None), missing=[])
    is_draftable = fields.Bool(missing=None)
    salary = fields.Float(missing=None)
    starts_at = fields.DateTime(missing=None)


class PlayerTeamSeriesDetailsSchema(Schema):
    away_team_id = fields.Integer(missing=None)
    home_team_id = fields.Integer(missing=None)
    opposition_rank = fields.Integer(missing=None)
    team_series_id = fields.Integer(missing=None)


class PlayerPositionSchema(Schema):
    name = fields.Str(missing=None)
    position_id = fields.Integer(missing=None)


class PlayerSchema(Schema):
    draft_details = fields.Nested(DraftDetailsSchema, missing={})
    first_name = fields.Str(missing=None)
    jersey_number = fields.Integer(missing=None)
    last_name = fields.Str(missing=None)
    player_id = fields.Integer(missing=None)
    points_per_game = fields.Float(missing=None)
    position = fields.Nested(PlayerPositionSchema, missing={})
    team_id = fields.Integer(missing=None)
    team_series = fields.Nested(PlayerTeamSeriesDetailsSchema, missing={})
