import datetime
from unittest import TestCase

import pytz

from draft_kings.client import available_players
from draft_kings.output.objects.players import Player, DraftDetails, PlayerPosition, \
    PlayerTeamSeriesDetails, TeamSeries


class TestNBAAvailablePlayers(TestCase):
    def setUp(self) -> None:
        self.result = available_players(draft_group_id=11513)

    def test_get_available_players(self):
        self.assertIsNotNone(self.result)

    def test_nba_multiple_players(self):
        self.assertEqual(len(self.result.players), 150)

    def test_nba_multiple_teams(self):
        self.assertEqual(len(self.result.team_series), 5)

    def test_nba_player_fields(self):
        self.assertEqual(
            Player(
                draft_details=DraftDetails(
                    exceptional_messages=[],
                    is_draftable=True,
                    salary=float(10300),
                    starts_at=datetime.datetime(2016, 11, 16, 0, 0, 0, tzinfo=pytz.UTC)
                ),
                first_name="LeBron",
                jersey_number=23,
                last_name="James",
                player_id=214152,
                points_per_game=55.7,
                position=PlayerPosition(
                    name="SF/PF",
                    position_id=27
                ),
                team_id=5,
                team_series=PlayerTeamSeriesDetails(
                    away_team_id=28,
                    home_team_id=5,
                    opposition_rank=15,
                    team_series_id=5479720
                )
            ),
            self.result.players[0]
        )

    def test_nba_team_series_fields(self):
        self.assertListEqual(
            [
                TeamSeries(
                    away_team_id=28,
                    home_team_id=5,
                    starts_at=datetime.datetime(2016, 11, 16, 0, 0, 0, tzinfo=pytz.UTC),
                    status="Final",
                    team_series_id=5479720,
                    weather_description=None
                ),
                TeamSeries(
                    away_team_id=4,
                    home_team_id=22,
                    starts_at=datetime.datetime(2016, 11, 16, 3, 0, 0, tzinfo=pytz.UTC),
                    status="Final",
                    team_series_id=5479968,
                    weather_description=None
                ),
                TeamSeries(
                   away_team_id=1,
                   home_team_id=14,
                   starts_at=datetime.datetime(2016, 11, 16, 0, 30, 0, tzinfo=pytz.UTC),
                   status="Final",
                   team_series_id=5479637,
                   weather_description=None
                ),
                TeamSeries(
                    away_team_id=5312,
                    home_team_id=16,
                    starts_at=datetime.datetime(2016, 11, 16, 1, 0, 0, tzinfo=pytz.UTC),
                    status="Final",
                    team_series_id=5479280,
                    weather_description=None
                ),
                TeamSeries(
                    away_team_id=17,
                    home_team_id=13,
                    starts_at=datetime.datetime(2016, 11, 16, 3, 30, 0, tzinfo=pytz.UTC),
                    status="Final",
                    team_series_id=5480294,
                    weather_description=None
                )
            ],
            self.result.team_series
        )


class TestLeagueOfLegendsAvailablePlayers(TestCase):
    def setUp(self) -> None:
        self.result = available_players(draft_group_id=26691)

    def test_get_available_players_league_of_legends(self):
        self.assertIsNotNone(self.result)

    def test_lol_multiple_players(self):
        self.assertEqual(28, len(self.result.players))

    def test_lol_multiple_teams(self):
        self.assertEqual(2, len(self.result.team_series))

    def test_lol_player_fields(self):
        self.assertEqual(
            Player(
                draft_details=DraftDetails(
                    exceptional_messages=[],
                    is_draftable=True,
                    salary=float(9000),
                    starts_at=datetime.datetime(2019, 5, 1, 9, 0, 0, tzinfo=pytz.UTC)
                ),
                first_name="",
                jersey_number=None,
                last_name="BigKoro",
                player_id=1283,
                points_per_game=float(0),
                position=PlayerPosition(
                    name="ADC",
                    position_id=155
                ),
                team_id=62492,
                team_series=PlayerTeamSeriesDetails(
                    away_team_id=62492,
                    home_team_id=156847,
                    opposition_rank=None,
                    team_series_id=5613734
                )
            ),
            self.result.players[0]
        )

    def test_lol_team_series_fields(self):
        self.assertListEqual(
            [
                TeamSeries(
                    away_team_id=62492,
                    home_team_id=156847,
                    starts_at=datetime.datetime(2019, 5, 1, 9, 0, 0, 0, tzinfo=pytz.UTC),
                    status="Final",
                    team_series_id=5613734,
                    weather_description=None
                ),
                TeamSeries(
                    away_team_id=58492,
                    home_team_id=45073,
                    starts_at=datetime.datetime(2019, 5, 1, 9, 55, 0, 0, tzinfo=pytz.UTC),
                    status="Final",
                    team_series_id=5613735,
                    weather_description=None
                )
            ],
            self.result.team_series
        )