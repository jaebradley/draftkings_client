from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from draft_kings.data import Sport


@dataclass(frozen=True)
class PlayerNameDetails:
    display: Optional[str]
    first: Optional[str]
    last: Optional[str]
    short: Optional[str]


@dataclass(frozen=True)
class PlayerImageDetails:
    fifty_pixels_by_fifty_pixels_url: Optional[str]
    one_hundred_and_sixty_pixels_by_one_hundred_pixels_url: Optional[str]


@dataclass(frozen=True)
class PlayerCompetitionDetails:
    competition_id: Optional[int]
    name: Optional[str]
    starts_at: Optional[datetime]


@dataclass(frozen=True)
class PlayerTeamDetails:
    abbreviation: Optional[str]
    team_id: Optional[int]


@dataclass(frozen=True)
class Player:
    competition: Optional[PlayerCompetitionDetails]
    draftable_id: Optional[int]
    draft_alerts: List[str]
    image_details: Optional[PlayerImageDetails]
    is_disabled: Optional[bool]
    is_swappable: Optional[bool]
    name_details: Optional[PlayerNameDetails]
    news_status: Optional[str]
    player_id: Optional[int]
    position: Optional[str]
    roster_slot_id: Optional[int]
    salary: Optional[float]
    team_details: Optional[PlayerTeamDetails]


@dataclass(frozen=True)
class CompetitionTeam:
    abbreviation: Optional[str]
    city: Optional[str]
    name: Optional[str]
    team_id: Optional[int]


@dataclass(frozen=True)
class CompetitionWeather:
    description: Optional[str]
    is_in_a_dome: Optional[bool]


@dataclass(frozen=True)
class Competition:
    are_depth_charts_available: Optional[bool]
    are_starting_lineups_available: Optional[bool]
    away_team: Optional[CompetitionTeam]
    competition_id: Optional[int]
    home_team: Optional[CompetitionTeam]
    name: Optional[str]
    sport: Optional[Sport]
    starts_at: Optional[str]
    state: Optional[str]
    venue: Optional[str]
    weather: Optional[CompetitionWeather]


@dataclass(frozen=True)
class Draftables:
    competitions: List[Competition]
    players: List[Player]
