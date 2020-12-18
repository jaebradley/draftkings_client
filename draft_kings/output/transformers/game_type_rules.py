from typing import Callable

from draft_kings.response.objects.game_type_rules import SalaryCap as ResponseSalaryCap, RosterSlot as \
    ResponseRosterSlot, LineupTemplate as ResponseLineupTemplate, GameTypeRules as ResponseGameTypeRules
from draft_kings.output.objects.game_type_rules import SalaryCapDetails, RosterSlotDetails, LineupTemplateDetails, \
    GameTypeRulesDetails


def transform_salary_cap(salary_cap: ResponseSalaryCap) -> SalaryCapDetails:
    return SalaryCapDetails(
        is_enabled=salary_cap.is_enabled,
        maximum_value=salary_cap.max_value,
        minimum_value=salary_cap.min_value
    )


def transform_roster_slot(roster_slot: ResponseRosterSlot) -> RosterSlotDetails:
    return RosterSlotDetails(
        description=roster_slot.description,
        name=roster_slot.name,
        roster_slot_id=roster_slot.roster_slot_id
    )


class LineupTemplateTransformer:
    def __init__(self, roster_slot_transformer: Callable[[ResponseRosterSlot], RosterSlotDetails]):
        self.roster_slot_transformer = roster_slot_transformer

    def transform(self, lineup_template: ResponseLineupTemplate) -> LineupTemplateDetails:
        return LineupTemplateDetails(
            roster_slot_details=self.roster_slot_transformer(lineup_template.roster_slot) if
            lineup_template.roster_slot is not None else None
        )


class GameTypeRulesTransformer:
    def __init__(self, salary_cap_transformer: Callable[[ResponseSalaryCap], SalaryCapDetails],
                 lineup_template_transformer: LineupTemplateTransformer):
        self.salary_cap__transformer = salary_cap_transformer
        self.lineup_template_transformer = lineup_template_transformer

    def transform(self, game_type_rules: ResponseGameTypeRules) -> GameTypeRulesDetails:
        return GameTypeRulesDetails(
            allow_late_swaps=game_type_rules.allow_late_swap,
            description=game_type_rules.description,
            enforce_selecting_unique_players=game_type_rules.unique_players,
            draft_type_name=game_type_rules.draft_type,
            game_type_id=game_type_rules.game_type_id,
            lineup_templates=list(map(
                lambda template:
                self.lineup_template_transformer.transform(lineup_template=template),
                game_type_rules.lineup_template
            )),
            name=game_type_rules.name,
            salary_cap_details=self.salary_cap__transformer(game_type_rules.salary_cap)
            if game_type_rules.salary_cap is not None else None
        )
