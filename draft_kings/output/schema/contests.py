from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from draft_kings.data import Sport


class EntriesDetailsSchema(Schema):
    fee = fields.Number(missing=None)
    maximum = fields.Integer(missing=None)
    total = fields.Integer(missing=None)


class DraftGroupSchema(Schema):
    contest_type_id = fields.Integer(missing=None)
    draft_group_id = fields.Integer(missing=None)
    games_count = fields.Integer(missing=None)
    series_id = fields.Integer(missing=None)
    sport = EnumField(Sport, by_value=True)
    starts_at = fields.Str(missing=None)


class ContestSchema(Schema):
    contest_id = fields.Integer(missing=None)
    draft_group_id = fields.Integer(missing=None)
    entries_details = fields.Nested(EntriesDetailsSchema(), required=True)
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
    draft_groups = fields.List(fields.Nested(DraftGroupSchema()), default=[])
