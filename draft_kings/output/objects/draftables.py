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
    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url: Optional[str]


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
class PlayerDraftAlertDetails:
    alert_description: Optional[str]
    message: Optional[str]
    priority_value: Optional[int]
    updated_at: Optional[datetime]


@dataclass(frozen=True)
class PlayerDetails:
    competition_details: Optional[PlayerCompetitionDetails]
    draftable_id: Optional[int]
    draft_alerts: List[PlayerDraftAlertDetails]
    image_details: PlayerImageDetails
    is_disabled: Optional[bool]
    is_swappable: Optional[bool]
    name_details: PlayerNameDetails
    news_status_description: Optional[str]
    player_id: Optional[int]
    position_name: Optional[str]
    roster_slot_id: Optional[int]
    salary: Optional[float]
    team_details: PlayerTeamDetails


@dataclass(frozen=True)
class CompetitionTeamDetails:
    abbreviation: Optional[str]
    city: Optional[str]
    name: Optional[str]
    team_id: Optional[int]


@dataclass(frozen=True)
class CompetitionWeatherDetails:
    description: Optional[str]
    is_in_a_dome: Optional[bool]


@dataclass(frozen=True)
class CompetitionDetails:
    are_depth_charts_available: Optional[bool]
    are_starting_lineups_available: Optional[bool]
    away_team: Optional[CompetitionTeamDetails]
    competition_id: Optional[int]
    home_team: Optional[CompetitionTeamDetails]
    name: Optional[str]
    sport: Optional[Sport]
    starts_at: Optional[datetime]
    state_description: Optional[str]
    venue: Optional[str]
    weather: Optional[CompetitionWeatherDetails]


@dataclass(frozen=True)
class DraftablesDetails:
    competitions: List[CompetitionDetails]
    players: List[PlayerDetails]
