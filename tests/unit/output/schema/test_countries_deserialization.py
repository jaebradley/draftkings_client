from unittest import TestCase

import marshmallow

from draft_kings.output.objects.countries import CountryDetails, CountriesDetails
from draft_kings.output.schema.countries import CountryDetailsSchema, CountriesDetailsSchema


class TestCountryDetailsSchemaLoading(TestCase):
    def test_loading_empty_object(self):
        self.assertRaises(
            marshmallow.ValidationError,
            CountryDetailsSchema().load,
            {}
        )

    def test_validation_error_when_invalid_value_is_loaded(self):
        self.assertRaises(
            marshmallow.ValidationError,
            CountryDetailsSchema().load,
            {
                "code": 123
            }
        )

    def test_extraneous_properties_raise_validation_error(self):
        self.assertRaises(
            marshmallow.ValidationError,
            CountryDetailsSchema().load,
            {
                "code": "jaebaebae",
                "country_id": 1,
                "is_licensed": True,
                "name": "bae jadley",
                "jaebaebae": True
            }
        )

    def test_correct_properties_are_serialized_appropriately(self):
        self.assertEqual(
            CountryDetails(
                code="jaebaebae",
                country_id=1,
                is_licensed=True,
                name="bae jadley",
            ),
            CountryDetailsSchema().load({
                "code": "jaebaebae",
                "country_id": 1,
                "is_licensed": True,
                "name": "bae jadley",
            })
        )


class CountriesDetailsSchemaLoading(TestCase):
    def setUp(self) -> None:
        self.schema = CountriesDetailsSchema()

    def test_empty_list(self):
        self.assertEqual(
            CountriesDetails(countries=[]),
            self.schema.load({"countries": []})
        )

    def test_non_empty_list(self):
        self.assertEqual(
            CountriesDetails(
                countries=[
                    CountryDetails(
                        code="some code",
                        country_id=456,
                        is_licensed=True,
                        name="jaebaebae"
                    )
                ]
            ),
            self.schema.load({
                "countries": [
                    {
                        "code": "some code",
                        "country_id": 456,
                        "is_licensed": True,
                        "name": "jaebaebae"
                    }
                ]
            })
        )
