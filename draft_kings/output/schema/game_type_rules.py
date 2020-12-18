# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load

from draft_kings.output.objects.game_type_rules import SalaryCapDetails, RosterSlotDetails, LineupTemplateDetails, \
    GameTypeRulesDetails


class SalaryCapDetailsSchema(Schema):
    is_enabled = fields.Bool(allow_none=True, required=True)
    maximum_value = fields.Float(allow_none=True, required=True)
    minimum_value = fields.Float(allow_none=True, required=True)

    @post_load
    def make_salary_cap_details(self, data, **kwargs):
        return SalaryCapDetails(**data)


class RosterSlotDetailsSchema(Schema):
    description = fields.Str(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)
    roster_slot_id = fields.Int(allow_none=True, required=True)

    @post_load
    def make_roster_slot_details(self, data, **kwargs):
        return RosterSlotDetails(**data)


class LineupTemplateDetailsSchema(Schema):
    roster_slot_details = fields.Nested(RosterSlotDetailsSchema, allow_none=True, required=True)

    @post_load
    def make_lineup_template(self, data, **kwargs):
        return LineupTemplateDetails(**data)


class GameTypeRulesDetailsSchema(Schema):
    allow_late_swaps = fields.Bool(allow_none=True, required=True)
    description = fields.Str(allow_none=True, required=True)
    enforce_unique_players = fields.Bool(allow_none=True, required=True)
    draft_type_name = fields.Str(allow_none=True, required=True)
    game_type_id = fields.Int(allow_none=True, required=True)
    lineup_templates = fields.List(fields.Nested(LineupTemplateDetailsSchema, allow_none=False, required=True),
                                   allow_none=False, required=True)
    name = fields.Str(allow_none=True, required=True)
    salary_cap_details = fields.Nested(SalaryCapDetailsSchema, allow_none=True, required=True)

    @post_load
    def make_game_type_details(self, data, **kwargs):
        return GameTypeRulesDetails(**data)

# pylint: enable=unused-argument, no-self-use
