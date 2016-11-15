import requests

from data.models.league import League
from data.translators.contests_response_translator import ContestsResponseTranslator
from draftkings_client.requests.url_builder import UrlBuilder


class Client:

    def __init__(self):
        pass

    @staticmethod
    def get_contests(league):
        assert isinstance(league, League)

        response = requests.get(url=UrlBuilder.get_contest_url(),
                                params={'sport': league._value_})

        response.raise_for_status()

        return ContestsResponseTranslator.translate(response=response.json())

    @staticmethod
    def get_player_list(draft_group_id):
        if type(draft_group_id) is not int or type(draft_group_id) is not long:
            raise TypeError('draft group id must be an integer or long')

        response = requests.get(url=UrlBuilder.get_player_list_url(),
                                params={'draftGroupId', draft_group_id})

        response.raise_for_status()

        return response