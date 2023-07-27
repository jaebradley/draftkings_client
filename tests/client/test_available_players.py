import datetime
import os
from unittest import TestCase, skip
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.http_client import HTTPClient
from draft_kings.model.players import (
    Player,
    DraftDetails,
    Position,
    PlayerTeamSeries,
    TeamSeries,
    ExceptionalMessage,
    ExceptionalMessageType,
)
from tests.config import ROOT_DIRECTORY


# @skip(reason="draftkings seems to deprecate draft groups after a couple weeks")
class TestNBAAvailablePlayers(TestCase):
    def setUp(self) -> None:
        self.result = Client().available_players(draft_group_id=42463)

    def test_get_available_players(self):
        self.assertIsNotNone(self.result)

    def test_nba_multiple_players(self):
        self.assertEqual(len(self.result.players), 75)

    def test_nba_multiple_teams(self):
        self.assertEqual(len(self.result.team_series), 2)

    # @skip(reason="current season fields change")
    def test_nba_player_fields(self):
        self.assertEqual(
            Player.model_construct(
                draft_details=DraftDetails.model_construct(is_draftable=True, salary=float(10000), starts_at=None),
                exceptional_messages=[],
                first_name="Anthony",
                jersey_number=3,
                last_name="Davis",
                player_id=603096,
                points_per_game=52.3,
                position=Position.model_construct(name="PF/C", id=28),
                team_id=13,
                team_series_details=PlayerTeamSeries.model_construct(
                    away_team_id=12, home_team_id=13, opposition_rank=23, team_series_id=5713406
                ),
            ),
            self.result.players[0],
        )

    # @skip(reason="current season fields change")
    def test_nba_team_series_fields(self):
        self.assertListEqual(
            [
                TeamSeries.model_construct(
                    away_team_id=12,
                    home_team_id=13,
                    starts_at=datetime.datetime(2020, 12, 23, 3, 0, 0, tzinfo=datetime.timezone.utc),
                    status_description="Final",
                    team_series_id=5713406,
                    weather=None,
                ),
                TeamSeries.model_construct(
                    away_team_id=9,
                    home_team_id=17,
                    starts_at=datetime.datetime(2020, 12, 23, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    status_description="Final",
                    team_series_id=5713400,
                    weather=None,
                ),
            ],
            self.result.team_series,
        )


class TestPlayersWithExceptionalMessages(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/available_players/41793.json"), encoding="utf-8"
        ) as data_file:
            self.response_data = data_file.read()
            patched_method = patch.object(HTTPClient, "available_players")
            mocked_method = patched_method.start()
            mocked_method.return_value = Mock(text=self.response_data)
            self.result = Client().available_players(draft_group_id=41793)

    def test_exceptional_messages(self):
        self.assertListEqual(
            [
                ExceptionalMessage.model_construct(
                    message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points "
                    "in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                    priority_value=100,
                    type_details=ExceptionalMessageType.model_construct(name="player"),
                )
            ],
            self.result.players[3].exceptional_messages,
        )
