from unittest import TestCase

from draft_kings_client.data.utilities.url_builder import UrlBuilder


class TestUrlBuilder(TestCase):
    def test_contest_url(self):
        self.assertEqual(UrlBuilder.get_contest_url(), 'https://www.draftkings.com/lobby/getcontests')

    def test_get_available_players_url(self):
        self.assertEqual(UrlBuilder.get_available_players_url(), 'https://www.draftkings.com/lineup/getavailableplayers')
