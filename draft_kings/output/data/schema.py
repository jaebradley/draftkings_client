from marshmallow import Schema, fields, post_dump
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.output.data.objects import ContestDraftGroup


class ContestEntryDetailsSchema(Schema):
    maximum = fields.Number()
    fee = fields.Number()
    total = fields.Number()


class ContestDraftGroupSchema(Schema):
    draft_group_id = fields.Integer()
    series_id = fields.Integer()
    contest_type_id = fields.Integer()
    sport = EnumField(Sport)
    starts_at = fields.Str()
    games_count = fields.Integer()

    @post_dump
    def make_contest_draft_group(self, data, many, **kwargs):
        return ContestDraftGroup(**data)


class ContestSchema(Schema):
    id = fields.Integer()
    double_up = fields.Bool()
    draft_group_id = fields.Integer()
    entries = fields.Nested(ContestEntryDetailsSchema())
    fantasy_player_points = fields.Number()
    fifty_fifty = fields.Bool()
    guaranteed = fields.Bool()
    head_to_head = fields.Bool()
    name = fields.Str()
    payout = fields.Number()
    sport = EnumField(Sport)
    starred = fields.Bool()
    starts_at = fields.DateTime()


class ContestsDetailsSchema(Schema):
    contests = fields.List(fields.Nested(ContestSchema()))
    groups = fields.List(fields.Nested(ContestDraftGroupSchema()))
