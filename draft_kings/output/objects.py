from datetime import datetime
from typing import Optional, List

from draft_kings.data import Sport


class ContestDraftGroup:
    def __init__(self, draft_group_id: Optional[int], series_id: Optional[int], contest_type_id: Optional[int],
                 sport: Optional[Sport], starts_at: Optional[datetime], games_count: Optional[int]) -> None:
        self.draft_group_id = draft_group_id
        self.series_id = series_id
        self.contest_type_id = contest_type_id
        self.sport = sport
        self.starts_at = starts_at
        self.games_count = games_count


class ContestEntryDetails:
    def __init__(self, maximum: Optional[float], fee: Optional[float], total: Optional[float]) -> None:
        self.maximum = maximum
        self.fee = fee
        self.total = total


class Contest:
    def __init__(self, contest_id: Optional[int], draft_group_id: Optional[int], entry_details: ContestEntryDetails,
                 fantasy_player_points: Optional[float], is_double_up: Optional[bool], is_fifty_fifty: Optional[bool],
                 is_guaranteed: Optional[bool], is_head_to_head: Optional[bool], is_starred: Optional[bool],
                 name: Optional[str], payout: Optional[float], sport: Optional[Sport],
                 starts_at: Optional[datetime]) -> None:
        self.contest_id = contest_id
        self.draft_group_id = draft_group_id
        self.entry_details = entry_details
        self.fantasy_player_points = fantasy_player_points
        self.is_double_up = is_double_up
        self.is_fifty_fifty = is_fifty_fifty
        self.is_guaranteed = is_guaranteed
        self.is_head_to_head = is_head_to_head
        self.is_starred = is_starred
        self.name = name
        self.payout = payout
        self.sport = sport
        self.starts_at = starts_at


class ContestsDetails:
    def __init__(self, contests: List[Contest], groups: List[ContestDraftGroup]) -> None:
        self.contests = contests
        self.groups = groups
