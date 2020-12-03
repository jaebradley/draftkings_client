from datetime import datetime, timezone
from unittest import TestCase

import marshmallow

from draft_kings.output.schema.fields import CustomAwareDateTime, CustomDateTime


class TestCustomAwareDateTimeSerialization(TestCase):
    class TestSchema(marshmallow.Schema):
        timestamp = CustomAwareDateTime()

    def setUp(self) -> None:
        self.schema = TestCustomAwareDateTimeSerialization.TestSchema()

    def test_timezone_aware_datetime(self):
        self.assertEqual(
            {"timestamp": "2020-12-02T00:00:00+00:00"},
            self.schema.dump({"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)})
        )

    def test_non_timezone_aware_datetime(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.dump,
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=None)}
        )


class TestCustomAwareDateTimeDeserialization(TestCase):
    class TestSchema(marshmallow.Schema):
        timestamp = CustomAwareDateTime()

    def setUp(self) -> None:
        self.schema = TestCustomAwareDateTimeDeserialization.TestSchema()

    def test_timezone_aware_datetime_object(self):
        self.assertEqual(
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)},
            self.schema.load({"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)})
        )

    def test_timezone_aware_datetime_string(self):
        self.assertEqual(
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)},
            self.schema.load({"timestamp": "2020-12-02T00:00:00+00:00"})
        )

    def test_non_timezone_aware_datetime_object(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=None)}
        )

    def test_non_timezone_aware_datetime_string(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {"timestamp": "2020-12-02T00:00:00"}
        )


class TestCustomDateTimeSerialization(TestCase):
    class TestSchema(marshmallow.Schema):
        timestamp = CustomDateTime()

    def setUp(self) -> None:
        self.schema = TestCustomDateTimeSerialization.TestSchema()

    def test_timezone_aware_datetime(self):
        self.assertEqual(
            {"timestamp": "2020-12-02T00:00:00+00:00"},
            self.schema.dump({"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)})
        )

    def test_non_timezone_aware_datetime(self):
        self.assertEqual(
            {"timestamp": "2020-12-02T00:00:00"},
            self.schema.dump({"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=None)})
        )


class TestCustomDateTimeDeserialization(TestCase):
    class TestSchema(marshmallow.Schema):
        timestamp = CustomDateTime()

    def setUp(self) -> None:
        self.schema = TestCustomDateTimeDeserialization.TestSchema()

    def test_timezone_aware_datetime_object(self):
        self.assertEqual(
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)},
            self.schema.load({"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)})
        )

    def test_timezone_aware_datetime_string(self):
        self.assertEqual(
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=timezone.utc)},
            self.schema.load({"timestamp": "2020-12-02T00:00:00+00:00"})
        )

    def test_non_timezone_aware_datetime_object(self):
        self.assertEqual(
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=None)},
            self.schema.load({"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=None)})
        )

    def test_non_timezone_aware_datetime_string(self):
        self.assertEqual(
            {"timestamp": datetime(2020, 12, 2, 00, 00, 00, 00, tzinfo=None)},
            self.schema.load({"timestamp": "2020-12-02T00:00:00"})
        )
