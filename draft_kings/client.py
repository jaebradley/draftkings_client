# pylint: disable=too-many-instance-attributes
from typing import AnyStr

from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.contests import ContestsDetails
from draft_kings.output.objects.countries import CountriesDetails
from draft_kings.output.objects.draft_group import DraftGroupDetails
from draft_kings.output.objects.draftables import DraftablesDetails
from draft_kings.output.objects.players import PlayersDetails
from draft_kings.output.objects.regions import RegionsDetails
from draft_kings.output.transformers.contests import ContestsDetailsTransformer, DraftGroupTransformer, \
    ContestTransformer
from draft_kings.output.transformers.countries import CountriesTransformer, transform_country
from draft_kings.output.transformers.draft_group import transform_contest as transform_draft_group_contest, \
    transform_draft_group_start_time_details, \
    transform_game, transform_league, DraftGroupDetailsTransformer
from draft_kings.output.transformers.draftables import transform_competition_team_details, \
    transform_competition_weather_details, transform_player_competition_details, transform_player_image_details, \
    transform_player_name_details, transform_player_team_details, PlayerTransformer, CompetitionTransformer, \
    DraftablesTransformer, transform_draft_alert
from draft_kings.output.transformers.players import TeamSeriesTransformer, DraftDetailsTransformer, \
    transform_player_position, transform_player_team_series_details, PlayerDetailsTransformer, \
    PlayersDetailsTransformer, ExceptionalMessageTransformer, transform_exceptional_message_type
from draft_kings.output.transformers.regions import RegionsTransformer, transform_region
from draft_kings.output.transformers.sports import transform_sport_id, transform_sport_abbreviation
from draft_kings.response.schema.contests import ContestsSchema
from draft_kings.response.schema.countries import CountriesSchema
from draft_kings.response.schema.draft_group import DraftGroupResponseSchema
from draft_kings.response.schema.draftables import DraftablesSchema
from draft_kings.response.schema.players import PlayersDetailsSchema
from draft_kings.response.schema.regions import RegionsSchema
from draft_kings.url_builder import URLBuilder
from draft_kings.utilities import translate_formatted_datetime, from_unix_milliseconds_to_datetime


class Client:
    contest_details_transformer: ContestsDetailsTransformer
    players_details_transformer: PlayersDetailsTransformer
    draft_group_details_transformer: DraftGroupDetailsTransformer
    countries_transformer: CountriesTransformer
    regions_transformer: RegionsTransformer
    draftables_transformer: DraftablesTransformer

    contests_schema: ContestsSchema
    players_schema: PlayersDetailsSchema
    draft_group_schema: DraftGroupResponseSchema
    countries_schema: CountriesSchema
    regions_schema: RegionsSchema
    draftables_schema: DraftablesSchema

    http_client: HTTPClient

    def __init__(self):
        self.contest_details_transformer = ContestsDetailsTransformer(
            contest_transformer=ContestTransformer(
                formatted_datetime_transformer=translate_formatted_datetime,
                sport_id_transformer=transform_sport_id,
            ),
            draft_group_transformer=DraftGroupTransformer(
                sport_abbreviation_transformer=transform_sport_abbreviation,
            )
        )
        self.players_details_transformer = PlayersDetailsTransformer(
            team_series_transformer=TeamSeriesTransformer(
                formatted_datetime_translator=translate_formatted_datetime
            ),
            player_details_transformer=PlayerDetailsTransformer(
                draft_details_transformer=DraftDetailsTransformer(
                    unix_milliseconds_translator=from_unix_milliseconds_to_datetime
                ),
                player_team_series_details_transformer=transform_player_team_series_details,
                player_position_transformer=transform_player_position,
                exceptional_message_transformer=ExceptionalMessageTransformer(
                    message_type_transformer=transform_exceptional_message_type
                )
            )
        )
        self.draft_group_details_transformer = DraftGroupDetailsTransformer(
            contest_transformer=transform_draft_group_contest,
            game_transformer=transform_game,
            league_transformer=transform_league,
            sport_id_transformer=transform_sport_id,
            start_time_details_transformer=transform_draft_group_start_time_details
        )
        self.countries_transformer = CountriesTransformer(country_transformer=transform_country)
        self.regions_transformer = RegionsTransformer(region_transformer=transform_region)
        self.draftables_transformer = DraftablesTransformer(
            competition_transformer=CompetitionTransformer(
                team_details_transformer=transform_competition_team_details,
                weather_details_transformer=transform_competition_weather_details,
                sport_abbreviation_transformer=transform_sport_abbreviation,
            ),
            player_transformer=PlayerTransformer(
                competition_details_transformer=transform_player_competition_details,
                name_details_transformer=transform_player_name_details,
                image_details_transformer=transform_player_image_details,
                team_details_transformer=transform_player_team_details,
                draft_alert_transformer=transform_draft_alert,
            )
        )
        self.contests_schema = ContestsSchema()
        self.players_schema = PlayersDetailsSchema()
        self.draft_group_schema = DraftGroupResponseSchema()
        self.countries_schema = CountriesSchema()
        self.regions_schema = RegionsSchema()
        self.draftables_schema = DraftablesSchema()
        self.http_client = HTTPClient(url_builder=URLBuilder())

    def contests(self, sport: Sport) -> ContestsDetails:
        response = self.http_client.contests(sport=sport)
        deserialized_response = self.contests_schema.loads(response.text)
        return self.contest_details_transformer.transform(deserialized_response)

    def available_players(self, draft_group_id: int) -> PlayersDetails:
        response = self.http_client.available_players(draft_group_id=draft_group_id)
        deserialized_response = self.players_schema.loads(response.text)
        return self.players_details_transformer.transform(deserialized_response)

    def draft_group_details(self, draft_group_id: int) -> DraftGroupDetails:
        response = self.http_client.draft_group_details(draft_group_id=draft_group_id)
        deserialized_response = self.draft_group_schema.loads(response.text)
        return self.draft_group_details_transformer.transform(draft_group=deserialized_response.draft_group)

    def countries(self) -> CountriesDetails:
        response = self.http_client.countries()
        deserialized_response = self.countries_schema.loads(response.text)
        return self.countries_transformer.transform(deserialized_response)

    def regions(self, country_code: AnyStr) -> RegionsDetails:
        response = self.http_client.regions(country_code=country_code)
        deserialized_response = self.regions_schema.loads(response.text)
        return self.regions_transformer.transform(deserialized_response)

    def draftables(self, draft_group_id: int) -> DraftablesDetails:
        response = self.http_client.draftables(draft_group_id=draft_group_id)
        deserialized_response = self.draftables_schema.loads(response.text)
        return self.draftables_transformer.transform(response_draftables=deserialized_response)

# pylint: enable=too-many-instance-attributes
