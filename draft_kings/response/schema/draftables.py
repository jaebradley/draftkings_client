# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, EXCLUDE, post_load

from draft_kings.response.objects.draftables import Draftables, Competition, Player, PlayerCompetitionDetails, \
    CompetitionWeather, CompetitionTeam, DraftAlert


class PlayerCompetitionDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    competitionId = fields.Int(attribute="competition_id", missing=None)
    name = fields.Str(attribute="name", missing=None)
    startTime = fields.AwareDateTime(attribute="start_time", missing=None)

    @post_load
    def make_player_competition(self, data, **kwargs):
        return PlayerCompetitionDetails(**data)


class PlayerDraftAlertSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    alertType = fields.Str(attribute="alert_type", missing=None)
    message = fields.Str(attribute="message", missing=None)
    updatedDate = fields.AwareDateTime(attribute="updated_date", missing=None)
    priority = fields.Int(attribute="priority", missing=None)

    @post_load
    def make_player_draft_alert(self, data, **kwargs):
        return DraftAlert(**data)


class PlayerSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    competition = fields.Nested(PlayerCompetitionDetailsSchema, attribute="competition", missing=None)
    displayName = fields.Str(attribute="display_name", missing=None)
    draftableId = fields.Int(attribute="draftable_id", missing=None)
    draftAlerts = fields.List(fields.Nested(PlayerDraftAlertSchema), attribute="draft_alerts", missing=[])
    firstName = fields.Str(attribute="first_name", missing=None)
    isDisabled = fields.Bool(attribute="is_disabled", missing=None)
    isSwappable = fields.Bool(attribute="is_swappable", missing=None)
    lastName = fields.Str(attribute="last_name", missing=None)
    newsStatus = fields.Str(attribute="news_status", missing=None)
    playerId = fields.Int(attribute="player_id", missing=None)
    playerImage50 = fields.Str(attribute="player_image_50", missing=None)
    playerImage160 = fields.Str(attribute="player_image_160", missing=None)
    position = fields.Str(attribute="position", missing=None)
    rosterSlotId = fields.Int(attribute="roster_slot_id", missing=None)
    salary = fields.Float(attribute="salary", missing=None)
    shortName = fields.Str(attribute="short_name", missing=None)
    teamAbbreviation = fields.Str(attribute="team_abbreviation", missing=None)
    teamId = fields.Int(attribute="team_id", missing=None)

    @post_load
    def make_player(self, data, **kwargs):
        return Player(**data)


class CompetitionTeamSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    abbreviation = fields.Str(attribute="abbreviation", missing=None)
    city = fields.Str(attribute="city", missing=None)
    teamId = fields.Int(attribute="team_id", missing=None)
    teamName = fields.Str(attribute="team_name", missing=None)

    @post_load
    def make_competition(self, data, **kwargs):
        return CompetitionTeam(**data)


class CompetitionWeatherSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    icon = fields.Str(attribute="icon", missing=None)
    isDome = fields.Bool(attribute="is_dome", missing=None)

    @post_load
    def make_competition_weather(self, data, **kwargs):
        return CompetitionWeather(**data)


class CompetitionSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    awayTeam = fields.Nested(CompetitionTeamSchema, attribute="away_team", missing=None)
    competitionId = fields.Int(attribute="competition_id", missing=None)
    competitionState = fields.Str(attribute="competition_state", missing=None)
    depthChartsAvailable = fields.Bool(attribute="are_depth_charts_available", missing=None)
    homeTeam = fields.Nested(CompetitionTeamSchema, attribute="home_team", missing=None)
    name = fields.Str(attribute="name", missing=None)
    sport = fields.Str(attribute="sport", missing=None)
    startingLineupsAvailable = fields.Bool(attribute="are_starting_lineups_available", missing=None)
    startTime = fields.AwareDateTime(attribute="start_time", missing=None)
    venue = fields.Str(attribute="venue", missing=None)
    weather = fields.Nested(CompetitionWeatherSchema, attribute="weather", missing=None)

    @post_load
    def make_competition(self, data, **kwargs):
        return Competition(**data)


class DraftablesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    draftables = fields.List(fields.Nested(PlayerSchema), attribute="draftables", missing=[])
    competitions = fields.List(fields.Nested(CompetitionSchema), attribute="competitions", missing=[])

    @post_load
    def make_draftables(self, data, **kwargs):
        return Draftables(**data)

# pylint: enable=unused-argument, no-self-use
