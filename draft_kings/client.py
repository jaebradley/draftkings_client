from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.contests import ContestsDetails
from draft_kings.output.objects.countries import CountriesDetails
from draft_kings.output.objects.draft_group import DraftGroupDetails
from draft_kings.output.objects.draftables import Draftables
from draft_kings.output.objects.players import PlayersDetails
from draft_kings.output.objects.regions import Regions
from draft_kings.output.transformers.contests import ContestsDetailsTransformer, DraftGroupTransformer, \
    ContestTransformer
from draft_kings.output.transformers.countries import CountriesTransformer, transform_country
from draft_kings.output.transformers.draft_group import transform_contest as transform_draft_group_contest, \
    transform_draft_group_starts_at, \
    transform_game, transform_league, DraftGroupDetailsTransformer
from draft_kings.output.transformers.draftables import transform_competition_team_details, \
    transform_competition_weather_details, transform_player_competition_details, transform_player_image_details, \
    transform_player_name_details, transform_player_team_details, PlayerTransformer, CompetitionTransformer, \
    DraftablesTransformer
from draft_kings.output.transformers.players import transform_team_series, transform_draft_details, \
    transform_player_position, transform_player_team_series_details, PlayerDetailsTransformer, PlayersDetailsTransformer
from draft_kings.output.transformers.regions import RegionsTransformer, transform_region
from draft_kings.output.transformers.sports import transform_sport_id, transform_sport_abbreviation
from draft_kings.response.schema.contests import ContestsSchema
from draft_kings.response.schema.countries import CountriesSchema
from draft_kings.response.schema.draft_group import DraftGroupResponseSchema
from draft_kings.response.schema.draftables import DraftablesSchema
from draft_kings.response.schema.players import PlayersDetailsSchema
from draft_kings.response.schema.regions import RegionsSchema
from draft_kings.url_builder import URLBuilder
from draft_kings.utilities import translate_formatted_datetime


def contests(sport: Sport) -> ContestsDetails:
    response = HTTPClient(url_builder=URLBuilder()).contests(sport)

    schema = ContestsSchema()
    deserialized_response = schema.loads(response.text)

    return ContestsDetailsTransformer(
        contest_transformer=ContestTransformer(
            formatted_datetime_transformer=translate_formatted_datetime,
            sport_id_transformer=transform_sport_id,
        ),
        draft_group_transformer=DraftGroupTransformer(
            sport_abbreviation_transformer=transform_sport_abbreviation,
        )
    ).transform(deserialized_response)


def available_players(draft_group_id: int) -> PlayersDetails:
    response = HTTPClient(url_builder=URLBuilder()).available_players(draft_group_id)

    schema = PlayersDetailsSchema()
    deserialized_response = schema.loads(response.text)

    return PlayersDetailsTransformer(
        team_series_transformer=transform_team_series,
        player_details_transformer=PlayerDetailsTransformer(
            draft_details_transformer=transform_draft_details,
            player_team_series_details_transformer=transform_player_team_series_details,
            player_position_transformer=transform_player_position
        )
    ).transform(deserialized_response)


def draft_group_details(draft_group_id) -> DraftGroupDetails:
    response = HTTPClient(url_builder=URLBuilder()).draft_group_details(draft_group_id=draft_group_id)

    schema = DraftGroupResponseSchema()
    deserialized_response = schema.loads(response.text)

    return DraftGroupDetailsTransformer(
        contest_transformer=transform_draft_group_contest,
        game_transformer=transform_game,
        league_transformer=transform_league,
        sport_id_transformer=transform_sport_id,
        starts_at_transformer=transform_draft_group_starts_at
    ).transform(draft_group=deserialized_response.draft_group)


def countries() -> CountriesDetails:
    response = HTTPClient(url_builder=URLBuilder()).countries()
    schema = CountriesSchema()
    deserialized_response = schema.loads(response.text)
    return CountriesTransformer(country_transformer=transform_country).transform(deserialized_response)


def regions(country_code: str) -> Regions:
    response = HTTPClient(url_builder=URLBuilder()).regions(country_code=country_code)
    schema = RegionsSchema()
    deserialized_response = schema.loads(response.text)
    return RegionsTransformer(region_transformer=transform_region).transform(deserialized_response)


def draftables(draft_group_id: int) -> Draftables:
    response = HTTPClient(url_builder=URLBuilder()).draftables(draft_group_id=draft_group_id)

    schema = DraftablesSchema()
    deserialized_response = schema.loads(response.text)

    return DraftablesTransformer(
        competition_transformer=CompetitionTransformer(
            team_details_transformer=transform_competition_team_details,
            weather_details_transformer=transform_competition_weather_details,
        ),
        player_transformer=PlayerTransformer(
            competition_details_transformer=transform_player_competition_details,
            name_details_transformer=transform_player_name_details,
            image_details_transformer=transform_player_image_details,
            team_details_transformer=transform_player_team_details,
        )
    ).transform(response_draftables=deserialized_response)
