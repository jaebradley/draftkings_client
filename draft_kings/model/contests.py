from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from draft_kings.data import Sport
from draft_kings.utilities import (
    translate_formatted_datetime,
    collect,
    flatten,
    transform_sport_id,
    transform_sport_abbreviation,
)


class Entries(BaseModel):
    fee: float | None = Field(validation_alias="a", default=None)
    maximum: int | None = Field(validation_alias="m", default=None)
    total: int | None = Field(validation_alias="nt", default=None)


class Contest(BaseModel):
    contest_id: int | None = Field(validation_alias="id", default=None)
    draft_group_id: int | None = Field(validation_alias="dg", default=None)
    entries_details: Entries | None = Field(validation_alias="entries", default=None)
    fantasy_player_points: float | None = Field(validation_alias="fpp", default=None)

    is_double_up: bool = Field(validation_alias="IsDoubleUp", default=False)
    is_fifty_fifty: bool = Field(validation_alias="IsFiftyFifty", default=False)
    is_guaranteed: bool = Field(validation_alias="IsGuaranteed", default=False)
    is_head_to_head: bool = Field(validation_alias="IsH2h", default=False)
    is_starred: bool = Field(validation_alias="IsStarred", default=False)

    name: str | None = Field(validation_alias="n", default=None)
    payout: float | None = Field(validation_alias="po", default=None)
    sport: Sport | None = Field(validation_alias="s", default=None)
    starts_at: datetime | None = Field(validation_alias="sd", default=None)

    @model_validator(mode="before")
    def transform(cls, data: dict) -> dict:
        flatten(data, "attr")
        collect(data, "entries", ["a", "m", "nt"])
        return data

    @field_validator("sport", mode="before")
    def transform_sport_id(cls, v: int | None) -> Sport | None:
        return transform_sport_id(v)

    @field_validator("starts_at", mode="before")
    def translate_formatted_datetime(cls, v: str) -> datetime:
        return translate_formatted_datetime(v)


class DraftGroup(BaseModel):
    draft_group_id: int | None = Field(validation_alias="DraftGroupId", default=None)
    series_id: int | None = Field(validation_alias="DraftGroupSeriesId", default=None)
    contest_type_id: int | None = Field(validation_alias="ContestTypeId", default=None)
    game_count: int | None = Field(validation_alias="GameCount", default=None)
    sport: Sport | None = Field(validation_alias="Sport", default=None)
    starts_at: datetime | None = Field(validation_alias="StartDate", default=None)

    @field_validator("sport", mode="before")
    def transform_sport_abbreviation(cls, v: str | None) -> Sport | None:
        return transform_sport_abbreviation(v)


class Contests(BaseModel):
    contests: list[Contest] = Field(validation_alias="Contests", default=[])
    draft_groups: list[DraftGroup] = Field(validation_alias="DraftGroups", default=[])
