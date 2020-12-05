# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load, EXCLUDE

from draft_kings.response.objects.countries import Country, Countries


class CountrySchema(Schema):
    class Meta:
        unknown = EXCLUDE

    countryCode = fields.Str(attribute="country_code", missing=None)
    countryId = fields.Int(attribute="country_id", missing=None)
    isLicensed = fields.Bool(attribute="is_licensed", missing=None)
    name = fields.Str(attribute="name", missing=None)

    @post_load
    def make_country(self, data, **kwargs):
        return Country(**data)


class CountriesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    countries = fields.List(fields.Nested(CountrySchema), missing=[])

    @post_load
    def make_country(self, data, **kwargs):
        return Countries(**data)

# pylint: enable=unused-argument, no-self-use
