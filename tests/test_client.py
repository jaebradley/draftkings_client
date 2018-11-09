from unittest import TestCase

from draft_kings_client.data import Sport
from draft_kings_client.draft_kings_client import DraftKingsClient


class TestClient(TestCase):
    def test_get_contests(self):
        result = DraftKingsClient.get_contests(Sport.NBA)
        self.assertIsNotNone(result)

    def test_get_available_players(self):
        result = DraftKingsClient.get_available_players(draft_group_id=11513)
        self.assertIsNotNone(result)

    def test_get_draft_group_details(self):
        response = DraftKingsClient.get_draft_group_details(draft_group_id=11513)
        self.assertIsNotNone(response)

    def test_get_countries(self):
        response = DraftKingsClient.get_countries()
        self.assertIsNotNone(response)

    def test_get_regions(self):
        response = DraftKingsClient.get_regions(country_code='US')
        self.assertIsNotNone(response)

    def test_get_contest_details(self):
        response = DraftKingsClient.get_contest_details(contest_id=54639629)
        self.assertIsNotNone(response)

    def test_get_draftables(self):
        response = DraftKingsClient.get_draftables(draft_group_id=18186)
        self.assertIsNotNone(response)
