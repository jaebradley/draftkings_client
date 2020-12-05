from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass(frozen=True)
class PlayerCompetitionDetails:
    competition_id: Optional[int]
    name: Optional[str]
    start_time: Optional[datetime]


@dataclass(frozen=True)
class DraftAlert:
    alert_type: Optional[str]
    message: Optional[str]
    priority: Optional[int]
    updated_date: Optional[datetime]


@dataclass(frozen=True)
class Player:
    competition: Optional[PlayerCompetitionDetails]
    display_name: Optional[str]
    draftable_id: Optional[int]
    draft_alerts: List[DraftAlert]
    first_name: Optional[str]
    is_disabled: Optional[bool]
    is_swappable: Optional[bool]
    last_name: Optional[str]
    news_status: Optional[str]
    player_id: Optional[int]
    player_image_50: Optional[str]
    player_image_160: Optional[str]
    position: Optional[str]
    roster_slot_id: Optional[int]
    salary: Optional[float]
    short_name: Optional[str]
    team_abbreviation: Optional[str]
    team_id: Optional[int]


@dataclass(frozen=True)
class CompetitionTeam:
    abbreviation: Optional[str]
    city: Optional[str]
    team_id: Optional[int]
    team_name: Optional[str]


@dataclass(frozen=True)
class CompetitionWeather:
    icon: Optional[str]
    is_dome: Optional[bool]


@dataclass(frozen=True)
class Competition:
    are_depth_charts_available: Optional[bool]
    are_starting_lineups_available: Optional[bool]
    away_team: Optional[CompetitionTeam]
    competition_id: Optional[int]
    competition_state: Optional[str]
    home_team: Optional[CompetitionTeam]
    name: Optional[str]
    sport: Optional[str]
    start_time: Optional[datetime]
    venue: Optional[str]
    weather: Optional[CompetitionWeather]


@dataclass(frozen=True)
class Draftables:
    competitions: List[Competition]
    draftables: List[Player]
