from unittest import TestCase
import marshmallow
from datetime import datetime, timezone


from draft_kings.output.objects.draft_group import ContestDetails, StartTimeDetails, LeagueDetails, GameDetails, \
    DraftGroupDetails
from draft_kings.output.schema.draft_group import ContestDetailsSchema, StartTimeDetailsSchema, LeagueDetailsSchema, \
    GameDetailsSchema, DraftGroupDetailsSchema


class TestContestDetailsSerialization(TestCase):
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


class TestStartTimeDetailsSerialization(TestCase):
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
