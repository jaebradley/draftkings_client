from unittest import TestCase

from draft_kings_client.draft_kings_client import DraftKingsClient
from draft_kings_client.data.models.league import League


class TestClient(TestCase):
    def test_get_contests(self):
        result = DraftKingsClient.get_contests(League.nba)
        self.assertIsNotNone(result)

    def test_get_available_players(self):
        result = DraftKingsClient.get_available_players(draft_group_id=11513)
        self.assertIsNotNone(result)
