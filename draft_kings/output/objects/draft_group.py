from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from draft_kings.data import Sport


@dataclass(frozen=True)
class ContestDetails:
    game_type_description: Optional[str]
    type_id: Optional[int]


@dataclass(frozen=True)
class StartTimeDetails:
    maximum: Optional[datetime]
    minimum: Optional[datetime]
    type_description: Optional[str]


@dataclass(frozen=True)
class LeagueDetails:
    abbreviation: Optional[str]
    league_id: Optional[int]
    name: Optional[str]


@dataclass(frozen=True)
class GameDetails:
    away_team_id: Optional[int]
    description: Optional[str]
    game_id: Optional[int]
    home_team_id: Optional[int]
    location: Optional[str]
    name: Optional[str]
    starts_at: Optional[datetime]
    status_description: Optional[str]


@dataclass(frozen=True)
class DraftGroupDetails:
    contest_details: ContestDetails
    draft_group_id: Optional[int]
    games: List[GameDetails]
    leagues: List[LeagueDetails]
    sport: Optional[Sport]
    start_time_details: StartTimeDetails
    state_description: Optional[str]
