from typing import Callable, Optional

from draft_kings.data import Sport
from draft_kings.output.objects.draftables import PlayerNameDetails, PlayerImageDetails, PlayerCompetitionDetails, \
    PlayerTeamDetails, PlayerDetails, CompetitionTeamDetails, CompetitionWeatherDetails, CompetitionDetails, \
    DraftablesDetails, PlayerDraftAlertDetails
from draft_kings.response.objects.draftables import Player as ResponsePlayer, PlayerCompetitionDetails as \
    ResponsePlayerCompetitionDetails, CompetitionTeam as ResponseCompetitionTeam, CompetitionWeather as \
    ResponseCompetitionWeather, Competition as ResponseCompetition, Draftables as ResponseDraftables, \
    DraftAlert as ResponseDraftAlert


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
        one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url=player.player_image_160
    )


def transform_player_competition_details(
        response_player_competition_details: ResponsePlayerCompetitionDetails
) -> PlayerCompetitionDetails:
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


def transform_draft_alert(draft_alert: ResponseDraftAlert) -> PlayerDraftAlertDetails:
    return PlayerDraftAlertDetails(
        alert_description=draft_alert.alert_type,
        message=draft_alert.message,
        updated_at=draft_alert.updated_date,
        priority_value=draft_alert.priority
    )


class PlayerTransformer:
    def __init__(self, name_details_transformer: Callable[[ResponsePlayer], PlayerNameDetails],
                 image_details_transformer: Callable[[ResponsePlayer], PlayerImageDetails],
                 competition_details_transformer: Callable[
                     [ResponsePlayerCompetitionDetails], PlayerCompetitionDetails
    ],
        team_details_transformer: Callable[[ResponsePlayer], PlayerTeamDetails],
        draft_alert_transformer: Callable[[ResponseDraftAlert], PlayerDraftAlertDetails]
    ) -> None:
        self.name_details_transformer = name_details_transformer
        self.image_details_transformer = image_details_transformer
        self.competition_details_transformer = competition_details_transformer
        self.team_details_transformer = team_details_transformer
        self.draft_alert_transformer = draft_alert_transformer

    def transform(self, response_player: ResponsePlayer) -> PlayerDetails:
        return PlayerDetails(
            competition_details=self.competition_details_transformer(response_player.competition)
            if response_player.competition is not None else None,
            draftable_id=response_player.draftable_id,
            draft_alerts=list(map(self.draft_alert_transformer, response_player.draft_alerts)),
            image_details=self.image_details_transformer(response_player),
            is_disabled=response_player.is_disabled,
            is_swappable=response_player.is_swappable,
            name_details=self.name_details_transformer(response_player),
            news_status_description=response_player.news_status,
            player_id=response_player.player_id,
            position_name=response_player.position,
            roster_slot_id=response_player.roster_slot_id,
            salary=response_player.salary,
            team_details=self.team_details_transformer(response_player)
        )


def transform_competition_team_details(
        response_competition_team_details: ResponseCompetitionTeam) -> CompetitionTeamDetails:
    return CompetitionTeamDetails(
        abbreviation=response_competition_team_details.abbreviation,
        city=response_competition_team_details.city,
        team_id=response_competition_team_details.team_id,
        name=response_competition_team_details.team_name
    )


def transform_competition_weather_details(
        response_competition_weather_details: ResponseCompetitionWeather
) -> CompetitionWeatherDetails:
    return CompetitionWeatherDetails(
        description=response_competition_weather_details.icon,
        is_in_a_dome=response_competition_weather_details.is_dome
    )


class CompetitionTransformer:
    def __init__(self, team_details_transformer: Callable[[ResponseCompetitionTeam], CompetitionTeamDetails],
                 weather_details_transformer: Callable[[ResponseCompetitionWeather], CompetitionWeatherDetails],
                 sport_abbreviation_transformer: Callable[[Optional[str]], Optional[Sport]]) -> None:
        self.team_details_transformer = team_details_transformer
        self.weather_details_transformer = weather_details_transformer
        self.sport_abbreviation_transformer = sport_abbreviation_transformer

    def transform(self, response_competition: ResponseCompetition) -> CompetitionDetails:
        return CompetitionDetails(
            are_depth_charts_available=response_competition.are_depth_charts_available,
            are_starting_lineups_available=response_competition.are_starting_lineups_available,
            away_team=self.team_details_transformer(response_competition.away_team)
            if response_competition.away_team is not None else None,
            competition_id=response_competition.competition_id,
            home_team=self.team_details_transformer(response_competition.home_team)
            if response_competition.home_team is not None else None,
            name=response_competition.name,
            sport=self.sport_abbreviation_transformer(response_competition.sport),
            starts_at=response_competition.start_time,
            state_description=response_competition.competition_state,
            venue=response_competition.venue,
            weather=self.weather_details_transformer(response_competition.weather)
            if response_competition.weather is not None else None
        )


class DraftablesTransformer:
    def __init__(self, competition_transformer: CompetitionTransformer, player_transformer: PlayerTransformer) -> None:
        self.competition_transformer = competition_transformer
        self.player_transformer = player_transformer

    def transform(self, response_draftables: ResponseDraftables) -> DraftablesDetails:
        return DraftablesDetails(
            competitions=list(map(
                lambda competition: self.competition_transformer.transform(response_competition=competition),
                response_draftables.competitions
            )),
            players=list(map(
                lambda player: self.player_transformer.transform(response_player=player),
                response_draftables.draftables
            ))
        )
