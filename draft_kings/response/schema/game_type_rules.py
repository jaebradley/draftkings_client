# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, EXCLUDE, post_load

from draft_kings.response.objects.game_type_rules import SalaryCap, RosterSlot, LineupTemplate, GameTypeRules


class SalaryCapSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    isEnabled = fields.Bool(attribute="is_enabled", missing=None)
    maxValue = fields.Float(attribute="max_value", missing=None)
    minValue = fields.Float(attribute="min_value", missing=None)

    @post_load
    def make_salary_cap(self, data, **kwargs):
        return SalaryCap(**data)


class RosterSlotSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int(attribute="roster_slot_id", missing=None)
    description = fields.Str(attribute="description", missing=None)
    name = fields.Str(attribute="name", missing=None)

    @post_load
    def make_roster_slot(self, data, **kwargs):
        return RosterSlot(**data)


class LineupTemplateSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    rosterSlot = fields.Nested(RosterSlotSchema, attribute="roster_slot", missing=None)

    @post_load
    def make_lineup_template(self, data, **kwargs):
        return LineupTemplate(**data)


class GameTypeRulesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    allowLateSwap = fields.Bool(attribute="allow_late_swap", missing=None)
    draftType = fields.Str(attribute="draft_type", missing=None)
    gameTypeDescription = fields.Str(attribute="description", missing=None)
    gameTypeId = fields.Int(attribute="game_type_id", missing=None)
    gameTypeName = fields.Str(attribute="name", missing=None)
    lineupTemplate = fields.List(fields.Nested(LineupTemplateSchema), attribute="lineup_template", missing=[])
    salaryCap = fields.Nested(SalaryCapSchema, attribute="salary_cap", missing=None)
    uniquePlayers = fields.Bool(attribute="unique_players", missing=None)

    @post_load
    def make_game_type_rules(self, data, **kwargs):
        return GameTypeRules(**data)

# pylint: enable=unused-argument, no-self-use
