import os
from datetime import datetime, timezone
from unittest import TestCase

from draft_kings import Sport
from draft_kings.model.draft_group import DraftGroup
from draft_kings.model.draft_group import League, Game
from tests.config import ROOT_DIRECTORY


class TestUpcomingGolfDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draft_group_details/26545_upcoming.json"), encoding="utf-8"
        ) as data_file:
            self.data: DraftGroup = DraftGroup.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_id(self):
        self.assertEqual(26545, self.data.draft_group_id)

    def test_draft_group_sport(self):
        self.assertEqual(Sport.GOLF, self.data.sport)

    def test_draft_group_start_time_type_description(self):
        self.assertEqual("Normal", self.data.start_time.type_description)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.start_time.minimum)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.start_time.maximum)

    def test_draft_group_state(self):
        self.assertEqual("Upcoming", self.data.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [League.model_construct(abbreviation="PGA", league_id=26, name="Professional Golf Association")],
            self.data.leagues,
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game.model_construct(
                    away_team_id=-5,
                    description="Wells Fargo Championship",
                    game_id=5559805,
                    home_team_id=-5,
                    location="Quail Hollow Club",
                    name="Wells Fargo Championship",
                    starts_at=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    status_description="Upcoming",
                )
            ],
            self.data.games,
        )


class TestHistoricalGolfDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draft_group_details/26545_historical.json"), encoding="utf-8"
        ) as data_file:
            self.data: DraftGroup = DraftGroup.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_id(self):
        self.assertEqual(26545, self.data.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(Sport.GOLF, self.data.sport)

    def test_draft_group_start_time_type_description(self):
        self.assertEqual("Normal", self.data.start_time.type_description)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.start_time.minimum)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc), self.data.start_time.maximum)

    def test_draft_group_state(self):
        self.assertEqual("Historical", self.data.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [League.model_construct(abbreviation="PGA", league_id=26, name="Professional Golf Association")],
            self.data.leagues,
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game.model_construct(
                    away_team_id=-5,
                    description="Wells Fargo Championship",
                    game_id=5559805,
                    home_team_id=-5,
                    location="Quail Hollow Club",
                    name="Wells Fargo Championship",
                    starts_at=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    status_description="ScoresOfficial",
                )
            ],
            self.data.games,
        )


class TestUpcomingNFLDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draft_group_details/41409_upcoming.json"), encoding="utf-8"
        ) as data_file:
            self.data: DraftGroup = DraftGroup.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_id(self):
        self.assertEqual(41409, self.data.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(Sport.NFL, self.data.sport)

    def test_draft_group_start_time_type(self):
        self.assertEqual("Normal", self.data.start_time.type_description)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.start_time.minimum)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.start_time.maximum)

    def test_draft_group_state(self):
        self.assertEqual("Upcoming", self.data.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [League.model_construct(abbreviation="NFL", league_id=1, name="National Football League")],
            self.data.leagues,
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game.model_construct(
                    away_team_id=347,
                    description="MIN @ CHI",
                    game_id=5673706,
                    home_team_id=326,
                    location="Soldier Field",
                    name=None,
                    starts_at=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    status_description="Pre-Game",
                )
            ],
            self.data.games,
        )


class TestHistoricalNFLDraftGroup(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draft_group_details/41409_historical.json"), encoding="utf-8"
        ) as data_file:
            self.data: DraftGroup = DraftGroup.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draft_group_id(self):
        self.assertEqual(41409, self.data.draft_group_id)

    def test_draft_group_sport_id(self):
        self.assertEqual(Sport.NFL, self.data.sport)

    def test_draft_group_start_time_type(self):
        self.assertEqual("Normal", self.data.start_time.type_description)

    def test_draft_group_min_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.start_time.minimum)

    def test_draft_group_max_start_time(self):
        self.assertEqual(datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc), self.data.start_time.maximum)

    def test_draft_group_state(self):
        self.assertEqual("Historical", self.data.draft_group_state)

    def test_draft_group_leagues(self):
        self.assertListEqual(
            [League.model_construct(abbreviation="NFL", league_id=1, name="National Football League")],
            self.data.leagues,
        )

    def test_draft_group_games(self):
        self.assertListEqual(
            [
                Game.model_construct(
                    away_team_id=347,
                    description="MIN @ CHI",
                    game_id=5673706,
                    home_team_id=326,
                    location="Soldier Field",
                    name=None,
                    starts_at=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    status_description="Final",
                )
            ],
            self.data.games,
        )
