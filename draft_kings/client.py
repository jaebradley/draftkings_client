# pylint: disable=too-many-instance-attributes
import json
import pprint
from typing import AnyStr

from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.model.contests import Contests
from draft_kings.model.countries import Countries
from draft_kings.model.draft_group import DraftGroup
from draft_kings.model.draftables import Draftables
from draft_kings.model.game_type_rules import GameTypeRules
from draft_kings.model.players import Players
from draft_kings.model.regions import Regions
from draft_kings.url_builder import URLBuilder


class Client:
    def __init__(self) -> None:
        self.http_client: HTTPClient = HTTPClient(url_builder=URLBuilder())

    def contests(self, sport: Sport) -> Contests:
        response = self.http_client.contests(sport=sport)
        return Contests.model_validate_json(response.text)

    def available_players(self, draft_group_id: int) -> Players:
        response = self.http_client.available_players(draft_group_id=draft_group_id)
        return Players.model_validate_json(response.text)

    def draft_group_details(self, draft_group_id: int) -> DraftGroup:
        response = self.http_client.draft_group_details(draft_group_id=draft_group_id)
        return DraftGroup.model_validate_json(response.text)

    def countries(self) -> Countries:
        response = self.http_client.countries()
        return Countries.model_validate_json(response.text)

    def regions(self, country_code: AnyStr) -> Regions:
        response = self.http_client.regions(country_code=country_code)
        return Regions.model_validate_json(response.text)

    def draftables(self, draft_group_id: int) -> Draftables:
        response = self.http_client.draftables(draft_group_id=draft_group_id)
        return Draftables.model_validate_json(response.text)

    def game_type_rules(self, game_type_id: int) -> GameTypeRules:
        response = self.http_client.game_type_rules(game_type_id=game_type_id)
        return GameTypeRules.model_validate_json(response.text)


# pylint: enable=too-many-instance-attributes
if __name__ == "__main__":
    c: Client = Client()
    pprint.pprint(c.contests(Sport.NBA).model_dump())
    pprint.pprint(c.available_players(41793).model_dump())
    pprint.pprint(c.draft_group_details(90053).model_dump())
    pprint.pprint(c.countries().model_dump())
    pprint.pprint(c.regions("GB").model_dump())
    pprint.pprint(c.draftables(41793).model_dump())
    pprint.pprint(c.game_type_rules(1).model_dump())
