class DraftGroupPlayer:
    def __init__(self, player_id, first_name, last_name, jersey_number, position,
                 draft_group_start_timestamp, team_id, home_team, away_team,
                 is_disabled_from_drafting, exceptional_messages, salary,
                 draftkings_points_per_contest, opposition_rank):
        self.player_id = player_id
        self.position = position
        self.jersey_number = jersey_number
        self.last_name = last_name
        self.first_name = first_name
        self.draft_group_start_timestamp = draft_group_start_timestamp
        self.team_id = team_id
        self.home_team = home_team
        self.away_team = away_team
        self.is_disabled_from_drafting = is_disabled_from_drafting
        self.exceptional_messages = exceptional_messages
        self.salary = salary
        self.draftkings_points_per_game = draftkings_points_per_contest
        self.opposition_rank = opposition_rank


class DraftGroupPlayerPosition:
    def __init__(self, position_id, position_name):
        self.position_id = position_id
        self.position_name = position_name


class DraftGroupPlayerGame:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team


class DraftGroupPlayerGameTeam:
    def __init__(self, team_id, team_abbreviation):
        self.team_id = team_id
        self.team_abbreviation = team_abbreviation