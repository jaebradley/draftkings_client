from unittest import TestCase
import marshmallow


from draft_kings.output.objects.countries import CountryDetails, CountriesDetails
from draft_kings.output.schema.countries import CountryDetailsSchema


class TestCountryDetailsSchemaLoading(TestCase):
    def test_loading_empty_object(self):
        self.assertEqual(
            CountryDetails(
                code=None,
                country_id=None,
                is_licensed=None,
                name=None
            ),
            CountryDetailsSchema().load({})
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


class TestCountryDetailsSchemaDumping(TestCase):
    def test_empty_dictionary(self):
        self.assertEqual(
            {},
            CountryDetailsSchema().dump({})
        )

    def test_default_country_details_object(self):
        self.assertEqual(
            {
                "code": None,
                "country_id": None,
                "is_licensed": None,
                "name": None
            },
            CountryDetailsSchema().dump(
                CountryDetails(
                    code=None,
                    country_id=None,
                    is_licensed=None,
                    name=None
                ),
            )
        )

    def test_numeric_value_is_stringified_when_used_as_a_string_value(self):
        self.assertEqual(
            {
                "code": "123",
                "country_id": 456,
                "is_licensed": True,
                "name": "jaebaebae"
            },
            CountryDetailsSchema().dump({
                "code": 123,
                "country_id": 456,
                "is_licensed": True,
                "name": "jaebaebae"
            })
        )

    def test_integer_value_raises_value_error_when_string_value_is_passed(self):
        self.assertRaises(ValueError, CountryDetailsSchema().dump, {"code": 123, "country_id": "jaebaebae",
                                                                    "is_licensed": True, "name": "bae jadley"})

    def test_extraneous_property_is_removed(self):
        self.assertEqual(
            {
                "code": "some code",
                "country_id": 456,
                "is_licensed": True,
                "name": "jaebaebae"
            },
            CountryDetailsSchema().dump({
                "code": "some code",
                "country_id": 456,
                "is_licensed": True,
                "name": "jaebaebae",
                "jaebaebae": "bae jadley"
            })
        )

