from datetime import datetime, timezone
from unittest import TestCase

from draft_kings.utilities import translate_formatted_datetime


class TestTranslateDatetime(TestCase):
    def test_translate_datetime_string(self):
        timestamp = translate_formatted_datetime("/Date(1479258000000)/")
        self.assertIsNotNone(timestamp)
        self.assertEqual(timestamp, datetime.fromtimestamp(1479258000000 / 1e3, tz=timezone.utc))
