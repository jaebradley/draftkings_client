from unittest import TestCase

from draft_kings.output.objects.countries import CountriesDetails, CountryDetails
from draft_kings.output.transformers.countries import CountriesTransformer, transform_country
from draft_kings.response.objects.countries import Country as ResponseCountry, Countries as ResponseCountries


class TestCountryTransformer(TestCase):
    def test_transforming_country_with_defined_values(self) -> None:
        self.assertEqual(
            CountryDetails(
                code="jaebabeae",
                country_id=1,
                is_licensed=True,
                name="baejaejae"
            ),
            transform_country(
                ResponseCountry(
                    country_code="jaebabeae",
                    country_id=1,
                    is_licensed=True,
                    name="baejaejae"
                )
            )
        )

    def test_transforming_country_with_none_values(self) -> None:
        self.assertEqual(
            CountryDetails(
                code=None,
                country_id=None,
                is_licensed=None,
                name=None
            ),
            transform_country(
                ResponseCountry(
                    country_code=None,
                    country_id=None,
                    is_licensed=None,
                    name=None
                )
            )
        )


class TestCountriesTransformer(TestCase):
    def setUp(self) -> None:
        self.transformer = CountriesTransformer(country_transformer=transform_country)

    def test_empty_countries(self):
        self.assertEqual(
            CountriesDetails(countries=[]),
            self.transformer.transform(countries=ResponseCountries(countries=[]))
        )

    def test_existing_countries(self):
        self.assertEqual(
            CountriesDetails(
                countries=[
                    CountryDetails(
                        code="jaebabeae",
                        country_id=1,
                        is_licensed=True,
                        name="baejaejae"
                    ),
                    CountryDetails(
                        code=None,
                        country_id=None,
                        is_licensed=None,
                        name=None
                    ),
                ]
            ),
            self.transformer.transform(
                countries=ResponseCountries(
                    countries=[
                        ResponseCountry(
                            country_code="jaebabeae",
                            country_id=1,
                            is_licensed=True,
                            name="baejaejae"
                        ),
                        ResponseCountry(
                            country_code=None,
                            country_id=None,
                            is_licensed=None,
                            name=None
                        )
                    ]
                )
            )
        )
