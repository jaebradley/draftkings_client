from unittest import TestCase

from draft_kings.urls import CONTESTS_URL, AVAILABLE_PLAYERS_URL, COUNTRIES_URL, draft_group_url, regions_url, \
    contest_url, draftables_url


class TestUrls(TestCase):
    def test_contests_url(self):
        self.assertEqual(CONTESTS_URL, "https://www.draftkings.com/lobby/getcontests")

    def test_available_players_url(self):
        self.assertEqual(AVAILABLE_PLAYERS_URL, "https://www.draftkings.com/lineup/getavailableplayers")

    def test_countries_url(self):
        self.assertEqual(COUNTRIES_URL, "https://api.draftkings.com/addresses/v1/countries/")

    def test_draft_group_url(self):
        self.assertEqual(draft_group_url("jaebaebae"), "https://api.draftkings.com/draftgroups/v1/jaebaebae")

    def test_regions_url(self):
        self.assertEqual(regions_url("jaebaebae"), "https://api.draftkings.com/addresses/v1/countries/jaebaebae/regions")

    def test_contest_url(self):
        self.assertEqual(contest_url("jaebaebae"), "https://api.draftkings.com/contests/v1/contests/jaebaebae")

    def test_draftables_url(self):
        self.assertEqual(draftables_url("jaebaebae"), "https://api.draftkings.com/draftgroups/v1/draftgroups/jaebaebae/draftables")
