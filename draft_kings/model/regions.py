from pydantic import BaseModel, Field


class Region(BaseModel):
    code: str | None = Field(validation_alias="regionCode", default=None)
    country_code: str | None = Field(validation_alias="countryCode", default=None)
    iso_code: str | None = Field(validation_alias="isoRegionCode", default=None)
    name: str | None = Field(validation_alias="name", default=None)


class Regions(BaseModel):
    regions: list[Region] = Field(validation_alias="regions", default=[])
