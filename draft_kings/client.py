import requests

from draft_kings import urls
from draft_kings.response_translators import translate_players, translate_contests, translate_countries, \
    translate_draft_group, translate_regions, translate_draftables, SPORT_TO_CONTESTS_ABBREVIATION


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
    response = requests.get(url=urls.COUNTRIES_URL,
                            params={'format': 'json'})

    response.raise_for_status()

    return translate_countries(response.json())


def regions(country_code):
    response = requests.get(url=urls.regions_url(country_code),
                            params={'format': 'json'})

    response.raise_for_status()

    return translate_regions(response.json())


def draftables(draft_group_id):
    response = requests.get(url=urls.draftables_url(draft_group_id),
                            params={'format': 'json'})

    response.raise_for_status()

    return translate_draftables(response.json())
