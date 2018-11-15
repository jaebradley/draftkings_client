import requests

from draft_kings_client.data import Sport
from draft_kings_client.response_translators import translate_players, translate_contests
from draft_kings_client import urls

sport_parameter_value = {
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
}


class DraftKingsClient:

    def __init__(self):
        pass

    @staticmethod
    def get_contests(sport):
        assert isinstance(sport, Sport)

        response = requests.get(url=urls.CONTESTS_URL,
                                params={'sport': sport_parameter_value[sport]})

        response.raise_for_status()

        return translate_contests(response=response.json())

    @staticmethod
    def get_available_players(draft_group_id):
        if type(draft_group_id) is not int and type(draft_group_id) is not int:
            raise TypeError('draft group id must be an integer or long')

        response = requests.get(url=urls.AVAILABLE_PLAYERS_URL,
                                params={'draftGroupId': draft_group_id})

        response.raise_for_status()

        return translate_players(response=response.json())

    @staticmethod
    def get_draft_group_details(draft_group_id):
        response = requests.get(url=urls.draft_group_url(draft_group_id),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_countries(include_unlicensed=True):
        response = requests.get(url=urls.COUNTRIES_URL,
                                params={'format': 'json', 'includeUnlicensed': include_unlicensed})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_regions(country_code):
        response = requests.get(url=urls.regions_url(country_code),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_contest_details(contest_id):
        response = requests.get(url=urls.contest_url(contest_id),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_draftables(draft_group_id):
        response = requests.get(url=urls.draftables_url(draft_group_id),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()
