from datetime import datetime
from typing import Optional, List

from draft_kings.data import Sport


class PlayerNameDetails:
    def __init__(self, display, first, last, short):
        self.display = display
        self.first = first
        self.last = last
        self.short = short

    def __eq__(self, other):
        if type(self) is type(other):
            return self.display == other.display \
                   and self.first == other.first \
                   and self.last == other.last \
                   and self.short == other.short

        return False


class PlayerImageDetails:
    def __init__(self, unresized_url: Optional[str], fifty_pixels_by_fifty_pixels_url: Optional[str],
                 sixty_five_pixels_by_sixty_five_pixels_url: Optional[str],
                 one_hundred_and_sixty_pixels_by_one_hundred_pixels_url: Optional[str]) -> None:
        self.unresized_url = unresized_url
        self.fifty_pixels_by_fifty_pixels_url = fifty_pixels_by_fifty_pixels_url
        self.sixty_five_pixels_by_sixty_five_pixels_url = sixty_five_pixels_by_sixty_five_pixels_url
        self.one_hundred_and_sixty_pixels_by_one_hundred_pixels_url = one_hundred_and_sixty_pixels_by_one_hundred_pixels_url

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.unresized_url == other.unresized_url \
                   and self.fifty_pixels_by_fifty_pixels_url == other.fifty_pixels_by_fifty_pixels_url \
                   and self.sixty_five_pixels_by_sixty_five_pixels_url == other.sixty_five_pixels_by_sixty_five_pixels_url \
                   and self.one_hundred_and_sixty_pixels_by_one_hundred_pixels_url == other.one_hundred_and_sixty_pixels_by_one_hundred_pixels_url

        return False


class PlayerCompetitionDetails:
    def __init__(self, competition_id: Optional[int], name: Optional[str], starts_at: Optional[datetime]) -> None:
        self.competition_id = competition_id
        self.name = name
        self.starts_at = starts_at

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.competition_id == other.competition_id \
                   and self.name == other.name \
                   and self.starts_at == other.starts_at

        return False


class PlayerTeamDetails:
    def __init__(self, abbreviation: Optional[str], team_id: Optional[int]) -> None:
        self.abbreviation = abbreviation
        self.team_id = team_id

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.abbreviation == other.abbreviation \
                   and self.team_id == other.team_id

        return False


class Player:
    def __init__(self, competition: PlayerCompetitionDetails, draftable_id: Optional[int], draft_alerts: List[str],
                 image_details: PlayerImageDetails, is_disabled: Optional[bool], is_swappable: Optional[bool],
                 name_details: PlayerNameDetails, news_status: Optional[str], player_id: Optional[int],
                 position: Optional[str], roster_slot_id: Optional[int], salary: Optional[float],
                 team_details: PlayerTeamDetails) -> None:
        self.competition = competition
        self.draftable_id = draftable_id
        self.draft_alerts = draft_alerts
        self.image_details = image_details
        self.is_disabled = is_disabled
        self.is_swappable = is_swappable
        self.name_details = name_details
        self.news_status = news_status
        self.player_id = player_id
        self.position = position
        self.roster_slot_id = roster_slot_id
        self.salary = salary
        self.team_details = team_details

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.competition == other.competition \
                   and self.draftable_id == other.draftable_id \
                   and self.draft_alerts == other.draft_alerts \
                   and self.image_details == other.image_details \
                   and self.is_disabled == other.is_disabled \
                   and self.is_swappable == other.is_swappable \
                   and self.name_details == other.name_details \
                   and self.news_status == other.news_status \
                   and self.player_id == other.player_id \
                   and self.position == other.position \
                   and self.roster_slot_id == other.roster_slot_id \
                   and self.salary == other.salary \
                   and self.team_details == other.team_details

        return False


class CompetitionTeam:
    def __init__(self, abbreviation: Optional[str], city: Optional[str], name: Optional[str], team_id: Optional[int]) -> None:
        self.abbreviation = abbreviation
        self.city = city
        self.name = name
        self.team_id = team_id

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.abbreviation == other.abbreviation \
                   and self.city == other.city \
                   and self.name == other.name \
                   and self.team_id == other.team_id

        return False


class CompetitionWeather:
    def __init__(self, description: Optional[str], is_in_a_dome: Optional[bool]) -> None:
        self.description = description
        self.is_in_a_dome = is_in_a_dome

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.description == other.icon \
                   and self.is_in_a_dome == other.is_dome

        return False


class Competition:
    def __init__(self, are_depth_charts_available: Optional[bool], are_starting_lineups_available: Optional[bool],
                 away_team: CompetitionTeam, competition_id: Optional[int], home_team: CompetitionTeam,
                 name: Optional[str], sport: Optional[Sport], starts_at: Optional[str], state: Optional[str],
                 venue: Optional[str], weather: CompetitionWeather) -> None:
        self.are_depth_charts_available = are_depth_charts_available
        self.are_starting_lineups_available = are_starting_lineups_available
        self.away_team = away_team
        self.competition_id = competition_id
        self.home_team = home_team
        self.name = name
        self.sport = sport
        self.starts_at = starts_at
        self.state = state
        self.venue = venue
        self.weather = weather

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.are_depth_charts_available == other.are_depth_charts_available \
                   and self.are_starting_lineups_available == other.are_starting_lineups_available \
                   and self.away_team == other.away_team \
                   and self.competition_id == other.competition_id \
                   and self.home_team == other.home_team \
                   and self.name == other.name \
                   and self.sport == other.sport \
                   and self.starts_at == other.start_time \
                   and self.state == other.state \
                   and self.venue == other.venue \
                   and self.weather == other.weather

        return False


class Draftables:
    def __init__(self, competitions: List[Competition], players: List[Player]) -> None:
        self.competitions = competitions
        self.players = players

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.competitions == other.competitions \
                   and self.players == other.players

        return False
