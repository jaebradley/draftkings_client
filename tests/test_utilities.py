from datetime import datetime
from unittest import TestCase

import pytz

from draft_kings.utilities import dig, translate_formatted_datetime


class TestGet(TestCase):
    def test_fallback(self):
        self.assertIsNone(dig({}, "a", "b", "c"))

    def test_returns_nested_value(self):
        self.assertEqual(dig({"foo": {"bar": "baz"}}, "foo", "bar"), "baz")


class TestTranslateDatetime(TestCase):
    def test_translate_datetime_string(self):
        timestamp = translate_formatted_datetime("/Date(1479258000000)/")
        self.assertIsNotNone(timestamp)
        self.assertEqual(timestamp, datetime.fromtimestamp(1479258000000 / 1e3, tz=pytz.utc))

