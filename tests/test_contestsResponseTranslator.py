import json
import os
from unittest import TestCase

from draft_kings_client.data.translators.contests_response_translator import ContestsResponseTranslator
from tests.config import ROOT_DIRECTORY


class TestContestsResponseTranslator(TestCase):
    def test_translate(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/nba_contests_example.json')) as data_file:
            data = json.load(data_file)
            translation = ContestsResponseTranslator.translate(data)
            self.assertIsNotNone(translation)
