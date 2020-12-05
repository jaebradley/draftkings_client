import requests
from requests.models import Response

from draft_kings.data import Sport, SPORT_TO_CONTESTS_ABBREVIATION
from draft_kings.url_builder import URLBuilder


class HTTPClient:
    def __init__(self, url_builder: URLBuilder) -> None:
        self.url_builder = url_builder

    def countries(self):
        response = requests.get(url=self.url_builder.build_countries_url(),
                                params={'format': 'json'})

        response.raise_for_status()

        return response

    def regions(self, country_code):
        response = requests.get(url=self.url_builder.build_regions_url(country_code=country_code),
                                params={'format': 'json'})

        response.raise_for_status()

        return response

    def contests(self, sport: Sport) -> Response:
        response = requests.get(url=self.url_builder.build_contests_url(),
                                params={'sport': SPORT_TO_CONTESTS_ABBREVIATION.get(sport)})

        response.raise_for_status()

        return response

    def available_players(self, draft_group_id: int) -> Response:
        response = requests.get(url=self.url_builder.build_available_players_url(),
                                params={'draftGroupId': draft_group_id})

        response.raise_for_status()

        return response

    def draft_group_details(self, draft_group_id: int) -> Response:
        response = requests.get(url=self.url_builder.build_draft_group_url(draft_group_id=draft_group_id))

        response.raise_for_status()

        return response

    def draftables(self, draft_group_id: int) -> Response:
        response = requests.get(url=self.url_builder.build_draftables_url(draft_group_id=draft_group_id))

        response.raise_for_status()

        return response
