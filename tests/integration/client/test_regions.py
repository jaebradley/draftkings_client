import os
from unittest import TestCase
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.regions import RegionDetails
from tests.config import ROOT_DIRECTORY


class TestRegions(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_american_regions_is_not_none(self):
        regions = self.client.regions("US")
        self.assertIsNotNone(regions)

    def test_american_regions_exist(self):
        regions = self.client.regions("US")
        self.assertGreater(len(regions.regions), 0)

    def test_first_american_region(self):
        regions = self.client.regions("US")
        self.assertEqual(
            RegionDetails(
                code="AL",
                country_code="US",
                iso_code="US-AL",
                name="Alabama"
            ),
            regions.regions[0]
        )

    def test_british_regions_is_not_none(self):
        regions = self.client.regions("GB")
        self.assertIsNotNone(regions)

    def test_british_regions_exist(self):
        regions = self.client.regions("GB")
        self.assertGreater(len(regions.regions), 0)

    def test_canadian_regions_is_not_none(self):
        regions = self.client.regions("CA")
        self.assertIsNotNone(regions)

    def test_canadian_regions_exist(self):
        regions = self.client.regions("CA")
        self.assertGreater(len(regions.regions), 0)


class TestMockedUSResponseRegions(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/regions/us.json"), encoding="utf-8") as data_file:
            self.response_data = data_file.read()
            patched_method = patch.object(HTTPClient, "regions")
            mocked_method = patched_method.start()
            mocked_method.return_value = Mock(text=self.response_data)
            self.result = Client().regions("US")

    def tearDown(self) -> None:
        patch.stopall()

    def test_exists(self):
        self.assertIsNotNone(self.result)

    def test_length(self):
        self.assertEqual(62, len(self.result.regions))

    def test_first_region(self):
        self.assertEqual(
            RegionDetails(
                country_code="US",
                code="AL",
                iso_code="US-AL",
                name="Alabama"
            ),
            self.result.regions[0]
        )
