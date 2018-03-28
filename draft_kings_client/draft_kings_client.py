import requests

from data.models.sport import Sport
from data.translators.available_players_translator import AvailablePlayersTranslator
from data.translators.contests_response_translator import ContestsResponseTranslator
from data.utilities.url_builder import UrlBuilder


class DraftKingsClient:

    def __init__(self):
        pass

    @staticmethod
    def get_contests(sport):
        assert isinstance(sport, Sport)

        response = requests.get(url=UrlBuilder.get_contest_url(),
                                params={'sport': sport._value_})

        response.raise_for_status()

        return ContestsResponseTranslator.translate(response=response.json())

    @staticmethod
    def get_available_players(draft_group_id):
        if type(draft_group_id) is not int and type(draft_group_id) is not long:
            raise TypeError('draft group id must be an integer or long')

        response = requests.get(url=UrlBuilder.get_available_players_url(),
                                params={'draftGroupId': draft_group_id})

        response.raise_for_status()

        return AvailablePlayersTranslator.translate(response=response.json())

    @staticmethod
    def get_draft_group_details(draft_group_id):
        response = requests.get(url=UrlBuilder.get_draft_group_url(draft_group_id),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_countries(include_unlicensed=True):
        response = requests.get(url=UrlBuilder.get_countries_url(),
                                params={'format': 'json', 'includeUnlicensed': include_unlicensed})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_regions(country_code):
        response = requests.get(url=UrlBuilder.get_regions_url(country_code),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_contest_details(contest_id):
        response = requests.get(url=UrlBuilder.get_contest_details_url(contest_id),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_draftables(draft_group_id):
        response = requests.get(url=UrlBuilder.get_draftables_url(draft_group_id),
                                params={'format': 'json'})

        response.raise_for_status()

        return response.json()
