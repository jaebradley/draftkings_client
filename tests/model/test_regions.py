import os
from unittest import TestCase

from draft_kings.model.regions import Region, Regions
from tests.config import ROOT_DIRECTORY


class TestUSRegions(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/regions/us.json"), encoding="utf-8") as data_file:
            self.data: Regions = Regions.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(62, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region.model_construct(country_code="US", code="AL", iso_code="US-AL", name="Alabama"), self.data.regions[0]
        )


class TestCanadianRegions(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/regions/ca.json"), encoding="utf-8") as data_file:
            self.data: Regions = Regions.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(13, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region.model_construct(country_code="CA", code="AB", iso_code="CA-AB", name="Alberta"), self.data.regions[0]
        )


class TestGBRegions(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/regions/gb.json"), encoding="utf-8") as data_file:
            self.data: Regions = Regions.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_regions_length(self):
        self.assertEqual(225, len(self.data.regions))

    def test_first_region(self):
        self.assertEqual(
            Region.model_construct(country_code="GB", code="ABE", iso_code="GB-ABE", name="Aberdeen City"),
            self.data.regions[0],
        )
