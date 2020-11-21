from marshmallow import Schema, fields, EXCLUDE


class CountrySchema(Schema):
    class Meta:
        unknown = EXCLUDE

    code = fields.Str(missing=None)
    country_id = fields.Int(missing=None)
    is_licensed = fields.Bool(missing=None)
    name = fields.Str(missing=None)


class CountriesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    countries = fields.List(fields.Nested(CountrySchema), missing=[])
