from marshmallow import Schema, fields, EXCLUDE, post_load

from draft_kings.response.objects.players import TeamSeries, PlayerDetails, PlayersDetails
from draft_kings.response.schema.fields import DictField


class TeamSeriesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    atid = fields.Integer(attribute="away_team_id", missing=None)
    htid = fields.Int(attribute="home_team_id", missing=None)
    status = fields.Str(attribute="status", missing=None)
    tz = fields.Str(attribute="starts_at", missing=None)
    wthr = fields.Str(attribute="weather", missing=None)

    @post_load
    def make_team_series(self, data, **kwargs):
        return TeamSeries(**data)


class PlayerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        include = {
            "or": fields.Integer(attribute="opposition_rank", missing=None)
        }

    atid = fields.Integer(attribute="away_team_id", missing=None)
    dgst = fields.Integer(attribute="draft_group_start_time", missing=None)
    ExceptionalMessages = fields.List(fields.Str, attribute="exceptional_messages")
    fn = fields.Str(attribute="first_name", missing=None)
    htid = fields.Int(attribute="home_team_id", missing=None)
    IsDisabledFromDrafting = fields.Bool(attribute="is_disabled_from_drafting", missing=None)
    jn = fields.Integer(attribute="jersey_number", missing=None)
    ln = fields.Str(attribute="last_name", missing=None)
    pid = fields.Integer(attribute="player_id", missing=None)
    pn = fields.Str(attribute="position_name", missing=None)
    posid = fields.Integer(attribute="position_id", missing=None)
    ppg = fields.Str(attribute="points_per_game", missing=None)
    s = fields.Float(attribute="salary", missing=None)
    tid = fields.Integer(attribute="team_id", missing=None)
    tsid = fields.Integer(attribute="team_series_id", missing=None)

    @post_load
    def make_player_detail(self, data, **kwargs):
        return PlayerDetails(**data)


class PlayersDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    playerList = fields.List(fields.Nested(PlayerSchema, missing={}), attribute="players", missing=[])
    teamList = DictField(fields.Str(required=True), fields.Nested(TeamSeriesSchema, missing={}), missing={},
                         attribute="team_series")

    @post_load
    def make_players_details(self, data, **kwargs):
        return PlayersDetails(**data)
