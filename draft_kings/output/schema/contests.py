from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.output.objects.contests import EntriesDetails, DraftGroupDetails, ContestDetails, ContestsDetails


class EntriesDetailsSchema(Schema):
    fee = fields.Number(missing=None)
    maximum = fields.Integer(missing=None)
    total = fields.Integer(missing=None)

    @post_load
    def make_entries_details(self, data, **kwargs):
        return EntriesDetails(**data)


class DraftGroupDetailsSchema(Schema):
    contest_type_id = fields.Integer(missing=None)
    draft_group_id = fields.Integer(missing=None)
    games_count = fields.Integer(missing=None)
    series_id = fields.Integer(missing=None)
    sport = EnumField(Sport, by_value=True)
    starts_at = fields.Str(missing=None)

    @post_load
    def make_draft_group_details(self, data, **kwargs):
        return DraftGroupDetails(**data)


class ContestDetailsSchema(Schema):
    contest_id = fields.Integer(missing=None)
    draft_group_id = fields.Integer(missing=None)
    entries_details = fields.Nested(EntriesDetailsSchema(), required=True)
    fantasy_player_points = fields.Number(missing=None)
    is_double_up = fields.Bool(missing=False)
    is_fifty_fifty = fields.Bool(missing=False)
    is_guaranteed = fields.Bool(missing=False)
    is_head_to_head = fields.Bool(missing=False)
    is_starred = fields.Bool(missing=False)
    name = fields.Str(missing=None)
    payout = fields.Number(missing=None)
    sport = EnumField(Sport, by_value=True, missing=None)
    starts_at = fields.DateTime(missing=None)

    @post_load
    def make_contest_details(self, data, **kwargs):
        return ContestDetails(**data)


class ContestsDetailsSchema(Schema):
    contests = fields.List(fields.Nested(ContestDetailsSchema()), missing=[])
    draft_groups = fields.List(fields.Nested(DraftGroupDetailsSchema()), missing=[])

    @post_load
    def make_contests_details(self, data, **kwargs):
        return ContestsDetails(**data)
