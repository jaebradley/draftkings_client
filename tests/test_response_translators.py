import json
import os
from unittest import TestCase

from draft_kings_client.response_translators import translate_contests, translate_contest
from tests.config import ROOT_DIRECTORY


class TestContestsResponseTranslator(TestCase):
    def test_translate_contests(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/nba_contests_example.json')) as data_file:
            data = json.load(data_file)
            translation = translate_contests(data)
            self.assertIsNotNone(translation)


class TestContestResponseTranslator(TestCase):
    def test_translate_contest(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/nba_contest_example.json')) as data_file:
            data = json.load(data_file)
            translation = translate_contest(data)
            self.assertIsNotNone(translation)
            self.assertEqual(translation["id"], 32099545)
