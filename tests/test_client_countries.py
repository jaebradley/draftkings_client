from unittest import TestCase

from draft_kings_client import client


class TestClientCountries(TestCase):
    def test_countries(self):
        response = client.countries()
        self.assertIsNotNone(response)