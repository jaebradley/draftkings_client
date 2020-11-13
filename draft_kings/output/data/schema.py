from marshmallow import Schema, fields, post_dump
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.output.data.objects import ContestDraftGroup, ContestEntryDetails, Contest, ContestsDetails


class ContestEntryDetailsSchema(Schema):
    maximum = fields.Number()
    fee = fields.Number()
    total = fields.Number()


class ContestDraftGroupSchema(Schema):
    draft_group_id = fields.Integer()
    series_id = fields.Integer()
    contest_type_id = fields.Integer()
    sport = EnumField(Sport, by_value=True)
    starts_at = fields.Str()
    games_count = fields.Integer()


class ContestSchema(Schema):
    contest_id = fields.Integer()
    draft_group_id = fields.Integer()
    entry_details = fields.Nested(ContestEntryDetailsSchema())
    fantasy_player_points = fields.Number()
    is_double_up = fields.Bool()
    is_fifty_fifty = fields.Bool()
    is_guaranteed = fields.Bool()
    is_head_to_head = fields.Bool()
    is_starred = fields.Bool()
    name = fields.Str()
    payout = fields.Number()
    sport = fields.Str()
    starts_at = fields.Str()


class ContestsDetailsSchema(Schema):
    contests = fields.List(fields.Nested(ContestSchema()), default=[])
    groups = fields.List(fields.Nested(ContestDraftGroupSchema()), default=[])
