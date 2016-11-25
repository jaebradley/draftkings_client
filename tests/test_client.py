from unittest import TestCase

from draft_kings_client.draft_kings_client import DraftKingsClient
from draft_kings_client.data.models.sport import Sport


class TestClient(TestCase):
    def test_get_contests(self):
        result = DraftKingsClient.get_contests(Sport.nba)
        self.assertIsNotNone(result)

    def test_get_available_players(self):
        result = DraftKingsClient.get_available_players(draft_group_id=11513)
        self.assertIsNotNone(result)
