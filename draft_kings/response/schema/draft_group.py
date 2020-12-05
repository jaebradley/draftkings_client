# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, EXCLUDE, post_load

from draft_kings.response.objects.draft_group import ContestType, League, Game, DraftGroup, DraftGroupResponse


class ContestTypeSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    contestTypeId = fields.Int(attribute="contest_type_id", missing=None)
    gameType = fields.Str(attribute="game_type", missing=None)

    @post_load
    def make_contest_type(self, data, **kwargs):
        return ContestType(**data)


class LeagueSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    leagueAbbreviation = fields.Str(attribute="league_abbreviation", missing=None)
    leagueId = fields.Int(attribute="league_id", missing=None)
    leagueName = fields.Str(attribute="league_name", missing=None)

    @post_load
    def make_league(self, data, **kwargs):
        return League(**data)


class GameSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    awayTeamId = fields.Int(attribute="away_team_id", missing=None)
    description = fields.Str(attribute="description", missing=None)
    gameId = fields.Int(attribute="game_id", missing=None)
    homeTeamId = fields.Int(attribute="home_team_id", missing=None)
    location = fields.Str(attribute="location", missing=None)
    name = fields.Str(attribute="name", missing=None)
    startDate = fields.AwareDateTime(attribute="start_date", missing=None)
    status = fields.Str(attribute="status", missing=None)

    @post_load
    def make_game(self, data, **kwargs):
        return Game(**data)


class DraftGroupSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    contestType = fields.Nested(ContestTypeSchema, attribute="contest_type", required=True)
    draftGroupId = fields.Int(attribute="draft_group_id", missing=None)
    draftGroupState = fields.Str(attribute="draft_group_state", missing=None)
    games = fields.List(fields.Nested(GameSchema, required=True), attribute="games", missing=[])
    leagues = fields.List(fields.Nested(LeagueSchema, required=True), attribute="leagues", missing=[])
    maxStartTime = fields.AwareDateTime(attribute="max_start_time", missing=None)
    minStartTime = fields.AwareDateTime(attribute="min_start_time", missing=None)
    sportId = fields.Int(attribute="sport_id", missing=None)
    startTimeType = fields.Str(attribute="start_time_type", missing=None)

    @post_load
    def make_draft_group(self, data, **kwargs):
        return DraftGroup(**data)


class DraftGroupResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    draftGroup = fields.Nested(DraftGroupSchema, attribute="draft_group", required=True)

    @post_load
    def make_draft_group_response(self, data, **kwargs):
        return DraftGroupResponse(**data)

# pylint: enable=unused-argument, no-self-use
