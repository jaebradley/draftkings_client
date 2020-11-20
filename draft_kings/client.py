import json

from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.contests import ContestsDetails
from draft_kings.output.objects.draft_group import DraftGroupDetails
from draft_kings.output.objects.players import PlayersDetails
from draft_kings.output.transformers.contests import ContestsDetailsResponseTransformer, ContestsResponseTransformer, \
    transform_contest, transform_draft_group, DraftGroupsTransformer
from draft_kings.output.transformers.draft_group import transform_contest as transform_draft_group_contest, \
    transform_draft_group_starts_at, \
    transform_game, transform_league, DraftGroupDetailsTransformer
from draft_kings.output.transformers.players import transform_team_series, transform_draft_details, \
    transform_player_position, transform_player_team_series_details, PlayerDetailsTransformer, PlayersDetailsTransformer
from draft_kings.output.transformers.sports import transform_sport_id
from draft_kings.response.decoders import CountriesDecoder, RegionsDecoder
from draft_kings.response.schema.contests import ContestsSchema
from draft_kings.response.schema.draft_group import DraftGroupResponseSchema
from draft_kings.response.schema.players import PlayersDetailsSchema
from draft_kings.response_translators import translate_draftables
from draft_kings.response.schema.draftables import DraftablesSchema
from draft_kings.output.objects.draftables import Draftables
from draft_kings.output.transformers.draftables import transform_competition_team_details, \
    transform_competition_weather_details, transform_player_competition_details, transform_player_image_details, \
    transform_player_name_details, transform_player_team_details, PlayerTransformer, CompetitionTransformer, \
    DraftablesTransformer
from draft_kings.urls import URLBuilder


def contests(sport: Sport) -> ContestsDetails:
    response = HTTPClient(url_builder=URLBuilder()).contests(sport)

    schema = ContestsSchema()
    deserialized_response = schema.loads(response.text)

    return ContestsDetailsResponseTransformer(
        ContestsResponseTransformer(transform_contest),
        DraftGroupsTransformer(transform_draft_group)
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


def countries():
    response = HTTPClient(url_builder=URLBuilder()).countries()
    data = json.loads(response.text, cls=CountriesDecoder)
    return list(map(lambda country_data: country_data.asdict(), data))


def regions(country_code):
    response = HTTPClient(url_builder=URLBuilder()).regions(country_code=country_code)
    data = json.loads(response.text, cls=RegionsDecoder)
    return list(map(lambda region_data: region_data.asdict(), data))


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
