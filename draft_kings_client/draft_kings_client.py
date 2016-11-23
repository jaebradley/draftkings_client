import requests

from data.models.league import League
from data.translators.available_players_translator import AvailablePlayersTranslator
from data.translators.contests_response_translator import ContestsResponseTranslator
from data.utilities.url_builder import UrlBuilder


class DraftKingsClient:

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
    def get_available_players(draft_group_id):
        if type(draft_group_id) is not int and type(draft_group_id) is not long:
            raise TypeError('draft group id must be an integer or long')

        response = requests.get(url=UrlBuilder.get_available_players_url(),
                                params={'draftGroupId': draft_group_id})

        response.raise_for_status()

        return AvailablePlayersTranslator.translate(response=response.json())