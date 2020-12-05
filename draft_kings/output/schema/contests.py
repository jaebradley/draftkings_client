# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.output.objects.contests import EntriesDetails, DraftGroupDetails, ContestDetails, ContestsDetails
from draft_kings.output.schema.fields import CustomDateTime, CustomAwareDateTime


class EntriesDetailsSchema(Schema):
    fee = fields.Number(allow_none=True, required=True)
    maximum = fields.Integer(allow_none=True, required=True)
    total = fields.Integer(allow_none=True, required=True)

    @post_load
    def make_entries_details(self, data, **kwargs):
        return EntriesDetails(**data)


class DraftGroupDetailsSchema(Schema):
    contest_type_id = fields.Integer(allow_none=True, required=True)
    draft_group_id = fields.Integer(allow_none=True, required=True)
    games_count = fields.Integer(allow_none=True, required=True)
    series_id = fields.Integer(allow_none=True, required=True)
    sport = EnumField(Sport, allow_none=True, required=True, by_value=True)
    starts_at = CustomAwareDateTime(allow_none=True, required=True)

    @post_load
    def make_draft_group_details(self, data, **kwargs):
        return DraftGroupDetails(**data)


class ContestDetailsSchema(Schema):
    contest_id = fields.Integer(allow_none=True, required=True)
    draft_group_id = fields.Integer(allow_none=True, required=True)
    entries_details = fields.Nested(EntriesDetailsSchema, required=True)
    fantasy_player_points = fields.Number(allow_none=True, required=True)
    is_double_up = fields.Bool(allow_none=False, required=True)
    is_fifty_fifty = fields.Bool(allow_none=False, required=True)
    is_guaranteed = fields.Bool(allow_none=False, required=True)
    is_head_to_head = fields.Bool(allow_none=False, required=True)
    is_starred = fields.Bool(allow_none=False, required=True)
    name = fields.Str(allow_none=True, required=True)
    payout = fields.Number(allow_none=True, required=True)
    sport = EnumField(Sport, by_value=True, allow_none=True, required=True)
    starts_at = CustomDateTime(allow_none=True, required=True)

    @post_load
    def make_contest_details(self, data, **kwargs):
        return ContestDetails(**data)


class ContestsDetailsSchema(Schema):
    contests = fields.List(fields.Nested(ContestDetailsSchema, required=True), required=True)
    draft_groups = fields.List(fields.Nested(DraftGroupDetailsSchema, required=True), required=True)

    @post_load
    def make_contests_details(self, data, **kwargs):
        return ContestsDetails(**data)

# pylint: enable=unused-argument, no-self-use
