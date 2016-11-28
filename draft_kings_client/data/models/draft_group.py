class DraftGroup:
    def __init__(self, id, draft_group_series_id, contest_type_id, start_datetime, sport, game_count):
        self.id = id
        self.draft_group_series_id = draft_group_series_id
        self.contest_type_id = contest_type_id
        self.start_datetime = start_datetime
        self.sport = sport
        self.game_count = game_count
