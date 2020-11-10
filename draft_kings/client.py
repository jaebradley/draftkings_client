import json

import requests

from draft_kings import urls
from draft_kings.http_client import HTTPClient
from draft_kings.response.decoders import CountriesDecoder, RegionsDecoder
from draft_kings.response_translators import translate_players, translate_contests, translate_draft_group, \
    translate_draftables, SPORT_TO_CONTESTS_ABBREVIATION
from draft_kings.urls import URLBuilder


def contests(sport):
    response = requests.get(url=urls.CONTESTS_URL,
                            params={'sport': SPORT_TO_CONTESTS_ABBREVIATION[sport]})

    response.raise_for_status()

    return translate_contests(response=response.json())


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
