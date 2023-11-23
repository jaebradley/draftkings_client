from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator

from draft_kings.data import Sport
from draft_kings.utilities import collect, transform_sport_abbreviation


class Name(BaseModel):
    display: str | None = Field(validation_alias="displayName", default=None)
    first: str | None = Field(validation_alias="firstName", default=None)
    last: str | None = Field(validation_alias="lastName", default=None)
    short: str | None = Field(validation_alias="shortName", default=None)


class Image(BaseModel):
    player_image_50: str | None = Field(validation_alias="playerImage50", default=None)
    player_image_160: str | None = Field(validation_alias="playerImage160", default=None)


class PlayerCompetitionDetails(BaseModel):
    competition_id: int | None = Field(validation_alias="competitionId", default=None)
    name: str | None = Field(validation_alias="name", default=None)
    start_time: datetime | None = Field(validation_alias="startTime", default=None)


class Team(BaseModel):
    abbreviation: str | None = Field(validation_alias="teamAbbreviation", default=None)
    team_id: int | None = Field(validation_alias="teamId", default=None)


class DraftAlert(BaseModel):
    alert_description: str | None = Field(validation_alias="alertType", default=None)
    message: str | None = Field(validation_alias="message", default=None)
    priority_value: int | None = Field(validation_alias="priority", default=None)
    updated_at: datetime | None = Field(validation_alias="updatedDate", default=None)


class Player(BaseModel):
    competition_details: PlayerCompetitionDetails | None = Field(validation_alias="competition", default=None)
    draftable_id: int | None = Field(validation_alias="draftableId", default=None)
    draft_alerts: list[DraftAlert] = Field(validation_alias="draftAlerts", default=[])
    image: Image | None = Field(validation_alias="image", default=None)
    is_disabled: bool | None = Field(validation_alias="isDisabled", default=None)
    is_swappable: bool | None = Field(validation_alias="isSwappable", default=None)
    name: Name | None = Field(validation_alias="name", default=None)
    news_status_description: str | None = Field(validation_alias="newsStatus", default=None)
    player_id: int | None = Field(validation_alias="playerId", default=None)
    position_name: str | None = Field(validation_alias="position", default=None)
    roster_slot_id: int | None = Field(validation_alias="rosterSlotId", default=None)
    salary: float | None = Field(validation_alias="salary", default=None)
    team: Team | None = Field(validation_alias="team", default=None)

    @model_validator(mode="before")
    def set_data(cls, data: dict) -> dict:
        collect(data, "image", ["playerImage50", "playerImage160"])
        collect(data, "name", ["displayName", "firstName", "lastName", "shortName"])
        collect(data, "team", ["teamAbbreviation", "teamId"])
        return data


class CompetitionTeam(BaseModel):
    abbreviation: str | None = Field(validation_alias="abbreviation", default=None)
    city: str | None = Field(validation_alias="city", default=None)
    name: str | None = Field(validation_alias="teamName", default=None)
    team_id: int | None = Field(validation_alias="teamId", default=None)


class CompetitionWeather(BaseModel):
    description: str | None = Field(validation_alias="icon", default=None)
    is_in_a_dome: bool | None = Field(validation_alias="isDome", default=None)


class Competition(BaseModel):
    are_depth_charts_available: bool | None = Field(validation_alias="depthChartsAvailable", default=None)
    are_starting_lineups_available: bool | None = Field(validation_alias="startingLineupsAvailable", default=None)
    away_team: CompetitionTeam | None = Field(validation_alias="awayTeam", default=None)
    competition_id: int | None = Field(validation_alias="competitionId", default=None)
    home_team: CompetitionTeam | None = Field(validation_alias="homeTeam", default=None)
    name: str | None = Field(validation_alias="name", default=None)
    sport: Sport | None = Field(validation_alias="sport", default=None)
    starts_at: datetime | None = Field(validation_alias="startTime", default=None)  #
    state_description: str | None = Field(validation_alias="competitionState", default=None)
    venue: str | None = Field(validation_alias="venue", default=None)
    weather: CompetitionWeather | None = Field(validation_alias="weather", default=None)  #

    @field_validator("sport", mode="before")
    def transform_sport_abbreviation(cls, v: str) -> Sport | None:
        return transform_sport_abbreviation(v)


class Draftables(BaseModel):
    competitions: list[Competition] = Field(validation_alias="competitions", default=[])
    players: list[Player] = Field(validation_alias="draftables", default=[])
