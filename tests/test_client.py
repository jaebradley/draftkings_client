from unittest import TestCase

from draftkings_client.draftkings_client import DraftkingsClient
from draftkings_client.data.models.league import League


class TestClient(TestCase):
    def test_get_contests(self):
        result = DraftkingsClient.get_contests(League.nba)
        self.assertIsNotNone(result)

    def test_get_available_players(self):
        result = DraftkingsClient.get_available_players(draft_group_id=11513)
        self.assertIsNotNone(result)
