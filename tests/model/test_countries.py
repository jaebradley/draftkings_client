import os
from unittest import TestCase

from draft_kings.model.countries import Country, Countries
from tests.config import ROOT_DIRECTORY


class TestCountries(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/countries.json"), encoding="utf-8") as data_file:
            self.data: Countries = Countries.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_countries_data(self) -> None:
        self.assertEqual(
            Countries.model_construct(
                countries=[
                    Country.model_construct(country_id=1, code="US", name="United States", is_licensed=True),
                    Country.model_construct(country_id=14, code="AU", name="Australia", is_licensed=True),
                    Country.model_construct(country_id=15, code="AT", name="Austria", is_licensed=True),
                    Country.model_construct(country_id=2, code="CA", name="Canada", is_licensed=True),
                    Country.model_construct(country_id=4, code="DE", name="Germany", is_licensed=True),
                    Country.model_construct(country_id=89, code="IE", name="Ireland", is_licensed=True),
                    Country.model_construct(country_id=117, code="MT", name="Malta", is_licensed=True),
                    Country.model_construct(country_id=132, code="NL", name="Netherlands", is_licensed=True),
                    Country.model_construct(country_id=3, code="GB", name="United Kingdom", is_licensed=True),
                ]
            ),
            self.data,
        )
