from typing import Callable

from draft_kings.data import CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS
from draft_kings.output.objects.draftables import PlayerNameDetails, PlayerImageDetails, PlayerCompetitionDetails, \
    PlayerTeamDetails, Player, CompetitionTeam, CompetitionWeather, Competition, Draftables
from draft_kings.response.objects.draftables import Player as ResponsePlayer, PlayerCompetitionDetails as \
    ResponsePlayerCompetitionDetails, CompetitionTeam as ResponseCompetitionTeam, CompetitionWeather as \
    ResponseCompetitionWeather, Competition as ResponseCompetition, Draftables as ResponseDraftables


def transform_player_name_details(player: ResponsePlayer) -> PlayerNameDetails:
    return PlayerNameDetails(
        display=player.display_name,
        first=player.first_name,
        last=player.last_name,
        short=player.short_name
    )


def transform_player_image_details(player: ResponsePlayer) -> PlayerImageDetails:
    return PlayerImageDetails(
        fifty_pixels_by_fifty_pixels_url=player.player_image_50,
        one_hundred_and_sixty_pixels_by_one_hundred_pixels_url=player.player_image_160
    )


def transform_player_competition_details(
        response_player_competition_details: ResponsePlayerCompetitionDetails) -> PlayerCompetitionDetails:
    return PlayerCompetitionDetails(
        competition_id=response_player_competition_details.competition_id,
        name=response_player_competition_details.name,
        starts_at=response_player_competition_details.start_time
    )


def transform_player_team_details(player: ResponsePlayer) -> PlayerTeamDetails:
    return PlayerTeamDetails(
        abbreviation=player.team_abbreviation,
        team_id=player.team_id
    )


class PlayerTransformer:
    def __init__(self, name_details_transformer: Callable[[ResponsePlayer], PlayerNameDetails],
                 image_details_transformer: Callable[[ResponsePlayer], PlayerImageDetails],
                 competition_details_transformer: Callable[
                     [ResponsePlayerCompetitionDetails], PlayerCompetitionDetails
                 ],
                 team_details_transformer: Callable[[ResponsePlayer], PlayerTeamDetails]
                 ) -> None:
        self.name_details_transformer = name_details_transformer
        self.image_details_transformer = image_details_transformer
        self.competition_details_transformer = competition_details_transformer
        self.team_details_transformer = team_details_transformer

    def transform(self, response_player: ResponsePlayer) -> Player:
        return Player(
            competition=self.competition_details_transformer(response_player.competition) if
            response_player.competition is not None else None,
            draftable_id=response_player.draftable_id,
            draft_alerts=response_player.draft_alerts,
            image_details=self.image_details_transformer(response_player),
            is_disabled=response_player.is_disabled,
            is_swappable=response_player.is_swappable,
            name_details=self.name_details_transformer(response_player),
            news_status=response_player.news_status,
            player_id=response_player.player_id,
            position=response_player.position,
            roster_slot_id=response_player.roster_slot_id,
            salary=response_player.salary,
            team_details=self.team_details_transformer(response_player)
        )


def transform_competition_team_details(response_competition_team_details: ResponseCompetitionTeam) -> CompetitionTeam:
    return CompetitionTeam(
        abbreviation=response_competition_team_details.abbreviation,
        city=response_competition_team_details.city,
        team_id=response_competition_team_details.team_id,
        name=response_competition_team_details.team_name
    )


def transform_competition_weather_details(response_competition_weather_details: ResponseCompetitionWeather) -> \
        CompetitionWeather:
    return CompetitionWeather(
        description=response_competition_weather_details.icon,
        is_in_a_dome=response_competition_weather_details.is_dome
    )


class CompetitionTransformer:
    def __init__(self, team_details_transformer: Callable[[ResponseCompetitionTeam], CompetitionTeam],
                 weather_details_transformer: Callable[[ResponseCompetitionWeather], CompetitionWeather]):
        self.team_details_transformer = team_details_transformer
        self.weather_details_transformer = weather_details_transformer

    def transform(self, response_competition: ResponseCompetition) -> Competition:
        return Competition(
            are_depth_charts_available=response_competition.are_depth_charts_available,
            are_starting_lineups_available=response_competition.are_starting_lineups_available,
            away_team=self.team_details_transformer(response_competition.away_team) if response_competition.away_team
                                                                                       is not None else None,
            competition_id=response_competition.competition_id,
            home_team=self.team_details_transformer(response_competition.home_team) if response_competition.home_team
                                                                                       is not None else None,
            name=response_competition.name,
            sport=CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS.get(response_competition.sport),
            starts_at=response_competition.start_time,
            state=response_competition.competition_state,
            venue=response_competition.venue,
            weather=response_competition.weather
        )


class DraftablesTransformer:
    def __init__(self, competition_transformer: CompetitionTransformer, player_transformer: PlayerTransformer):
        self.competition_transformer = competition_transformer
        self.player_transformer = player_transformer

    def transform(self, response_draftables: ResponseDraftables) -> Draftables:
        return Draftables(
            competitions=[
                self.competition_transformer.transform(response_competition=competition)
                for competition in response_draftables.competitions
            ],
            players=[
                self.player_transformer.transform(response_player=player)
                for player in response_draftables.draftables
            ]
        )
