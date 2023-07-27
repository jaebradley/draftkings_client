from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from draft_kings.data import Sport
from draft_kings.utilities import transform_sport_id


class Contest(BaseModel):
    type_id: int | None = Field(validation_alias="contestTypeId", default=None)
    game_type_description: str | None = Field(validation_alias="gameType", default=None)


class StartTime(BaseModel):
    maximum: datetime | None = Field(validation_alias="maxStartTime", default=None)
    minimum: datetime | None = Field(validation_alias="minStartTime", default=None)
    type_description: str | None = Field(validation_alias="startTimeType", default=None)

    @field_validator("maximum", "minimum", mode="before")
    def check_datetime(cls, v: datetime) -> datetime:
        return v if v is not None else None


class League(BaseModel):
    abbreviation: str | None = Field(validation_alias="leagueAbbreviation", default=None)
    league_id: int | None = Field(validation_alias="leagueId", default=None)
    name: str | None = Field(validation_alias="leagueName", default=None)


class Game(BaseModel):
    away_team_id: int | None = Field(validation_alias="awayTeamId", default=None)
    description: str | None = Field(validation_alias="description", default=None)
    game_id: int | None = Field(validation_alias="gameId", default=None)
    home_team_id: int | None = Field(validation_alias="homeTeamId", default=None)
    location: str | None = Field(validation_alias="location", default=None)
    name: str | None = Field(validation_alias="name", default=None)
    starts_at: datetime | None = Field(validation_alias="startDate", default=None)
    status_description: str | None = Field(validation_alias="status", default=None)


class DraftGroup(BaseModel):
    contest_details: Contest = Field(validation_alias="contestType")
    draft_group_id: int | None = Field(validation_alias="draftGroupId", default=None)
    games: list[Game] = Field(validation_alias="games")
    leagues: list[League] = Field(validation_alias="leagues")
    sport: Sport | None = Field(validation_alias="sportId", default=None)
    start_time: StartTime = Field(validation_alias="start_time_details", default=None)
    draft_group_state: str | None = Field(validation_alias="draftGroupState", default=None)

    @model_validator(mode="before")
    def set_entries(cls, data: dict) -> dict:
        data: dict = data.get("draftGroup")
        # move relevant items to 'start_time_details' parent key
        data["start_time_details"] = {}
        for k in ["maxStartTime", "minStartTime", "startTimeType"]:
            if v := data.pop(k, None):
                data["start_time_details"][k] = v
        return data

    @field_validator("sport", mode="before")
    def check_datetime(cls, v: int | None) -> Sport | None:
        return transform_sport_id(v)
