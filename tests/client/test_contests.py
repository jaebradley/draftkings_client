from unittest import TestCase

from draft_kings import Client
from draft_kings.data import Sport


class TestContests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_contest(self):
        for sport in Sport:
            result = self.client.contests(sport=sport)
            self.assertIsNotNone(result)
            self.assertIsNotNone(result.contests)
            self.assertIsNotNone(result.draft_groups)
