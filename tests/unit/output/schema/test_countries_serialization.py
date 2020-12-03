from unittest import TestCase

from draft_kings.output.objects.countries import CountryDetails, CountriesDetails
from draft_kings.output.schema.countries import CountryDetailsSchema, CountriesDetailsSchema


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
        self.assertRaises(ValueError, CountryDetailsSchema().dump, {
            "code": 123, "country_id": "jaebaebae",
            "is_licensed": True, "name": "bae jadley"
        })

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


class CountriesDetailsSchemaDumping(TestCase):
    def setUp(self) -> None:
        self.schema = CountriesDetailsSchema()

    def test_empty_list(self):
        self.assertEqual({"countries": []}, self.schema.dump(CountriesDetails(countries=[])))

    def test_list_with_objects(self):
        self.assertEqual(
            {
                "countries": [
                    {
                        "code": "some code",
                        "country_id": 456,
                        "is_licensed": True,
                        "name": "jaebaebae"
                    }
                ],
            },
            self.schema.dump(CountriesDetails(
                countries=[
                    CountryDetails(
                        code="some code",
                        country_id=456,
                        is_licensed=True,
                        name="jaebaebae"
                    )
                ]
            ))
        )
