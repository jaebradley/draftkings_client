# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load

from draft_kings.output.objects.countries import CountryDetails, CountriesDetails


class CountryDetailsSchema(Schema):
    code = fields.Str(allow_none=True, required=True)
    country_id = fields.Int(allow_none=True, required=True)
    is_licensed = fields.Bool(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)

    @post_load
    def make_country_details(self, data, **kwargs):
        return CountryDetails(**data)


class CountriesDetailsSchema(Schema):
    countries = fields.List(fields.Nested(CountryDetailsSchema, required=True), required=True)

    @post_load
    def make_countries_details(self, data, **kwargs):
        return CountriesDetails(**data)

# pylint: enable=unused-argument, no-self-use
