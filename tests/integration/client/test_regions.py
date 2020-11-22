from unittest import TestCase

from draft_kings import client
from draft_kings.output.objects.regions import Region


class TestRegions(TestCase):
    def test_american_regions_is_not_none(self):
        regions = client.regions("US")
        self.assertIsNotNone(regions)

    def test_american_regions_exist(self):
        regions = client.regions("US")
        self.assertGreater(len(regions.regions), 0)

    def test_first_american_region(self):
        regions = client.regions("US")
        self.assertEqual(
            Region(
                code="AL",
                country_code="US",
                iso_code="US-AL",
                name="Alabama"
            ),
            regions.regions[0]
        )

    def test_british_regions_is_not_none(self):
        regions = client.regions("GB")
        self.assertIsNotNone(regions)

    def test_british_regions_exist(self):
        regions = client.regions("GB")
        self.assertGreater(len(regions.regions), 0)

    def test_canadian_regions_is_not_none(self):
        regions = client.regions("CA")
        self.assertIsNotNone(regions)

    def test_canadian_regions_exist(self):
        regions = client.regions("CA")
        self.assertGreater(len(regions.regions), 0)
