import os
from unittest import TestCase

from draft_kings.response.objects.regions import Region
from draft_kings.response.schema.regions import RegionsSchema
from tests.config import ROOT_DIRECTORY


class TestUSRegions(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/us_regions.json')) as data_file:
            self.schema = RegionsSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(62, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region(
                country_code="US",
                region_code="AL",
                iso_region_code="US-AL",
                name="Alabama"
            ),
            self.data.regions[0]
        )
