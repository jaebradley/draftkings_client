from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from draft_kings.data import Sport


@dataclass(frozen=True)
class DraftGroup:
    contest_type_id: Optional[int]
    draft_group_id: Optional[int]
    games_count: Optional[int]
    series_id: Optional[int]
    sport: Optional[Sport]
    starts_at: Optional[datetime]


@dataclass(frozen=True)
class EntriesDetails:
    fee: Optional[float]
    maximum: Optional[int]
    total: Optional[int]


@dataclass(frozen=True)
class Contest:
    contest_id: Optional[int]
    draft_group_id: Optional[int]
    entries_details: EntriesDetails
    fantasy_player_points: Optional[float]
    is_double_up: Optional[bool]
    is_fifty_fifty: Optional[bool]
    is_guaranteed: Optional[bool]
    is_head_to_head: Optional[bool]
    is_starred: Optional[bool]
    name: Optional[str]
    payout: Optional[float]
    sport: Optional[Sport]
    starts_at: Optional[datetime]


@dataclass(frozen=True)
class ContestsDetails:
    contests: List[Contest]
    draft_groups: List[DraftGroup]
