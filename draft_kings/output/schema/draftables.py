# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from draft_kings.data import Sport
from draft_kings.output.objects.draftables import PlayerNameDetails, PlayerImageDetails, PlayerCompetitionDetails, \
    PlayerTeamDetails, PlayerDetails, CompetitionTeamDetails, CompetitionWeatherDetails, CompetitionDetails, \
    DraftablesDetails, PlayerDraftAlertDetails
from draft_kings.output.schema.fields import CustomAwareDateTime


class PlayerNameDetailsSchema(Schema):
    display = fields.Str(allow_none=True, required=True)
    first = fields.Str(allow_none=True, required=True)
    last = fields.Str(allow_none=True, required=True)
    short = fields.Str(allow_none=True, required=True)

    @post_load
    def make_player_name_details(self, data, **kwargs):
        return PlayerNameDetails(**data)


class PlayerImageDetailsSchema(Schema):
    fifty_pixels_by_fifty_pixels_url = fields.Str(allow_none=True, required=True)
    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url = fields.Str(allow_none=True, required=True)

    @post_load
    def make_player_image_details(self, data, **kwargs):
        return PlayerImageDetails(**data)


class PlayerCompetitionDetailsSchema(Schema):
    competition_id = fields.Int(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)
    starts_at = CustomAwareDateTime(allow_none=True, required=True)

    @post_load
    def make_player_competition_details(self, data, **kwargs):
        return PlayerCompetitionDetails(**data)


class PlayerTeamDetailsSchema(Schema):
    abbreviation = fields.Str(allow_none=True, required=True)
    team_id = fields.Int(allow_none=True, required=True)

    @post_load
    def make_player_team_details(self, data, **kwargs):
        return PlayerTeamDetails(**data)


class PlayerDraftAlertDetailsSchema(Schema):
    alert_description = fields.Str(allow_none=True, required=True)
    message = fields.Str(allow_none=True, required=True)
    priority_value = fields.Int(allow_none=True, required=True)
    updated_at = CustomAwareDateTime(allow_none=True, required=True)

    @post_load
    def make_player_draft_alert_details(self, data, **kwargs):
        return PlayerDraftAlertDetails(**data)


class PlayerDetailsSchema(Schema):
    competition_details = fields.Nested(PlayerCompetitionDetailsSchema, allow_none=True, required=True)
    draftable_id = fields.Int(allow_none=True, required=True)
    draft_alerts = fields.List(fields.Nested(PlayerDraftAlertDetailsSchema, required=True), required=True)
    image_details = fields.Nested(PlayerImageDetailsSchema, required=True)
    is_disabled = fields.Bool(allow_none=True, required=True)
    is_swappable = fields.Bool(allow_none=True, required=True)
    name_details = fields.Nested(PlayerNameDetailsSchema, required=True)
    news_status_description = fields.Str(allow_none=True, required=True)
    player_id = fields.Int(allow_none=True, required=True)
    position_name = fields.Str(allow_none=True, required=True)
    roster_slot_id = fields.Int(allow_none=True, required=True)
    salary = fields.Float(allow_none=True, required=True)
    team_details = fields.Nested(PlayerTeamDetailsSchema, required=True)

    @post_load
    def make_player_details(self, data, **kwargs):
        return PlayerDetails(**data)


class CompetitionTeamDetailsSchema(Schema):
    abbreviation = fields.Str(allow_none=True, required=True)
    city = fields.Str(allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)
    team_id = fields.Int(allow_none=True, required=True)

    @post_load
    def make_competition_team_details(self, data, **kwargs):
        return CompetitionTeamDetails(**data)


class CompetitionWeatherDetailsSchema(Schema):
    description = fields.Str(allow_none=True, required=True)
    is_in_a_dome = fields.Bool(allow_none=True, required=True)

    @post_load
    def make_competition_weather_details(self, data, **kwargs):
        return CompetitionWeatherDetails(**data)


class CompetitionDetailsSchema(Schema):
    are_depth_charts_available = fields.Bool(allow_none=True, required=True)
    are_starting_lineups_available = fields.Bool(allow_none=True, required=True)
    away_team = fields.Nested(CompetitionTeamDetailsSchema, allow_none=True, required=True)
    competition_id = fields.Int(allow_none=True, required=True)
    home_team = fields.Nested(CompetitionTeamDetailsSchema, allow_none=True, required=True)
    name = fields.Str(allow_none=True, required=True)
    sport = EnumField(Sport, by_value=True, allow_none=True, required=True)
    starts_at = CustomAwareDateTime(allow_none=True, required=True)
    state_description = fields.Str(allow_none=True, required=True)
    venue = fields.Str(allow_none=True, required=True)
    weather = fields.Nested(CompetitionWeatherDetailsSchema, allow_none=True, required=True)

    @post_load
    def make_competition_details(self, data, **kwargs):
        return CompetitionDetails(**data)


class DraftablesDetailsSchema(Schema):
    players = fields.List(fields.Nested(PlayerDetailsSchema, required=True), required=True)
    competitions = fields.List(fields.Nested(CompetitionDetailsSchema, required=True), required=True)

    @post_load
    def make_draftables_details(self, data, **kwargs):
        return DraftablesDetails(**data)

# pylint: enable=unused-argument, no-self-use
