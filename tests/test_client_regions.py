from unittest import TestCase

from draft_kings_client import client


class TestClientRegions(TestCase):
    def test_american_regions(self):
        regions = client.regions("US")
        self.assertIsNotNone(regions)
        self.assertGreater(len(regions), 0)
        self.assertEqual(len(regions), 61)

    def test_first_american_region(self):
        regions = client.regions("US")
        first_region = regions[0]
        self.assertEqual(first_region["country_code"], "US")
        self.assertEqual(first_region["code"], "AL")
        self.assertEqual(first_region["iso_code"], "US-AL")
        self.assertEqual(first_region["name"], "Alabama")

    def test_british_regions(self):
        regions = client.regions("GB")
        self.assertIsNotNone(regions)
        self.assertGreater(len(regions), 0)

    def test_canadian_regions(self):
        regions = client.regions("CA")
        self.assertIsNotNone(regions)
        self.assertGreater(len(regions), 0)
