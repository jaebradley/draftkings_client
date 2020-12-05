from datetime import datetime, timezone
from unittest import TestCase

import marshmallow

from draft_kings.data import Sport
from draft_kings.output.objects.draft_group import ContestDetails, StartTimeDetails, LeagueDetails, GameDetails, \
    DraftGroupDetails
from draft_kings.output.schema.draft_group import ContestDetailsSchema, StartTimeDetailsSchema, LeagueDetailsSchema, \
    GameDetailsSchema, DraftGroupDetailsSchema


class TestContestDetailsDeserialization(TestCase):
    def test_when_empty_object(self):
        self.assertRaises(
            marshmallow.ValidationError,
            ContestDetailsSchema().load,
            {}
        )

    def test_when_object_with_none_values(self):
        self.assertEqual(
            ContestDetails(game_type_description=None, type_id=None),
            ContestDetailsSchema().load({"game_type_description": None, "type_id": None})
        )

    def test_when_object_with_non_none_values(self):
        self.assertEqual(
            ContestDetails(game_type_description="jaebaebae", type_id=1),
            ContestDetailsSchema().load({"game_type_description": "jaebaebae", "type_id": 1})
        )

    def test_when_object_with_unparseable_type_id_value(self):
        self.assertRaises(
            marshmallow.ValidationError,
            ContestDetailsSchema().load,
            {"game_type_description": "jaebaebae", "type_id": "bae jadley"}
        )


class TestStartTimeDetailsDeserialization(TestCase):
    def test_when_empty_object(self):
        self.assertEqual(
            StartTimeDetails(maximum=None, minimum=None, type_description=None),
            StartTimeDetailsSchema().load({"maximum": None, "minimum": None, "type_description": None})
        )

    def test_when_object_with_non_none_values(self):
        maximum_start_time = datetime(2020, 11, 27, 0, 0, 0, tzinfo=timezone.utc)
        minimum_start_time = datetime(2020, 11, 26, 0, 0, 0, tzinfo=timezone.utc)

        self.assertEqual(
            StartTimeDetails(maximum=maximum_start_time, minimum=minimum_start_time, type_description="jaebaebae"),
            StartTimeDetailsSchema().load({
                "maximum": maximum_start_time,
                "minimum": minimum_start_time,
                "type_description": "jaebaebae"}
            )
        )

    def test_when_object_with_stringified_datetimes(self):
        maximum_start_time = datetime(2020, 11, 27, 0, 0, 0, tzinfo=timezone.utc)
        minimum_start_time = datetime(2020, 11, 26, 0, 0, 0, tzinfo=timezone.utc)

        self.assertEqual(
            StartTimeDetails(maximum=maximum_start_time, minimum=minimum_start_time, type_description="jaebaebae"),
            StartTimeDetailsSchema().load({
                "maximum": str(maximum_start_time),
                "minimum": str(minimum_start_time),
                "type_description": "jaebaebae"}
            )
        )

    def test_when_object_with__timezone_unaware_datetimes(self):
        maximum_start_time = datetime(2020, 11, 27, 0, 0, 0, tzinfo=None)
        minimum_start_time = datetime(2020, 11, 26, 0, 0, 0, tzinfo=None)

        self.assertRaises(
            marshmallow.ValidationError,
            StartTimeDetailsSchema().load,
            {
                "maximum": maximum_start_time,
                "minimum": minimum_start_time,
                "type_description": "jaebaebae"
            }
        )

    def test_when_object_with_stringified_timezone_unaware_datetimes(self):
        maximum_start_time = datetime(2020, 11, 27, 0, 0, 0, tzinfo=None)
        minimum_start_time = datetime(2020, 11, 26, 0, 0, 0, tzinfo=None)

        self.assertRaises(
            marshmallow.ValidationError,
            StartTimeDetailsSchema().load,
            {
                "maximum": str(maximum_start_time),
                "minimum": str(minimum_start_time),
                "type_description": "jaebaebae"
            }
        )


class TestLeagueDetailsDeserialization(TestCase):
    def setUp(self) -> None:
        self.schema = LeagueDetailsSchema()

    def test_raises_for_missing_abbreviation(self):
        self.assertRaises(marshmallow.ValidationError, self.schema.load, {"league_id": None, "name": None})

    def test_raises_for_missing_league_id(self):
        self.assertRaises(marshmallow.ValidationError, self.schema.load, {"abbreviation": None, "name": None})

    def test_raises_for_missing_name(self):
        self.assertRaises(marshmallow.ValidationError, self.schema.load, {"abbreviation": None, "league_id": None})

    def test_none_values(self):
        self.assertEqual(LeagueDetails(abbreviation=None, league_id=None, name=None),
                         self.schema.load({"abbreviation": None, "league_id": None, "name": None}))

    def test_non_none_values(self):
        self.assertEqual(LeagueDetails(abbreviation="jb", league_id=1, name="jaebaebae"),
                         self.schema.load({"abbreviation": "jb", "league_id": 1, "name": "jaebaebae"}))


class TestGameDetailsDeserialization(TestCase):
    def setUp(self) -> None:
        self.schema = GameDetailsSchema()

    def test_none_values(self):
        self.assertEqual(
            GameDetails(
                away_team_id=None,
                description=None,
                game_id=None,
                home_team_id=None,
                location=None,
                name=None,
                starts_at=None,
                status_description=None
            ),
            self.schema.load({
                "away_team_id": None,
                "description": None,
                "game_id": None,
                "home_team_id": None,
                "location": None,
                "name": None,
                "starts_at": None,
                "status_description": None
            })
        )

    def test_non_none_values(self):
        self.assertEqual(
            GameDetails(
                away_team_id=1,
                description="some description",
                game_id=2,
                home_team_id=3,
                location="some location",
                name="some name",
                starts_at=datetime(2020, 12, 2, 0, 0, 0, 0, tzinfo=timezone.utc),
                status_description="some status description"
            ),
            self.schema.load({
                "away_team_id": 1,
                "description": "some description",
                "game_id": 2,
                "home_team_id": 3,
                "location": "some location",
                "name": "some name",
                "starts_at": datetime(2020, 12, 2, 0, 0, 0, 0, tzinfo=timezone.utc),
                "status_description": "some status description"
            })
        )


class TestDraftGroupDetailsDeserialization(TestCase):
    def setUp(self) -> None:
        self.schema = DraftGroupDetailsSchema()

    def test_null_contest_details_raises_validation_error(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {
                "contest_details": None,
                "draft_group_id": 1,
                "games": [],
                "leagues": [],
                "sport": Sport.NBA,
                "start_time_details": StartTimeDetails(
                    maximum=datetime(2020, 11, 27, 0, 0, 0, tzinfo=None),
                    minimum=datetime(2020, 11, 26, 0, 0, 0, tzinfo=None),
                    type_description="jaebaebae"
                ),
                "state_description": "some state description"
            }
        )

    def test_null_start_time_details_raises_validation_error(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {
                "contest_details": ContestDetails(game_type_description="jaebaebae", type_id=1),
                "draft_group_id": 1,
                "games": [],
                "leagues": [],
                "sport": Sport.NBA,
                "start_time_details": StartTimeDetails(
                    maximum=datetime(2020, 11, 27, 0, 0, 0, tzinfo=None),
                    minimum=datetime(2020, 11, 26, 0, 0, 0, tzinfo=None),
                    type_description="jaebaebae"
                ),
                "state_description": "some state description"
            }
        )

    def test_non_null_empty_list_values(self):
        self.assertEqual(
            DraftGroupDetails(
                contest_details=ContestDetails(
                    game_type_description="jaebaebae",
                    type_id=1
                ),
                draft_group_id=1,
                games=[
                    GameDetails(
                        away_team_id=1,
                        description="some game description",
                        game_id=2,
                        home_team_id=3,
                        location="some location",
                        name="some name",
                        starts_at=datetime(2020, 12, 2, 0, 0, 0, tzinfo=timezone.utc),
                        status_description="some status description"
                    )
                ],
                leagues=[
                    LeagueDetails(
                        abbreviation="some abbreviation",
                        league_id=1,
                        name="some name"
                    )
                ],
                sport=Sport.NBA,
                start_time_details=StartTimeDetails(
                    maximum=datetime(2020, 11, 27, 0, 0, 0, tzinfo=timezone.utc),
                    minimum=datetime(2020, 11, 26, 0, 0, 0, tzinfo=timezone.utc),
                    type_description="jaebaebae"
                ),
                state_description="some state description"
            ),
            self.schema.load({
                "contest_details": {"game_type_description": "jaebaebae", "type_id": 1},
                "draft_group_id": 1,
                "games": [
                    {
                        "away_team_id": 1,
                        "description": "some game description",
                        "game_id": 2,
                        "home_team_id": 3,
                        "location": "some location",
                        "name": "some name",
                        "starts_at": datetime(2020, 12, 2, 0, 0, 0, tzinfo=timezone.utc),
                        "status_description": "some status description"
                    }
                ],
                "leagues": [
                    {
                        "abbreviation": "some abbreviation",
                        "league_id": 1,
                        "name": "some name"
                    }
                ],
                "sport": Sport.NBA,
                "start_time_details": {
                    "maximum": datetime(2020, 11, 27, 0, 0, 0, tzinfo=timezone.utc),
                    "minimum": datetime(2020, 11, 26, 0, 0, 0, tzinfo=timezone.utc),
                    "type_description": "jaebaebae"
                },
                "state_description": "some state description"
            })
        )
