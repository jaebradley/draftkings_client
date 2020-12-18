from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class SalaryCapDetails:
    is_enabled: Optional[bool]
    maximum_value: Optional[float]
    minimum_value: Optional[float]


@dataclass(frozen=True)
class RosterSlotDetails:
    description: Optional[str]
    name: Optional[str]
    roster_slot_id: Optional[int]


@dataclass(frozen=True)
class LineupTemplateDetails:
    roster_slot_details: Optional[RosterSlotDetails]


@dataclass(frozen=True)
class GameTypeRulesDetails:
    allow_late_swaps: Optional[bool]
    description: Optional[str]
    enforce_selecting_unique_players: Optional[bool]
    draft_type_name: Optional[str]
    game_type_id: Optional[int]
    lineup_templates: List[LineupTemplateDetails]
    name: Optional[str]
    salary_cap_details: Optional[SalaryCapDetails]
