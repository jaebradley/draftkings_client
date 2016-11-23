from unittest import TestCase
from draft_kings_client.data.translators.date_translator import DateTranslator


class TestDateTranslator(TestCase):
    def test_translate(self):
        timestamp = DateTranslator.translate(date_string="/Date(1479258000000)/")
        self.assertIsNotNone(timestamp)
        self.assertEqual(timestamp, 1479258000000)

