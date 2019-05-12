from unittest import TestCase

from draft_kings import client


class TestClientDraftables(TestCase):
    def test_nba_draftables(self):
        draftables = client.draftables(draft_group_id=11513)
        self.assertIsNotNone(draftables)

    def test_nhl_draftables(self):
        draftables = client.draftables(draft_group_id=22953)
        self.assertIsNotNone(draftables)

    def test_nfl_draftables(self):
        draftables = client.draftables(draft_group_id=22927)
        self.assertIsNotNone(draftables)

    def test_cfb_draftables(self):
        draftables = client.draftables(draft_group_id=22952)
        self.assertIsNotNone(draftables)

    def test_cbb_draftables(self):
        draftables = client.draftables(draft_group_id=22958)
        self.assertIsNotNone(draftables)

    def test_soccer_uefa_national_league_draftables(self):
        draftables = client.draftables(draft_group_id=22855)
        self.assertIsNotNone(draftables)

    def test_soccer_epl_draftables(self):
        draftables = client.draftables(draft_group_id=22831)
        self.assertIsNotNone(draftables)

    def test_euroleague_draftables(self):
        draftables = client.draftables(draft_group_id=22916)
        self.assertIsNotNone(draftables)