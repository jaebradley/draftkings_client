# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load

from draft_kings.output.objects.regions import RegionDetails, RegionsDetails


class RegionDetailsSchema(Schema):
    code = fields.Str(allow_none=True, required=True)
    country_code = fields.Str(allow_none=True, required=True)
    iso_code = fields.Str(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)

    @post_load
    def make_region_details(self, data, **kwargs):
        return RegionDetails(**data)


class RegionsDetailsSchema(Schema):
    regions = fields.List(fields.Nested(RegionDetailsSchema, required=True), required=True)

    @post_load
    def make_regions_details(self, data, **kwargs):
        return RegionsDetails(**data)

# pylint: enable=unused-argument, no-self-use
