from unittest import TestCase

from draft_kings_client.data import Sport


class TestSport(TestCase):
    def test_get_id(self):
        self.assertEqual(Sport.nfl.get_id(), 1)

    def test_from_id(self):
        self.assertEqual(Sport.from_id(sport_id=1), Sport.nfl)
