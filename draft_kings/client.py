import json

import requests

from draft_kings import urls
from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.contests import ContestsDetails
from draft_kings.output.objects.players import PlayersDetails
from draft_kings.output.transformers.contests import ContestsDetailsResponseTransformer, ContestsResponseTransformer, \
    transform_contest, transform_draft_group, DraftGroupsTransformer
from draft_kings.output.transformers.players import transform_team_series, transform_draft_details, \
    transform_player_position, transform_player_team_series_details, PlayerDetailsTransformer, PlayersDetailsTransformer
from draft_kings.response.decoders import CountriesDecoder, RegionsDecoder
from draft_kings.response.schema.contests import ContestsSchema
from draft_kings.response.schema.players import PlayersDetailsSchema
from draft_kings.response_translators import translate_draft_group, \
    translate_draftables
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


def draft_group_details(draft_group_id):
    response = requests.get(url=urls.draft_group_url(draft_group_id),
                            params={'format': 'json'})

    response.raise_for_status()

    return translate_draft_group(response.json())


def countries():
    response = HTTPClient(url_builder=URLBuilder()).countries()
    data = json.loads(response.text, cls=CountriesDecoder)
    return list(map(lambda country_data: country_data.asdict(), data))


def regions(country_code):
    response = HTTPClient(url_builder=URLBuilder()).regions(country_code=country_code)
    data = json.loads(response.text, cls=RegionsDecoder)
    return list(map(lambda region_data: region_data.asdict(), data))


def draftables(draft_group_id):
    response = requests.get(url=urls.draftables_url(draft_group_id),
                            params={'format': 'json'})

    response.raise_for_status()

    return translate_draftables(response.json())
