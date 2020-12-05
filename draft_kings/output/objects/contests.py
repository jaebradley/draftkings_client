from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from draft_kings.data import Sport


@dataclass(frozen=True)
class DraftGroupDetails:
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
class ContestDetails:
    contest_id: Optional[int]
    draft_group_id: Optional[int]
    entries_details: EntriesDetails
    fantasy_player_points: Optional[float]
    is_double_up: bool
    is_fifty_fifty: bool
    is_guaranteed: bool
    is_head_to_head: bool
    is_starred: bool
    name: Optional[str]
    payout: Optional[float]
    sport: Optional[Sport]
    starts_at: Optional[datetime]


@dataclass(frozen=True)
class ContestsDetails:
    contests: List[ContestDetails]
    draft_groups: List[DraftGroupDetails]
