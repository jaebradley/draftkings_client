class Contest:
    def __init__(self, contest_id, start_timestamp, fantasy_player_points, sport, name, is_guaranteed, is_starred,
                 is_head_to_head, is_double_up, is_fifty_fifty, total_entries, maximum_entries, entry_fee, total_payout):
        self.contest_id = contest_id
        self.start_timestamp = start_timestamp
        self.fantasy_player_points = fantasy_player_points
        self.sport = sport
        self.name = name
        self.is_guaranteed = is_guaranteed
        self.is_starred = is_starred
        self.is_head_to_head = is_head_to_head
        self.is_double_up = is_double_up
        self.is_fifty_fifty = is_fifty_fifty
        self.total_entries = total_entries
        self.maximum_entries = maximum_entries
        self.entry_fee = entry_fee
        self.total_payout = total_payout
