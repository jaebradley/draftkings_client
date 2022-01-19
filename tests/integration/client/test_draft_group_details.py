import os
from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.draft_group import LeagueDetails, GameDetails, ContestDetails, \
    StartTimeDetails
from tests.config import ROOT_DIRECTORY


class TestDraftGroupDetails(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_nba_draft_group_details(self):
        # Draft Group from 2016-11-16
        details = self.client.draft_group_details(draft_group_id=11513)
        self.assertIsNotNone(details)

    def test_nhl_draft_group_details(self):
        # Draft Group for 2018-11-20
        details = self.client.draft_group_details(draft_group_id=22953)
        self.assertIsNotNone(details)

    def test_nfl_draft_group_details(self):
        # Draft Group for 2018-11-20 MNF
        details = self.client.draft_group_details(draft_group_id=22927)
        self.assertIsNotNone(details)

    def test_cfb_draft_group_details(self):
        # Draft Group for 2018-11-24
        details = self.client.draft_group_details(draft_group_id=22952)
        self.assertIsNotNone(details)

    def test_cbb_draft_group_details(self):
        # Draft Group for 2018-11-19
        details = self.client.draft_group_details(draft_group_id=22958)
        self.assertIsNotNone(details)

    def test_soccer_uefa_national_league_draft_group_details(self):
        # Draft Group for 2018-11-19
        details = self.client.draft_group_details(draft_group_id=22855)
        self.assertIsNotNone(details)

    def test_soccer_epl_draft_group_details(self):
        # Start Date is 2018-11-24T15:00:00.0000000Z
        details = self.client.draft_group_details(draft_group_id=22831)
        self.assertIsNotNone(details)

    def test_euroleague_draft_group_details(self):
        # Start Date is 2018-11-20T17:00:00.0000000Z
        details = self.client.draft_group_details(draft_group_id=22916)
        self.assertIsNotNone(details)


class TestDraftGroup11513MockedHTTPResponse(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, "tests/files/draft_group_details/11513.json"),
                encoding="utf-8"
        ) as data_file:
            self.response_data = data_file.read()
            patched_method = patch.object(HTTPClient, "draft_group_details")
            mocked_draft_group_details = patched_method.start()
            mocked_draft_group_details.return_value = Mock(text=self.response_data)
            self.result = Client().draft_group_details(draft_group_id=11513)

    def tearDown(self) -> None:
        patch.stopall()

    def test_draft_group_details_are_not_none(self):
        self.assertIsNotNone(self.result)

    def test_league_details(self):
        self.assertListEqual(
            [
                LeagueDetails(
                    league_id=4,
                    name="National Basketball Association",
                    abbreviation="NBA"
                )
            ],
            self.result.leagues
        )

    def test_games_are_not_none(self):
        self.assertIsNotNone(self.result.games)

    def test_five_games(self):
        self.assertListEqual(
            [
                GameDetails(
                    away_team_id=5312,
                    description="CHA @ MIN",
                    game_id=5479280,
                    home_team_id=16,
                    location="Target Center",
                    name=None,
                    starts_at=datetime(2016, 11, 16, 1, 0, 0, 0, tzinfo=timezone.utc),
                    status_description="ScoresOfficial"
                ),
                GameDetails(
                    away_team_id=1,
                    description="ATL @ MIA",
                    game_id=5479637,
                    home_team_id=14,
                    location="AmericanAirlines Arena",
                    name=None,
                    starts_at=datetime(2016, 11, 16, 0, 30, 0, 0, tzinfo=timezone.utc),
                    status_description="ScoresOfficial"
                ),
                GameDetails(
                    away_team_id=28,
                    description="TOR @ CLE",
                    game_id=5479720,
                    home_team_id=5,
                    location="Quicken Loans Arena",
                    name=None,
                    starts_at=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc),
                    status_description="ScoresOfficial"
                ),
                GameDetails(
                    away_team_id=4,
                    description="CHI @ POR",
                    game_id=5479968,
                    home_team_id=22,
                    location="Moda Center at the Rose Quarter",
                    name=None,
                    starts_at=datetime(2016, 11, 16, 3, 0, 0, 0, tzinfo=timezone.utc),
                    status_description="ScoresOfficial"
                ),
                GameDetails(
                    away_team_id=17,
                    description="BKN @ LAL",
                    game_id=5480294,
                    home_team_id=13,
                    location="Staples Center",
                    name=None,
                    starts_at=datetime(2016, 11, 16, 3, 30, 0, 0, tzinfo=timezone.utc),
                    status_description="ScoresOfficial"
                ),
            ],
            self.result.games
        )

    def test_contest_details_values(self):
        self.assertEqual(
            ContestDetails(
                game_type_description="SalaryCap",
                type_id=5,
            ),
            self.result.contest_details
        )

    def test_start_time_details(self):
        self.assertEqual(
            StartTimeDetails(
                maximum=datetime(2016, 11, 16, 3, 30, 0, 0, tzinfo=timezone.utc),
                minimum=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc),
                type_description="Normal"
            ),
            self.result.start_time_details
        )

    def test_draft_group_id(self):
        self.assertEqual(11513, self.result.draft_group_id)

    def test_sport(self):
        self.assertEqual(Sport.NBA, self.result.sport)

    def test_state(self):
        self.assertEqual("Historical", self.result.state_description)
