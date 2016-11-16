class AvailablePlayer:
    def __init__(self, player_id, team_series_id, first_name, last_name, jersey_number, position,
                 draft_group_start_timestamp, team_id, match_up,
                 is_disabled_from_drafting, exceptional_messages, salary,
                 draftkings_points_per_contest, opposition_rank):
        self.player_id = player_id
        self.team_series_id = team_series_id
        self.position = position
        self.jersey_number = jersey_number
        self.last_name = last_name
        self.first_name = first_name
        self.draft_group_start_timestamp = draft_group_start_timestamp
        self.team_id = team_id
        self.match_up = match_up
        self.is_disabled_from_drafting = is_disabled_from_drafting
        self.exceptional_messages = exceptional_messages
        self.salary = salary
        self.draftkings_points_per_game = draftkings_points_per_contest
        self.opposition_rank = opposition_rank


class AvailablePlayerPosition:
    def __init__(self, position_id, position_name):
        self.position_id = position_id
        self.position_name = position_name