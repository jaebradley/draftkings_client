from dataclasses import dataclass
from typing import Optional, Dict, List


@dataclass(frozen=True)
class TeamSeries:
    away_team_id: Optional[int]
    home_team_id: Optional[int]
    starts_at: Optional[str]
    status: Optional[str]
    weather: Optional[str]


@dataclass(frozen=True)
class ExceptionalMessageType:
    name: Optional[str]


@dataclass(frozen=True)
class ExceptionalMessage:
    message: Optional[str]
    message_type: Optional[ExceptionalMessageType]
    priority: Optional[int]


@dataclass(frozen=True)
class Player:
    away_team_id: Optional[int]
    draft_group_start_time: Optional[int]
    exceptional_messages: List[ExceptionalMessage]
    first_name: Optional[str]
    home_team_id: Optional[int]
    is_disabled_from_drafting: Optional[bool]
    jersey_number: Optional[int]
    last_name: Optional[str]
    opposition_rank: Optional[int]
    player_id: Optional[int]
    position_id: Optional[int]
    position_name: Optional[str]
    points_per_game: Optional[str]
    salary: Optional[float]
    team_id: Optional[int]
    team_series_id: Optional[int]


@dataclass(frozen=True)
class PlayersDetails:
    players: List[Player]
    team_series: Dict[str, TeamSeries]
