class ContestDraftGroup:
    def __init__(self, draft_group_id, series_id, contest_type_id, sport, starts_at, games_count):
        self.draft_group_id = draft_group_id
        self.series_id = series_id
        self.contest_type_id = contest_type_id
        self.sport = sport
        self.starts_at = starts_at
        self.games_count = games_count


class ContestEntryDetails:
    def __init__(self, maximum, fee, total):
        self.maximum = maximum
        self.fee = fee
        self.total = total


class Contest:
    def __init__(self, contest_id, draft_group_id, entry_details, fantasy_player_points, is_double_up, is_fifty_fifty, is_guaranteed, is_head_to_head, is_starred, name, payout, sport, starts_at):
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
    def __init__(self, contests, groups):
        self.contests = contests
        self.groups = groups
