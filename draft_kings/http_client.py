import requests
from requests.models import Response

from draft_kings.data import Sport, SPORT_TO_CONTESTS_ABBREVIATION
from draft_kings.url_builder import URLBuilder


class HTTPClient:
    def __init__(self, url_builder: URLBuilder) -> None:
        self.url_builder: URLBuilder = url_builder

    def countries(self) -> Response:
        response: Response = requests.get(url=self.url_builder.countries(), params={"format": "json"})
        response.raise_for_status()
        return response

    def regions(self, country_code: str) -> Response:
        response: Response = requests.get(
            url=self.url_builder.regions(country_code=country_code), params={"format": "json"}
        )
        response.raise_for_status()
        return response

    def contests(self, sport: Sport) -> Response:
        response: Response = requests.get(
            url=self.url_builder.contests(), params={"sport": SPORT_TO_CONTESTS_ABBREVIATION.get(sport)}
        )
        response.raise_for_status()
        return response

    def available_players(self, draft_group_id: int) -> Response:
        response: Response = requests.get(
            url=self.url_builder.available_players(), params={"draftGroupId": draft_group_id}
        )
        response.raise_for_status()
        return response

    def draft_group_details(self, draft_group_id: int) -> Response:
        response: Response = requests.get(url=self.url_builder.draft_groups(draft_group_id=draft_group_id))
        response.raise_for_status()
        return response

    def draftables(self, draft_group_id: int) -> Response:
        response: Response = requests.get(url=self.url_builder.draftables(draft_group_id=draft_group_id))
        response.raise_for_status()
        return response

    def game_type_rules(self, game_type_id: int) -> Response:
        response: Response = requests.get(
            url=self.url_builder.game_type_rules(game_type_id=game_type_id), params={"format": "json"}
        )
        response.raise_for_status()
        return response
