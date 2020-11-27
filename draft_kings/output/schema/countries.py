from marshmallow import Schema, fields, post_load

from draft_kings.output.objects.countries import CountryDetails, CountriesDetails


class CountryDetailsSchema(Schema):
    code = fields.Str(missing=None)
    country_id = fields.Int(missing=None)
    is_licensed = fields.Bool(missing=None)
    name = fields.Str(missing=None)

    @post_load
    def make_country_details(self, data, **kwargs):
        return CountryDetails(**data)


class CountriesDetailsSchema(Schema):
    countries = fields.List(fields.Nested(CountryDetailsSchema), missing=[])

    @post_load
    def make_countries_details(self, data, **kwargs):
        return CountriesDetails(**data)
