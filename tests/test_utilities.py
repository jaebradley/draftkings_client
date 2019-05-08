from unittest import TestCase

import pytz
from datetime import datetime

from draft_kings_client.utilities import remap_keys, dig, translate_datetime


class TestRemapKeys(TestCase):
    def test_remaps_dictionary(self):
        column_map = {
            'old column 1': 'new column 1',
            'old column 2': 'new column 2',
            'old column 3': 'new column 3',
        }
        old_data = {
            'old column 1': 'foo',
            'old column 2': 'bar',
            'old column 3': 'baz',
        }
        new_data = {
            'new column 1': 'foo',
            'new column 2': 'bar',
            'new column 3': 'baz',
        }
        self.assertEqual(remap_keys(old_data, column_map), new_data)

    def test_default_none_for_keys_that_do_not_exist(self):
        column_map = {
            'old column 1': 'new column 1',
            'old column 2': 'new column 2',
            'old column 3': 'new column 3',
        }
        old_data = {
            'old column 1': 'foo',
            'old column 2': 'bar',
        }
        new_data = {
            'new column 1': 'foo',
            'new column 2': 'bar',
            'new column 3': None,
        }
        self.assertEqual(remap_keys(old_data, column_map), new_data)

    def test_only_returns_remapped_keyst(self):
        column_map = {
            'old column 1': 'new column 1',
            'old column 2': 'new column 2',
        }
        old_data = {
            'old column 1': 'foo',
            'old column 2': 'bar',
            'old column 3': 'baz',
        }
        new_data = {
            'new column 1': 'foo',
            'new column 2': 'bar',
        }
        self.assertEqual(remap_keys(old_data, column_map), new_data)


class TestGet(TestCase):
    def test_fallback(self):
        self.assertIsNone(dig({}, "a", "b", "c"))

    def test_returns_nested_value(self):
        self.assertEqual(dig({"foo": {"bar": "baz"}}, "foo", "bar"), "baz")


class TestTranslateDatetime(TestCase):
    def test_translate_datetime_string(self):
        timestamp = translate_datetime("/Date(1479258000000)/")
        self.assertIsNotNone(timestamp)
        self.assertEqual(timestamp, datetime.fromtimestamp(1479258000000 / 1e3, tz=pytz.utc))

