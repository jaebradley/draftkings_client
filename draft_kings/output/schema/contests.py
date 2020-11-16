from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from draft_kings.data import Sport


class ContestEntryDetailsSchema(Schema):
    maximum = fields.Number(missing=None)
    fee = fields.Number(missing=None)
    total = fields.Number(missing=None)


class ContestDraftGroupSchema(Schema):
    draft_group_id = fields.Integer(missing=None)
    series_id = fields.Integer(missing=None)
    contest_type_id = fields.Integer(missing=None)
    sport = EnumField(Sport, by_value=True)
    starts_at = fields.Str(missing=None)
    games_count = fields.Integer(missing=None)


class ContestSchema(Schema):
    contest_id = fields.Integer(missing=None)
    draft_group_id = fields.Integer(missing=None)
    entry_details = fields.Nested(ContestEntryDetailsSchema(), missing={})
    fantasy_player_points = fields.Number(missing=None)
    is_double_up = fields.Bool(required=True, default=False)
    is_fifty_fifty = fields.Bool(required=True, default=False)
    is_guaranteed = fields.Bool(required=True, default=False)
    is_head_to_head = fields.Bool(required=True, default=False)
    is_starred = fields.Bool(required=True, default=False)
    name = fields.Str(missing=None)
    payout = fields.Number(missing=None)
    sport = fields.Str(missing=None)
    starts_at = fields.DateTime(missing=None)


class ContestsDetailsSchema(Schema):
    contests = fields.List(fields.Nested(ContestSchema()), default=[])
    groups = fields.List(fields.Nested(ContestDraftGroupSchema()), default=[])
