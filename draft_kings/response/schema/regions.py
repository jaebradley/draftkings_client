# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load, EXCLUDE

from draft_kings.response.objects.regions import Region, Regions


class RegionSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    countryCode = fields.Str(attribute="country_code", missing=None)
    isoRegionCode = fields.Str(attribute="iso_region_code", missing=None)
    name = fields.Str(attribute="name", missing=None)
    regionCode = fields.Str(attribute="region_code", missing=None)

    @post_load
    def make_region(self, data, **kwargs):
        return Region(**data)


class RegionsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    regions = fields.List(fields.Nested(RegionSchema), attribute="regions", missing=[])

    @post_load
    def make_regions(self, data, **kwargs):
        return Regions(**data)

# pylint: enable=unused-argument, no-self-use
