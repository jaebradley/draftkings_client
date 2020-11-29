from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass(frozen=True)
class ContestAttributes:
    is_double_up: Optional[bool]
    is_fifty_fifty: Optional[bool]
    is_guaranteed: Optional[bool]
    is_h2h: Optional[bool]
    is_starred: Optional[bool]


@dataclass(frozen=True)
class Contest:
    attributes: Optional[ContestAttributes]
    contest_id: Optional[int]
    draft_group_id: Optional[int]
    entry_fee: Optional[float]
    entry_maximum: Optional[int]
    entry_total: Optional[int]
    fantasy_player_points: Optional[float]
    name: Optional[str]
    payout: Optional[float]
    sport_id: Optional[int]
    starts_at: Optional[str]


@dataclass(frozen=True)
class DraftGroup:
    draft_group_id: Optional[int]
    draft_group_series_id: Optional[int]
    contest_type_id: Optional[int]
    game_count: Optional[int]
    sport: Optional[str]
    start_date: Optional[datetime]


@dataclass(frozen=True)
class Contests:
    contests: List[Contest]
    draft_groups: List[DraftGroup]
