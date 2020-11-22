from marshmallow import Schema, fields, EXCLUDE


class RegionSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    code = fields.Str(missing=None)
    country_code = fields.Str(missing=None)
    iso_code = fields.Str(missing=None)
    name = fields.Str(missing=None)


class RegionsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    regions = fields.List(fields.Nested(RegionSchema), missing=None)
