from unittest import TestCase

from draft_kings.data import Sport
from draft_kings import client


class TestClientContests(TestCase):
    def test_nba_contests(self):
        result = client.contests(Sport.NBA)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_nfl_contests(self):
        result = client.contests(Sport.NFL)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_mlb_contests(self):
        result = client.contests(Sport.MLB)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_nhl_contests(self):
        result = client.contests(Sport.NHL)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_nascar_contests(self):
        result = client.contests(Sport.NASCAR)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_golf_contests(self):
        result = client.contests(Sport.GOLF)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_cfl_contests(self):
        result = client.contests(Sport.CFL)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_college_football_contests(self):
        result = client.contests(Sport.COLLEGE_FOOTBALL)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_college_basketball_contests(self):
        result = client.contests(Sport.COLLEGE_BASKETBALL)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_mma_contests(self):
        result = client.contests(Sport.MIXED_MARTIAL_ARTS)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_eurloeage_basketball_contests(self):
        result = client.contests(Sport.EUROLEAGUE_BASKETBALL)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_tennis_contests(self):
        result = client.contests(Sport.TENNIS)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])

    def test_league_of_legends_contests(self):
        result = client.contests(Sport.LEAGUE_OF_LEGENDS)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result["contests"])
        self.assertIsNotNone(result["groups"])