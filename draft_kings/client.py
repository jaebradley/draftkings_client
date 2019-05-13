import requests

from draft_kings import urls
from draft_kings.data import Sport
from draft_kings.response_translators import translate_players, translate_contests, translate_countries, \
    translate_draft_group, translate_regions, translate_draftables

"""
The API takes a sport query parameter that's different than then sports API endpoint
"""
SPORT_TO_CONTESTS_QUERY_PARAMETER = {
    Sport.NFL: "NFL",
    Sport.NHL: "NHL",
    Sport.NBA: "NBA",
    Sport.CFL: "CFL",
    Sport.COLLEGE_FOOTBALL: "CFB",
    Sport.MIXED_MARTIAL_ARTS: "MMA",
    Sport.NASCAR: "NAS",
    Sport.SOCCER: "SOC",
    Sport.EUROLEAGUE_BASKETBALL: "EL",
    Sport.MLB: "MLB",
    Sport.TENNIS: "TEN",
    Sport.LEAGUE_OF_LEGENDS: "LOL",
    Sport.GOLF: "GOLF",
    Sport.COLLEGE_BASKETBALL: "CBB"
}


def contests(sport):
    response = requests.get(url=urls.CONTESTS_URL,
                            params={'sport': SPORT_TO_CONTESTS_QUERY_PARAMETER[sport]})

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
