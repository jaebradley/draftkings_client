import os
from unittest import TestCase
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.countries import CountriesDetails, CountryDetails
from tests.config import ROOT_DIRECTORY


class TestCountries(TestCase):
    def setUp(self) -> None:
        self.result = Client().countries()

    def test_countries_are_not_none(self):
        self.assertIsNotNone(self.result)

    def test_more_than_one_country_exists(self):
        self.assertGreater(len(self.result.countries), 0)


class TestCountiesWithMockedHTTPResponse(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/countries.json"), encoding="utf-8") as data_file:
            self.response_data = data_file.read()

    @patch.object(HTTPClient, "countries")
    def test_countries_are_not_none(self, mocked_countries):
        mocked_countries.return_value = Mock(name="countries_response", text=self.response_data)
        self.assertIsNotNone(Client().countries())

    @patch.object(HTTPClient, "countries")
    def test_translated_country_details(self, mocked_countries):
        mocked_countries.return_value = Mock(name="countries_response", text=self.response_data)
        self.assertEqual(
            CountriesDetails(
                countries=[
                    CountryDetails(
                        country_id=1,
                        code="US",
                        name="United States",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=14,
                        code="AU",
                        name="Australia",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=15,
                        code="AT",
                        name="Austria",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=2,
                        code="CA",
                        name="Canada",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=4,
                        code="DE",
                        name="Germany",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=89,
                        code="IE",
                        name="Ireland",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=117,
                        code="MT",
                        name="Malta",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=132,
                        code="NL",
                        name="Netherlands",
                        is_licensed=True
                    ),
                    CountryDetails(
                        country_id=3,
                        code="GB",
                        name="United Kingdom",
                        is_licensed=True
                    )
                ]
            ),
            Client().countries()
        )
