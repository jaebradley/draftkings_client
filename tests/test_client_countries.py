from unittest import TestCase

from draft_kings import client


class TestClientCountries(TestCase):
    def test_countries_are_not_none(self):
        response = client.countries()
        self.assertIsNotNone(response)

    def test_more_than_one_country_exists(self):
        response = client.countries()
        self.assertGreater(len(response), 0)

    def test_county_keys_exist(self):
        response = client.countries()
        for country in response:
            self.assertCountEqual(
                list(country.keys()),
                [
                    "id",
                    "code",
                    "name",
                    "licensed",
                ]
            )