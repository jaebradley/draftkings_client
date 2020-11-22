from unittest import TestCase

from draft_kings import client


class TestCountries(TestCase):
    def setUp(self) -> None:
        self.result = client.countries()

    def test_countries_are_not_none(self):
        self.assertIsNotNone(self.result)

    def test_more_than_one_country_exists(self):
        self.assertGreater(len(self.result), 0)
