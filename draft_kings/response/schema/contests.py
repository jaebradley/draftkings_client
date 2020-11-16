from marshmallow import Schema, fields, EXCLUDE, post_load

from draft_kings.response.objects.contests import ContestTypeAttributes, Contest, DraftGroup, Contests


class ContestAttributeSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    IsDoubleUp = fields.Bool(missing=None, attribute="is_double_up")
    IsFiftyFifty = fields.Bool(missing=None, attribute="is_fifty_fifty")
    IsGuaranteed = fields.Bool(missing=None, attribute="is_guaranteed")
    IsH2h = fields.Bool(missing=None, attribute="is_h2h")
    IsStarred = fields.Bool(missing=None, attribute="is_starred")

    @post_load
    def make_contest_attribute(self, data, **kwargs):
        return ContestTypeAttributes(**data)


class ContestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(missing=None, attribute="contest_id")
    dg = fields.Integer(missing=None, attribute="draft_group_id")
    m = fields.Number(missing=None, attribute="entry_maximum")
    a = fields.Number(missing=None, attribute="entry_fee")
    nt = fields.Number(missing=None, attribute="entry_total")
    fpp = fields.Number(missing=None, attribute="fantasy_player_points")
    n = fields.Str(missing=None, attribute="name")
    po = fields.Number(missing=None, attribute="payout")
    s = fields.Integer(missing=None, attribute="sport_id")
    sd = fields.Str(missing=None, attribute="starts_at")
    attr = fields.Nested(ContestAttributeSchema(), missing={}, attribute="attributes")

    @post_load
    def make_contest(self, data, **kwargs):
        return Contest(**data)


class DraftGroupSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    DraftGroupId = fields.Integer(missing=None, attribute="draft_group_id")
    DraftGroupSeriesId = fields.Integer(missing=None, attribute="draft_group_series_id")
    ContestTypeId = fields.Integer(missing=None, attribute="contest_type_id")
    Sport = fields.Str(missing=None, attribute="sport")
    StartDate = fields.AwareDateTime(missing=None, attribute="start_date")
    GameCount = fields.Integer(missing=None, attribute="game_count")

    @post_load
    def make_draft_group(self, data, **kwargs):
        return DraftGroup(**data)


class ContestsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    Contests = fields.List(fields.Nested(ContestSchema(), missing={}), missing=[], attribute="contests")
    DraftGroups = fields.List(fields.Nested(DraftGroupSchema(), missing={}), missing=[], attribute="draft_groups")

    @post_load
    def make_contests(self, data, **kwargs):
        return Contests(**data)
