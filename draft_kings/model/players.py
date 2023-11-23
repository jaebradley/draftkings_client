from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from draft_kings.utilities import from_unix_milliseconds_to_datetime, collect, translate_formatted_datetime


class TeamSeries(BaseModel):
    away_team_id: int | None = Field(validation_alias="atid", default=None)
    home_team_id: int | None = Field(validation_alias="htid", default=None)
    starts_at: datetime | None = Field(validation_alias="tz", default=None)
    status_description: str | None = Field(validation_alias="status", default=None)
    team_series_id: int | None = Field(validation_alias="team_series_id", default=None)
    weather: str | None = Field(validation_alias="wthr", default=None)

    @field_validator("starts_at", mode="before")
    def transform_starts_at(cls, v: str) -> datetime:
        return translate_formatted_datetime(v)


class DraftDetails(BaseModel):
    is_draftable: bool = Field(validation_alias="IsDisabledFromDrafting", default=True)
    salary: float | None = Field(validation_alias="s", default=None)
    starts_at: datetime | None = Field(validation_alias="dgst", default=None)

    @field_validator("is_draftable", mode="before")
    def transform_is_draftable(cls, v: bool) -> bool:
        return not v

    @field_validator("starts_at", mode="before")
    def transform_starts_at(cls, v: int | None) -> datetime | None:
        return from_unix_milliseconds_to_datetime(v) if v else None


class PlayerTeamSeries(BaseModel):
    away_team_id: int | None = Field(validation_alias="atid", default=None)
    home_team_id: int | None = Field(validation_alias="htid", default=None)
    opposition_rank: int | None = Field(validation_alias="or", default=None)
    team_series_id: int | None = Field(validation_alias="tsid", default=None)


class Position(BaseModel):
    id: int | None = Field(validation_alias="posid", default=None)
    name: str | None = Field(validation_alias="pn", default=None)


class ExceptionalMessageType(BaseModel):
    name: str | None = Field(validation_alias="Name", default=None)


class ExceptionalMessage(BaseModel):
    message: str | None = Field(validation_alias="Message", default=None)
    type_details: ExceptionalMessageType | None = Field(validation_alias="MessageType", default=None)
    priority_value: int | None = Field(validation_alias="Priority", default=None)


class Player(BaseModel):
    draft_details: DraftDetails | None = Field(validation_alias="draft_details", default=None)
    exceptional_messages: list[ExceptionalMessage] = Field(validation_alias="ExceptionalMessages")
    first_name: str | None = Field(validation_alias="fn", default=None)
    jersey_number: int | None = Field(validation_alias="jn", default=None)
    last_name: str | None = Field(validation_alias="ln", default=None)
    player_id: int | None = Field(validation_alias="pid", default=None)
    points_per_game: float | None = Field(validation_alias="ppg", default=None)
    position: Position | None = Field(validation_alias="position", default=None)
    team_id: int | None = Field(validation_alias="tid", default=None)
    team_series_details: PlayerTeamSeries | None = Field(validation_alias="team_series_details", default=None)

    @model_validator(mode="before")
    def set_entries(cls, data: dict) -> dict:
        collect(data, "draft_details", ["IsDisabledFromDrafting", "s", "dgst"])
        collect(data, "position", ["posid", "pn"])
        collect(data, "team_series_details", ["atid", "htid", "or", "tsid"])
        return data


class Players(BaseModel):
    players: list[Player] = Field(validation_alias="playerList", default=[])
    team_series: list[TeamSeries] = Field(validation_alias="teamList", default=[])

    @model_validator(mode="before")
    def transform(cls, data: dict) -> dict:
        ts: dict[int, dict] = data.pop("teamList", None)
        ttss: list[dict] = []
        for k, v in ts.items():
            v["team_series_id"] = k
            ttss.append(v)
        data["teamList"] = ttss
        return data
