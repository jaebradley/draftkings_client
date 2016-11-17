from unittest import TestCase

from draftkings_client.client import Client
from draftkings_client.data.models.league import League


class TestClient(TestCase):
    def test_get_contests(self):
        result = Client.get_contests(League.nba)
        self.assertIsNotNone(result)

    def test_get_available_players(self):
        result = Client.get_available_players(draft_group_id=11513)
        self.assertIsNotNone(result)
