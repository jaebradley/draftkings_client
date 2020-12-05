from unittest import TestCase

from draft_kings.client import Client
from draft_kings.data import Sport


class TestClient(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_get_available_players(self):
        result = self.client.available_players(draft_group_id=11513)
        self.assertIsNotNone(result)

    def test_get_draft_group_details(self):
        response = self.client.draft_group_details(draft_group_id=11513)
        self.assertIsNotNone(response)

    def test_get_draftables(self):
        response = self.client.draftables(draft_group_id=18186)
        self.assertIsNotNone(response)

    def test_regions(self):
        response = self.client.regions("US")
        self.assertIsNotNone(response)

    def test_countries(self):
        response = self.client.countries()
        self.assertIsNotNone(response)

    def test_contests(self):
        response = self.client.contests(Sport.NBA)
        self.assertIsNotNone(response)
