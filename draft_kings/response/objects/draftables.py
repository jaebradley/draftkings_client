from typing import Optional, List


class PlayerCompetitionDetails:
    def __init__(self, competition_id: Optional[int], name: Optional[str], start_time: Optional[str]) -> None:
        self.competition_id = competition_id
        self.name = name
        self.start_time = start_time

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.competition_id == other.competition_id \
                and self.name == other.name \
                and self.start_time == other.start_time

        return False


class Player:
    def __init__(self, competition: PlayerCompetitionDetails, display_name: Optional[str],
                 draftable_id: Optional[int], draft_alerts: List[str], first_name: Optional[str],
                 is_disabled: Optional[bool], is_swappable: Optional[bool], last_name: Optional[str],
                 news_status: Optional[str], player_id: Optional[int], player_image_full: Optional[str],
                 player_image_50: Optional[str], player_image_65: Optional[str], player_image_160: Optional[str],
                 position: Optional[str], roster_slot_id: Optional[int], salary: Optional[float],
                 short_name: Optional[str], team_id: Optional[int]) -> None:
        self.competition = competition
        self.display_name = display_name
        self.draftable_id = draftable_id
        self.draft_alerts = draft_alerts
        self.first_name = first_name
        self.is_disabled = is_disabled
        self.is_swappable = is_swappable
        self.last_name = last_name
        self.news_status = news_status
        self.player_id = player_id
        self.player_image_full = player_image_full
        self.player_image_50 = player_image_50
        self.player_image_65 = player_image_65
        self.player_image_160 = player_image_160
        self.position = position
        self.roster_slot_id = roster_slot_id
        self.salary = salary
        self.short_name = short_name
        self.team_id = team_id

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.competition == other.competition \
                and self.display_name == other.display_name \
                and self.draftable_id == other.draftable_id \
                and self.draft_alerts == other.draft_alerts \
                and self.first_name == other.first_name \
                and self.is_disabled == other.is_disabled \
                and self.is_swappable == other.is_swappable \
                and self.last_name == other.last_name \
                and self.news_status == other.news_status \
                and self.player_id == other.player_id \
                and self.player_image_full == other.player_image_full \
                and self.player_image_50 == other.player_image_50 \
                and self.player_image_65 == other.player_image_65 \
                and self.player_image_160 == other.player_image_160 \
                and self.position == other.position \
                and self.roster_slot_id == other.roster_slot_id \
                and self.salary == other.salary \
                and self.short_name == other.short_name \
                and self.team_id == other.team_id

        return False


class CompetitionTeam:
    def __init__(self, abbreviation: Optional[str], city: Optional[str], team_id: Optional[int],
                 team_name: Optional[str]) -> None:
        self.abbreviation = abbreviation
        self.city = city
        self.team_id = team_id
        self.team_name = team_name

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.abbreviation == other.abbreviation \
                and self.city == other.city \
                and self.team_id == other.team_id \
                and self.team_name == other.team_name

        return False


class CompetitionWeather:
    def __init__(self, icon: Optional[str], is_dome: Optional[bool]) -> None:
        self.icon = icon
        self.is_dome = is_dome

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.icon == other.icon \
                and self.is_dome == other.is_dome

        return False


class Competition:
    def __init__(self, are_depth_charts_available: Optional[bool], are_starting_lineups_available: Optional[bool],
                 away_team: CompetitionTeam, competition_id: Optional[int], competition_state: Optional[str],
                 home_team: CompetitionTeam, name: Optional[str], sport: Optional[str], start_time: Optional[str],
                 venue: Optional[str], weather: CompetitionWeather) -> None:
        self.are_depth_charts_available = are_depth_charts_available
        self.are_starting_lineups_available = are_starting_lineups_available
        self.away_team = away_team
        self.competition_id = competition_id
        self.competition_state = competition_state
        self.home_team = home_team
        self.name = name
        self.sport = sport
        self.start_time = start_time
        self.venue = venue
        self.weather = weather

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.are_depth_charts_available == other.are_depth_charts_available \
                and self.are_starting_lineups_available == other.are_starting_lineups_available \
                and self.away_team == other.away_team \
                and self.competition_id == other.competition_id \
                and self.competition_state == other.competition_state \
                and self.home_team == other.home_team \
                and self.name == other.name \
                and self.sport == other.sport \
                and self.start_time == other.start_time \
                and self.venue == other.venue \
                and self.weather == other.weather

        return False


class Draftables:
    def __init__(self, competitions: List[Competition], draftables: List[Player]):
        self.competitions = competitions
        self.draftables = draftables

    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self.competitions == other.competitions \
                and self.draftables == other.draftables

        return False
