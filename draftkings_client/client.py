import requests

from data.models.league import League
from data.translators.contests_response_translator import ContestsResponseTranslator


class Client:

    def __init__(self):
        pass

    @staticmethod
    def get_contests(league):
        assert isinstance(league, League)

        response = requests.get(url='https://www.draftkings.com/lobby/getcontests',
                                params={'sport': league._value_})

        response.raise_for_status()

        return ContestsResponseTranslator.translate(response=response)