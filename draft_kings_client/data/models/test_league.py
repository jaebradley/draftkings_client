from unittest import TestCase

from draft_kings_client.data.models.league import League


class TestLeague(TestCase):
    def test_get_id(self):
        self.assertEqual(League.nfl.get_id(), 1)

    def test_from_id(self):
        self.assertEqual(League.from_id(league_id=1), League.nfl)
