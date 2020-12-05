# pylint: disable=unused-argument, no-self-use

from marshmallow import Schema, fields, EXCLUDE, post_load

from draft_kings.response.objects.players import TeamSeries, Player, PlayersDetails, ExceptionalMessage, \
    ExceptionalMessageType
from draft_kings.response.schema.fields import DictField


class TeamSeriesSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    atid = fields.Int(attribute="away_team_id", missing=None)
    htid = fields.Int(attribute="home_team_id", missing=None)
    status = fields.Str(attribute="status", missing=None)
    tz = fields.Str(attribute="starts_at", missing=None)
    wthr = fields.Str(attribute="weather", missing=None)

    @post_load
    def make_team_series(self, data, **kwargs):
        return TeamSeries(**data)


class ExceptionalMessageTypeSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    Name = fields.Str(attribute="name", missing=None)

    @post_load
    def make_exceptional_message_type(self, data, **kwargs):
        return ExceptionalMessageType(**data)


class ExceptionalMessageSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    Message = fields.Str(attribute="message", missing=None)
    MessageType = fields.Nested(ExceptionalMessageTypeSchema, attribute="message_type", missing=None)
    Priority = fields.Int(attribute="priority", missing=None)

    @post_load
    def make_exceptional_message(self, data, **kwargs):
        return ExceptionalMessage(**data)


class PlayerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        include = {
            "or": fields.Integer(attribute="opposition_rank", missing=None)
        }

    atid = fields.Integer(attribute="away_team_id", missing=None)
    dgst = fields.Integer(attribute="draft_group_start_time", missing=None)
    ExceptionalMessages = fields.List(
        fields.Nested(ExceptionalMessageSchema),
        attribute="exceptional_messages",
        missing=None
    )
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
        return Player(**data)


class PlayersDetailsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    playerList = fields.List(fields.Nested(PlayerSchema), attribute="players", missing=[])
    teamList = DictField(
        fields.Str(required=True),
        fields.Nested(TeamSeriesSchema, required=True),
        attribute="team_series",
        missing=None,
    )

    @post_load
    def make_players_details(self, data, **kwargs):
        return PlayersDetails(**data)

# pylint: enable=unused-argument, no-self-use
