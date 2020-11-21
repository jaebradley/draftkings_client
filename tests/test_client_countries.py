from unittest import TestCase

from draft_kings import client


class TestClientCountries(TestCase):
    def test_countries_are_not_none(self):
        result = client.countries()
        self.assertIsNotNone(result)

    def test_more_than_one_country_exists(self):
        result = client.countries()
        self.assertGreater(len(result), 0)
