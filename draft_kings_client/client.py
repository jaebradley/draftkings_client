import requests

from draft_kings_client import urls
from draft_kings_client.data import Sport
from draft_kings_client.response_translators import translate_players, translate_contests, translate_countries, \
    translate_draft_group, translate_regions

sports = {
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
                            params={'sport': sports[sport]})

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


def contest_details(contest_id):
    response = requests.get(url=urls.contest_url(contest_id),
                            params={'format': 'json'})

    response.raise_for_status()

    return response.json()


def draftables(draft_group_id):
    response = requests.get(url=urls.draftables_url(draft_group_id),
                            params={'format': 'json'})

    response.raise_for_status()

    return response.json()