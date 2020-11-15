import json

import requests

from draft_kings import urls
from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects import ContestsDetails
from draft_kings.output.transformers import ContestsDetailsResponseTransformer, ContestsResponseTransformer, \
    transform_contest, transform_draft_group, DraftGroupsTransformer
from draft_kings.response.decoders import CountriesDecoder, RegionsDecoder
from draft_kings.response.schema.contests import ContestsSchema
from draft_kings.response_translators import translate_players, translate_draft_group, \
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


def available_players(draft_group_id):
    response = requests.get(url=urls.AVAILABLE_PLAYERS_URL,
                            params={'draftGroupId': draft_group_id})

    response.raise_for_status()

    return translate_players(response=response.json())


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
