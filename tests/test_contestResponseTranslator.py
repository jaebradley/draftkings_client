import json
import os
from unittest import TestCase
from tests.config import ROOT_DIRECTORY
from draftkings_client.data.translators.contest_response_translator import ContestResponseTranslator


class TestContestResponseTranslator(TestCase):
    def test_contest_response_translation(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/nba_contest_example.json')) as data_file:
            data = json.load(data_file)
            translation = ContestResponseTranslator.translate(data)
            self.assertIsNotNone(translation)
            self.assertEqual(translation.contest_id, 32099545)
