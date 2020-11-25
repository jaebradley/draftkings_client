from marshmallow import Schema, fields, EXCLUDE
from marshmallow_enum import EnumField

from draft_kings.data import Sport


class PlayerNameDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    display = fields.Str(missing=None)
    first = fields.Str(missing=None)
    last = fields.Str(missing=None)
    short = fields.Str(missing=None)


class PlayerImageDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    fifty_pixels_by_fifty_pixels_url = fields.Str(missing=None)
    one_hundred_and_sixty_pixels_by_one_hundred_pixels_url = fields.Str(missing=None)


class PlayerCompetitionDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    competition_id = fields.Int(missing=None)
    name = fields.Str(missing=None)
    starts_at = fields.AwareDateTime(missing=None)


class PlayerTeamDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    abbreviation = fields.Str(missing=None)
    team_id = fields.Int(missing=None)


class PlayerSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    competition_details = fields.Nested(PlayerCompetitionDetailsSchema, missing=None)
    draftable_id = fields.Int(missing=None)
    image_details = fields.Nested(PlayerImageDetailsSchema, missing=None)
    is_disabled = fields.Bool(missing=None)
    is_swappable = fields.Bool(missing=None)
    name_details = fields.Nested(PlayerNameDetailsSchema, missing=None)
    news_status_description = fields.Str(missing=None)
    player_id = fields.Int(missing=None)
    position_name = fields.Str(missing=None)
    roster_slot_id = fields.Int(missing=None)
    salary = fields.Float(missing=None)
    team_details = fields.Nested(PlayerTeamDetailsSchema, missing=None)


class CompetitionTeamSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    abbreviation = fields.Str(missing=None)
    city = fields.Str(missing=None)
    name = fields.Str(missing=None)
    team_id = fields.Int(missing=None)


class CompetitionWeatherSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    description = fields.Str(missing=None)
    is_in_a_dome = fields.Bool(missing=None)


class CompetitionSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    are_depth_charts_available = fields.Bool(missing=None)
    are_starting_lineups_available = fields.Bool(missing=None)
    away_team = fields.Nested(CompetitionTeamSchema, missing=None)
    competition_id = fields.Int(missing=None)
    home_team = fields.Nested(CompetitionTeamSchema, missing=None)
    name = fields.Str(missing=None)
    sport = EnumField(Sport, missing=None)
    starts_at = fields.AwareDateTime(missing=None)
    state_description = fields.Str(missing=None)
    venue = fields.Str(missing=None)
    weather = fields.Nested(CompetitionWeatherSchema, missing=None)


class DraftablesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    players = fields.List(fields.Nested(PlayerSchema), missing=[])
    competitions = fields.List(fields.Nested(CompetitionSchema), missing=[])
