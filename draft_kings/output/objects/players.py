class TeamSeries:
    def __init__(self, away_team_id, home_team_id, starts_at, status, team_series_id, weather_description):
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.starts_at = starts_at
        self.status = status
        self.team_series_id = team_series_id
        self.weather_description = weather_description

    def __eq__(self, other):
        if type(other) is type(self):
            return self.away_team_id == other.away_team_id \
                   and self.home_team_id == other.home_team_id \
                   and self.starts_at == other.starts_at \
                   and self.status == other.status_id \
                   and self.team_series_id == other.team_series_id \
                   and self.weather_description == other.weather

        return False


class DraftDetails:
    def __init__(self, exceptional_messages, is_draftable, salary, starts_at):
        self.exceptional_messages = exceptional_messages
        self.is_draftable = is_draftable
        self.salary = salary
        self.starts_at = starts_at

    def __eq__(self, other):
        if type(other) is type(self):
            return self.exceptional_messages == other.exceptional_messages \
                and self.is_draftable == other.is_draftable \
                and self.salary == other.salary \
                and self.starts_at == other.starts_at

        return False


class PlayerTeamSeriesDetails:
    def __init__(self, away_team_id, home_team_id, opposition_rank, team_series_id):
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.opposition_rank = opposition_rank
        self.team_series_id = team_series_id

    def __eq__(self, other):
        if type(other) is type(self):
            return self.away_team_id == other.away_team_id \
                and self.home_team_id == other.home_team_id \
                and self.opposition_rank == other.opposition_rank \
                and self.team_series_id == other.team_series_id

        return False


class PlayerPosition:
    def __init__(self, name, position_id):
        self.name = name
        self.position_id = position_id

    def __eq__(self, other):
        if type(other) is type(self):
            return self.position_id == other.position_id \
                   and self.name == other.position_name

        return False


class Player:
    def __init__(self, draft_details, first_name, jersey_number, last_name, player_id, points_per_game, position,
                 team_id, team_series):
        self.draft_details = draft_details
        self.first_name = first_name
        self.jersey_number = jersey_number
        self.last_name = last_name
        self.player_id = player_id
        self.points_per_game = points_per_game
        self.position = position
        self.team_id = team_id
        self.team_series = team_series

    def __eq__(self, other):
        if type(other) is type(self):
            return self.draft_details == other.draft_details \
                and self.first_name == other.first_name \
                and self.jersey_number == other.jersey_number \
                and self.last_name == other.last_name \
                and self.player_id == other.player_id \
                and self.points_per_game == other.points_per_game \
                and self.position == other.position \
                and self.team_id == other.team_id  \
                and self.team_series == other.team_series

        return False


class PlayersDetails:
    def __init__(self, players, team_series):
        self.players = players
        self.team_series = team_series

    def __eq__(self, other):
        if type(other) is type(self):
            return self.players == other.players \
                and self.team_series == other.team_series
