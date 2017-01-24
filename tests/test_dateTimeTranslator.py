from unittest import TestCase
from datetime import datetime
import pytz

from draft_kings_client.data.translators.date_time_translator import DateTimeTranslator


class TestDateTimeTranslator(TestCase):
    def test_translate(self):
        timestamp = DateTimeTranslator.translate(date_string="/Date(1479258000000)/")
        self.assertIsNotNone(timestamp)
        self.assertEqual(timestamp, datetime.fromtimestamp(timestamp=1479258000000 / 1e3, tz=pytz.utc))

