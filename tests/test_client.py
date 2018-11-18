from unittest import TestCase

from draft_kings_client.data import Sport
from draft_kings_client.client import contests, available_players, draft_group_details, countries, regions, \
    contest_details, draftables


class TestClient(TestCase):
    def test_get_contests(self):
        result = contests(Sport.NBA)
        self.assertIsNotNone(result)

    def test_get_available_players(self):
        result = available_players(draft_group_id=11513)
        self.assertIsNotNone(result)

    def test_get_draft_group_details(self):
        response = draft_group_details(draft_group_id=11513)
        self.assertIsNotNone(response)

    def test_get_countries(self):
        response = countries()
        self.assertIsNotNone(response)

    def test_get_regions(self):
        response = regions(country_code='US')
        self.assertIsNotNone(response)

    def test_get_contest_details(self):
        response = contest_details(contest_id=54639629)
        self.assertIsNotNone(response)

    def test_get_draftables(self):
        response = draftables(draft_group_id=18186)
        self.assertIsNotNone(response)
