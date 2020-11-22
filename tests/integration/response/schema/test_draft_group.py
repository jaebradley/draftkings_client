import os
from unittest import TestCase

from draft_kings.response.objects.draft_group import League, Game
from draft_kings.response.schema.draft_group import DraftGroupResponseSchema
from tests.config import ROOT_DIRECTORY


class TestUpcomingGolfDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/upcoming_golf_draft_group_response.json')) as data_file:
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
        self.assertEqual("2019-05-02T11:00:00.0000000Z", self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual("2019-05-02T11:00:00.0000000Z", self.data.draft_group.max_start_time)

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
                    start_date="2019-05-02T11:00:00.0000000Z",
                    status="Upcoming"
                )
            ],
            self.data.draft_group.games
        )


class TestHistoricalGolfDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/historical_golf_draft_group_response.json')) as \
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
        self.assertEqual("2019-05-02T11:00:00.0000000Z", self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual("2019-05-02T11:00:00.0000000Z", self.data.draft_group.max_start_time)

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
                    start_date="2019-05-02T11:00:00.0000000Z",
                    status="ScoresOfficial"
                )
            ],
            self.data.draft_group.games
        )


class TestUpcomingNFLDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/upcoming_monday_night_nfl_game_draft_group.json')) as \
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
        self.assertEqual("2020-11-17T01:15:00.0000000Z", self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual("2020-11-17T01:15:00.0000000Z", self.data.draft_group.max_start_time)

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
                    start_date="2020-11-17T01:15:00.0000000Z",
                    status="Pre-Game"
                )
            ],
            self.data.draft_group.games
        )


class TestHistoricalNFLDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY,
                               'tests/files/draft_group_details/historical_monday_night_nfl_game_draft_group.json')) \
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
        self.assertEqual("2020-11-17T01:15:00.0000000Z", self.data.draft_group.min_start_time)

    def test_draft_group_max_start_time(self):
        self.assertEqual("2020-11-17T01:15:00.0000000Z", self.data.draft_group.max_start_time)

    def test_draft_group_state(self):
        self.assertEqual("Finalized", self.data.draft_group.draft_group_state)

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
                    start_date="2020-11-17T01:15:00.0000000Z",
                    status="Final"
                )
            ],
            self.data.draft_group.games
        )
