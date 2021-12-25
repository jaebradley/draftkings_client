import os
from datetime import datetime, timezone
from unittest import TestCase

from draft_kings.response.objects.draft_group import League, Game
from draft_kings.response.schema.draft_group import DraftGroupResponseSchema
from tests.config import ROOT_DIRECTORY


class TestUpcomingGolfDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/26545_upcoming.json'),
                  encoding="utf-8"
                  ) as data_file:
            self.schema = DraftGroupResponseSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_exists(self):
        self.assertIsNotNone(self.data.draft_group)

    def test_draft_group_id(self):
        self.assertEqual(26545, self.data.draft_group.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(13, self.data.draft_group.sport_id)

    def test_draft_group_start_time_type(self):
        self.assertEqual("Normal", self.data.draft_group.start_time_type)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.draft_group.max_start_time)

    def test_draft_group_state(self):
        self.assertEqual("Upcoming", self.data.draft_group.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [
                League(
                    league_abbreviation="PGA",
                    league_id=26,
                    league_name="Professional Golf Association"
                )
            ],
            self.data.draft_group.leagues
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game(
                    away_team_id=-5,
                    description="Wells Fargo Championship",
                    game_id=5559805,
                    home_team_id=-5,
                    location="Quail Hollow Club",
                    name="Wells Fargo Championship",
                    start_date=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    status="Upcoming"
                )
            ],
            self.data.draft_group.games
        )


class TestHistoricalGolfDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/26545_historical.json'),
                  encoding="utf-8") as \
                data_file:
            self.schema = DraftGroupResponseSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_exists(self):
        self.assertIsNotNone(self.data.draft_group)

    def test_draft_group_id(self):
        self.assertEqual(26545, self.data.draft_group.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(13, self.data.draft_group.sport_id)

    def test_draft_group_start_time_type(self):
        self.assertEqual("Normal", self.data.draft_group.start_time_type)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.draft_group.max_start_time)

    def test_draft_group_state(self):
        self.assertEqual("Historical", self.data.draft_group.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [
                League(
                    league_abbreviation="PGA",
                    league_id=26,
                    league_name="Professional Golf Association"
                )
            ],
            self.data.draft_group.leagues
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game(
                    away_team_id=-5,
                    description="Wells Fargo Championship",
                    game_id=5559805,
                    home_team_id=-5,
                    location="Quail Hollow Club",
                    name="Wells Fargo Championship",
                    start_date=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    status="ScoresOfficial"
                )
            ],
            self.data.draft_group.games
        )


class TestUpcomingNFLDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/41409_upcoming.json'),
                  encoding="utf-8") as \
                data_file:
            self.schema = DraftGroupResponseSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_exists(self):
        self.assertIsNotNone(self.data.draft_group)

    def test_draft_group_id(self):
        self.assertEqual(41409, self.data.draft_group.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(1, self.data.draft_group.sport_id)

    def test_draft_group_start_time_type(self):
        self.assertEqual("Normal", self.data.draft_group.start_time_type)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.draft_group.max_start_time)

    def test_draft_group_state(self):
        self.assertEqual("Upcoming", self.data.draft_group.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [
                League(
                    league_abbreviation="NFL",
                    league_id=1,
                    league_name="National Football League"
                )
            ],
            self.data.draft_group.leagues
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game(
                    away_team_id=347,
                    description="MIN @ CHI",
                    game_id=5673706,
                    home_team_id=326,
                    location="Soldier Field",
                    name=None,
                    start_date=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    status="Pre-Game"
                )
            ],
            self.data.draft_group.games
        )


class TestHistoricalNFLDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/41409_historical.json'),
                  encoding="utf-8") \
                as data_file:
            self.schema = DraftGroupResponseSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_exists(self):
        self.assertIsNotNone(self.data.draft_group)

    def test_draft_group_id(self):
        self.assertEqual(41409, self.data.draft_group.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(1, self.data.draft_group.sport_id)

    def test_draft_group_start_time_type(self):
        self.assertEqual("Normal", self.data.draft_group.start_time_type)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.draft_group.max_start_time)

    def test_draft_group_state(self):
        self.assertEqual("Historical", self.data.draft_group.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [
                League(
                    league_abbreviation="NFL",
                    league_id=1,
                    league_name="National Football League"
                )
            ],
            self.data.draft_group.leagues
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game(
                    away_team_id=347,
                    description="MIN @ CHI",
                    game_id=5673706,
                    home_team_id=326,
                    location="Soldier Field",
                    name=None,
                    start_date=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    status="Final"
                )
            ],
            self.data.draft_group.games
        )
