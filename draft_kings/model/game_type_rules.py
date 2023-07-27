from pydantic import BaseModel, Field


class SalaryCap(BaseModel):
    is_enabled: bool | None = Field(validation_alias="isEnabled", default=None)
    maximum_value: float | None = Field(validation_alias="maxValue", default=None)
    minimum_value: float | None = Field(validation_alias="minValue", default=None)


class RosterSlot(BaseModel):
    description: str | None = Field(validation_alias="description", default=None)
    name: str | None = Field(validation_alias="name", default=None)
    roster_slot_id: int | None = Field(validation_alias="id", default=None)


class LineupTemplate(BaseModel):
    roster_slot_details: RosterSlot | None = Field(validation_alias="rosterSlot", default=None)


class GameTypeRules(BaseModel):
    allow_late_swap: bool | None = Field(validation_alias="allowLateSwap", default=None)
    description: str | None = Field(validation_alias="gameTypeDescription", default=None)
    enforce_selecting_unique_players: bool | None = Field(validation_alias="uniquePlayers", default=None)
    draft_type_name: str | None = Field(validation_alias="draftType", default=None)
    game_type_id: int | None = Field(validation_alias="gameTypeId", default=None)
    lineup_templates: list[LineupTemplate] = Field(validation_alias="lineupTemplate", default=[])
    name: str | None = Field(validation_alias="gameTypeName", default=None)
    salary_cap_details: SalaryCap | None = Field(validation_alias="salaryCap", default=None)
