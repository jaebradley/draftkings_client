from marshmallow import Schema, fields


class RegionDetailsSchema(Schema):
    code = fields.Str(missing=None)
    country_code = fields.Str(missing=None)
    iso_code = fields.Str(missing=None)
    name = fields.Str(missing=None)


class RegionsDetailsSchema(Schema):
    regions = fields.List(fields.Nested(RegionDetailsSchema), missing=[])
