class PlayerTeamSeries:
    def __init__(self, away_team_id, home_team_id, starts_at, status_id, weather):
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.starts_at = starts_at
        self.status_id = status_id
        self.weather = weather

    def __eq__(self, other):
        if type(other) is type(self):
            return self.away_team_id == other.away_team_id \
                and self.home_team_id == other.home_team_id \
                and self.starts_at == other.starts_at \
                and self.status_id == other.status_id \
                and self.weather == other.weather

        return False


class PlayerDetail:
    def __init__(self, away_team_id, draft_group_start_time, exceptional_messages, first_name, home_team_id, is_disabled_from_drafting,
                 jersey_number, last_name, opposition_rank, player_id, position_id, position_name, points_per_game,
                 salary, team_id, team_series_id):
        self.away_team_id = away_team_id
        self.draft_group_start_time = draft_group_start_time
        self.exceptional_messages = exceptional_messages
        self.first_name = first_name
        self.home_team_id = home_team_id
        self.is_disabled_from_drafting = is_disabled_from_drafting
        self.jersey_number = jersey_number
        self.last_name = last_name
        self.opposition_rank = opposition_rank
        self.player_id = player_id
        self.position_id = position_id
        self.position_name = position_name
        self.points_per_game = points_per_game
        self.salary = salary
        self.team_id = team_id
        self.team_series_id = team_series_id

    def __eq__(self, other):
        if type(other) is type(self):
            return self.away_team_id == other.away_team_id \
                and self.draft_group_start_time == other.draft_group_start_time \
                and self.exceptional_messages == other.exceptional_messages \
                and self.first_name == other.first_name \
                and self.home_team_id == other.home_team_id \
                and self.is_disabled_from_drafting == other.is_disabled_from_drafting \
                and self.jersey_number == other.jersey_number \
                and self.last_name == other.last_name \
                and self.opposition_rank == other.opposition_rank \
                and self.player_id == other.player_id \
                and self.position_id == other.position_id \
                and self.position_name == other.position_name \
                and self.points_per_game == other.points_per_game \
                and self.salary == other.salary \
                and self.team_id == other.team_id \
                and self.team_series_id == other.team_series_id

        return False


class PlayersDetails:
    def __init__(self, players, team_series):
        self.players = players
        self.team_series = team_series

    def __eq__(self, other):
        if type(other) is type(self):
            return self.players == other.players \
                and self.team_series == other.team_series

        return False
