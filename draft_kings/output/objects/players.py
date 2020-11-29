from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass(frozen=True)
class TeamSeriesDetails:
    away_team_id: Optional[int]
    home_team_id: Optional[int]
    starts_at: Optional[datetime]
    status_description: Optional[str]
    team_series_id: Optional[int]
    weather_description: Optional[str]


@dataclass(frozen=True)
class DraftDetails:
    is_draftable: Optional[bool]
    salary: Optional[float]
    starts_at: Optional[datetime]


@dataclass(frozen=True)
class PlayerTeamSeriesDetails:
    away_team_id: Optional[int]
    home_team_id: Optional[int]
    opposition_rank: Optional[int]
    team_series_id: Optional[int]


@dataclass(frozen=True)
class PositionDetails:
    name: Optional[str]
    position_id: Optional[int]


@dataclass(frozen=True)
class ExceptionalMessageTypeDetails:
    name: Optional[str]


@dataclass(frozen=True)
class ExceptionalMessageDetails:
    message: Optional[str]
    priority_value: Optional[int]
    type_details: Optional[ExceptionalMessageTypeDetails]


@dataclass(frozen=True)
class PlayerDetails:
    draft_details: DraftDetails
    exceptional_messages: List[ExceptionalMessageDetails]
    first_name: Optional[str]
    jersey_number: Optional[int]
    last_name: Optional[str]
    player_id: Optional[int]
    points_per_game: Optional[float]
    position_details: PositionDetails
    team_id: Optional[int]
    team_series_details: PlayerTeamSeriesDetails


@dataclass(frozen=True)
class PlayersDetails:
    players: List[PlayerDetails]
    team_series: List[TeamSeriesDetails]
