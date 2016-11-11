class Contest:
    def __init__(self, contest_id, start_timestamp, fantasy_player_points, sport, name, guaranteed, starred,
                 total_entries, maximum_entries, entry_fee, total_payout, payout_distribution):
        self.contest_id = contest_id
        self.start_timestamp = start_timestamp
        self.fantasy_player_points = fantasy_player_points
        self.sport = sport
        self.name = name
        self.guaranteed = guaranteed
        self.starred = starred
        self.total_entries = total_entries
        self.maximum_entries = maximum_entries
        self.entry_fee = entry_fee
        self.total_payout = total_payout
        self.payout_distribution = payout_distribution