from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class SalaryCap:
    is_enabled: Optional[bool]
    max_value: Optional[float]
    min_value: Optional[float]


@dataclass(frozen=True)
class RosterSlot:
    description: Optional[str]
    name: Optional[str]
    roster_slot_id: Optional[int]


@dataclass(frozen=True)
class LineupTemplate:
    roster_slot: Optional[RosterSlot]


@dataclass(frozen=True)
class GameTypeRules:
    allow_late_swap: Optional[bool]
    description: Optional[str]
    draft_type: Optional[str]
    game_type_id: Optional[int]
    lineup_template: List[LineupTemplate]
    name: Optional[str]
    salary_cap: Optional[SalaryCap]
    unique_players: Optional[bool]
