from pydantic import BaseModel, Field


class Country(BaseModel):
    code: str | None = Field(validation_alias="countryCode", default=None)
    country_id: int | None = Field(validation_alias="countryId", default=None)
    is_licensed: bool | None = Field(validation_alias="isLicensed", default=None)
    name: str | None = Field(validation_alias="name", default=None)


class Countries(BaseModel):
    countries: list[Country] = Field(validation_alias="countries", default=[])
