from datetime import datetime, timezone
from unittest import TestCase

import marshmallow

from draft_kings.output.objects.draft_group import StartTimeDetails
from draft_kings.output.schema.draft_group import StartTimeDetailsSchema


class TestStartTimeDetailsSerialization(TestCase):
    def test_when_none_values(self):
        self.assertEqual(
            {"maximum": None, "minimum": None, "type_description": None},
            StartTimeDetailsSchema().dump(StartTimeDetails(maximum=None, minimum=None, type_description=None))
        )

    def test_when_empty_object(self):
        self.assertEqual(
            {},
            StartTimeDetailsSchema().dump({})
        )

    def test_when_timezone_aware_datetime_objects(self):
        maximum_start_time = datetime(2020, 11, 27, 0, 0, 0, tzinfo=timezone.utc)
        minimum_start_time = datetime(2020, 11, 26, 0, 0, 0, tzinfo=timezone.utc)

        self.assertDictEqual(
            {
                "maximum": maximum_start_time.isoformat(),
                "minimum": minimum_start_time.isoformat(),
                "type_description": "jaebaebae"
            },
            StartTimeDetailsSchema().dump(StartTimeDetails(maximum=maximum_start_time, minimum=minimum_start_time,
                                                           type_description="jaebaebae"))
        )

    def test_when_non_timezone_aware_datetime_objects(self):
        maximum_start_time = datetime(2020, 11, 27, 0, 0, 0, tzinfo=None)
        minimum_start_time = datetime(2020, 11, 26, 0, 0, 0, tzinfo=None)

        self.assertRaises(
            marshmallow.ValidationError,
            StartTimeDetailsSchema().dump,
            StartTimeDetails(maximum=maximum_start_time, minimum=minimum_start_time, type_description="jaebaebae")
        )
