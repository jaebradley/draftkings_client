from typing import Optional, Dict, List


class TeamSeries:
    def __init__(self, away_team_id: Optional[int], home_team_id: Optional[int], starts_at: Optional[str],
                 status: Optional[str], weather: Optional[str]):
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.starts_at = starts_at
        self.status = status
        self.weather = weather

    def __eq__(self, other):
        if type(other) is type(self):
            return self.away_team_id == other.away_team_id \
                and self.home_team_id == other.home_team_id \
                and self.starts_at == other.starts_at \
                and self.status == other.status_id \
                and self.weather == other.weather

        return False


class PlayerDetails:
    def __init__(self, away_team_id: Optional[int], draft_group_start_time: Optional[int],
                 exceptional_messages: List[str], first_name: Optional[str], home_team_id: Optional[int],
                 is_disabled_from_drafting: Optional[bool], jersey_number: Optional[int], last_name: Optional[str],
                 opposition_rank: Optional[int], player_id: Optional[int], position_id: Optional[int],
                 position_name: Optional[str], points_per_game: Optional[str], salary: Optional[float],
                 team_id: Optional[int], team_series_id: Optional[int]):
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
    def __init__(self, players: List[PlayerDetails], team_series: Dict[str, TeamSeries]):
        self.players = players
        self.team_series = team_series

    def __eq__(self, other):
        if type(other) is type(self):
            return self.players == other.players \
                and self.team_series == other.team_series

        return False
