from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass(frozen=True)
class ContestType:
    contest_type_id: Optional[int]
    game_type: Optional[str]


@dataclass(frozen=True)
class League:
    league_abbreviation: Optional[str]
    league_id: Optional[int]
    league_name: Optional[str]


@dataclass(frozen=True)
class Game:
    away_team_id: Optional[int]
    description: Optional[str]
    game_id: Optional[int]
    home_team_id: Optional[int]
    location: Optional[str]
    name: Optional[str]
    start_date: Optional[datetime]
    status: Optional[str]


@dataclass(frozen=True)
class DraftGroup:
    contest_type: ContestType
    draft_group_id: Optional[int]
    draft_group_state: Optional[str]
    games: List[Game]
    leagues: List[League]
    max_start_time: Optional[datetime]
    min_start_time: Optional[datetime]
    sport_id: Optional[int]
    start_time_type: Optional[str]


@dataclass(frozen=True)
class DraftGroupResponse:
    draft_group: DraftGroup
