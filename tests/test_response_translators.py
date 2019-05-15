import json
import os
from unittest import TestCase
from datetime import datetime
import pytz

from draft_kings.response_translators import translate_contests, translate_contest
from draft_kings.data import Sport
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
            self.assertFalse(translation["double_up"])
            self.assertEqual(translation["draft_group_id"], 11435)
            self.assertEqual(translation["entries"], {"maximum": 12261, "fee": 33.0, "total": 864})
            self.assertEqual(translation["fantasy_player_points"], 33)
            self.assertFalse(translation["fifty_fifty"])
            self.assertTrue(translation["guaranteed"])
            self.assertFalse(translation["head_to_head"])
            self.assertEqual(translation["name"], "NBA $350K Bird [$350,000 Guaranteed]")
            self.assertEqual(translation["payout"], 350000.0)
            self.assertEqual(translation["sport"], Sport.NBA)
            self.assertTrue(translation["starred"])
            self.assertEqual(translation["starts_at"], datetime(2016, 11, 12, 0, 0, 0, tzinfo=pytz.UTC))
