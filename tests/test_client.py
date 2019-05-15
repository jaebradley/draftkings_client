from unittest import TestCase

from draft_kings.client import available_players, draft_group_details, draftables, regions, contests, countries
from draft_kings.data import Sport


class TestClient(TestCase):
    def test_get_available_players(self):
        result = available_players(draft_group_id=11513)
        self.assertIsNotNone(result)

    def test_get_draft_group_details(self):
        response = draft_group_details(draft_group_id=11513)
        self.assertIsNotNone(response)

    def test_get_draftables(self):
        response = draftables(draft_group_id=18186)
        self.assertIsNotNone(response)

    def test_regions(self):
        response = regions("US")
        self.assertIsNotNone(response)

    def test_countries(self):
        response = countries()
        self.assertIsNotNone(response)

    def test_contests(self):
        response = contests(Sport.NBA)
        self.assertIsNotNone(response)
