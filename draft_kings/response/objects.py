from typing import Optional


class ContestAttribute:
    def __init__(self, is_double_up: Optional[bool], is_fifty_fifty: Optional[bool], is_guaranteed: Optional[bool], is_h2h: Optional[bool], is_starred: Optional[bool]):
        self.is_double_up = is_double_up
        self.is_fifty_fifty = is_fifty_fifty
        self.is_guaranteed = is_guaranteed
        self.is_h2h = is_h2h
        self.is_starred = is_starred


class Contest:
    def __init__(self, contest_id, draft_group_id, entry_maximum, entry_fee, entry_total, fantasy_player_points, name, payout, sport_id, starts_at, attributes):
        self.contest_id = contest_id
        self.draft_group_id = draft_group_id
        self.entry_maximum = entry_maximum
        self.entry_fee = entry_fee
        self.entry_total = entry_total
        self.fantasy_player_points = fantasy_player_points
        self.name = name
        self.payout = payout
        self.sport_id = sport_id
        self.starts_at = starts_at
        self.attributes = attributes


class DraftGroup:
    def __init__(self, draft_group_id, draft_group_series_id, contest_type_id, sport, start_date, game_count):
        self.draft_group_id = draft_group_id
        self.draft_group_series_id = draft_group_series_id
        self.contest_type_id = contest_type_id
        self.sport = sport
        self.start_date = start_date
        self.game_count = game_count


class Contests:
    def __init__(self, contests, draft_groups):
        self.contests = contests
        self.draft_groups = draft_groups
