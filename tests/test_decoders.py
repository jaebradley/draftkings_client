import json
import os
from unittest import TestCase

from draft_kings.response.decoders import CountriesDecoder, RegionsDecoder
from draft_kings.data import CountryData, RegionData
from tests.config import ROOT_DIRECTORY


class TestCountryDecoder(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/countries.json')) as data_file:
            self.data = json.load(data_file, cls=CountriesDecoder)

    def test_exists(self):
        self.assertIsNotNone(self.data)

    def test_data(self):
        self.assertListEqual(
            [
                CountryData(1, "US", "United States", True),
                CountryData(14, "AU", "Australia", True),
                CountryData(15, "AT", "Austria", True),
                CountryData(2, "CA", "Canada", True),
                CountryData(4, "DE", "Germany", True),
                CountryData(89, "IE", "Ireland", True),
                CountryData(117, "MT", "Malta", True),
                CountryData(132, "NL", "Netherlands", True),
                CountryData(3, "GB", "United Kingdom", True)
            ],
            self.data
        )


class TestUSRegionsDecoder(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/us_regions.json')) as data_file:
            self.data = json.load(data_file, cls=RegionsDecoder)

    def test_exists(self):
        self.assertIsNotNone(self.data)

    def test_has_more_than_one_element(self):
        self.assertGreater(len(self.data), 0)

    def test_first_element_is_same(self):
        self.assertEqual(
            RegionData("US", "AL", "US-AL", "Alabama"),
            self.data[0]
        )
