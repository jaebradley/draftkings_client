from unittest import TestCase

from draft_kings import client


class TestClientRegions(TestCase):
    def test_american_regions_is_not_none(self):
        regions = client.regions("US")
        self.assertIsNotNone(regions)

    def test_american_regions_exist(self):
        regions = client.regions("US")
        self.assertGreater(len(regions), 0)

    def test_first_american_region(self):
        regions = client.regions("US")
        first_region = regions[0]
        self.assertEqual(first_region["country_code"], "US")
        self.assertEqual(first_region["code"], "AL")
        self.assertEqual(first_region["iso_code"], "US-AL")
        self.assertEqual(first_region["name"], "Alabama")

    def test_british_regions_is_not_none(self):
        regions = client.regions("GB")
        self.assertIsNotNone(regions)

    def test_british_regions_exist(self):
        regions = client.regions("GB")
        self.assertGreater(len(regions), 0)

    def test_canadian_regions_is_not_none(self):
        regions = client.regions("CA")
        self.assertIsNotNone(regions)

    def test_canadian_regions_exist(self):
        regions = client.regions("CA")
        self.assertGreater(len(regions), 0)
