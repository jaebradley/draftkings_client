from unittest import TestCase

from draft_kings import client


class TestClientDraftGroupDetails(TestCase):
    def test_nba_draft_group_details(self):
        # Draft Group from 2016-11-16
        details = client.draft_group_details(draft_group_id=11513)
        self.assertIsNotNone(details)

    def test_nhl_draft_group_details(self):
        # Draft Group for 2018-11-20
        details = client.draft_group_details(draft_group_id=22953)
        self.assertIsNotNone(details)

    def test_nfl_draft_group_details(self):
        # Draft Group for 2018-11-20 MNF
        details = client.draft_group_details(draft_group_id=22927)
        self.assertIsNotNone(details)

    def test_cfb_draft_group_details(self):
        # Draft Group for 2018-11-24
        details = client.draft_group_details(draft_group_id=22952)
        self.assertIsNotNone(details)

    def test_cbb_draft_group_details(self):
        # Draft Group for 2018-11-19
        details = client.draft_group_details(draft_group_id=22958)
        self.assertIsNotNone(details)

    def test_soccer_uefa_national_league_draft_group_details(self):
        # Draft Group for 2018-11-19
        details = client.draft_group_details(draft_group_id=22855)
        self.assertIsNotNone(details)

    def test_soccer_epl_draft_group_details(self):
        # Start Date is 2018-11-24T15:00:00.0000000Z
        details = client.draft_group_details(draft_group_id=22831)
        self.assertIsNotNone(details)

    def test_euroleague_draft_group_details(self):
        # Start Date is 2018-11-20T17:00:00.0000000Z
        details = client.draft_group_details(draft_group_id=22916)
        self.assertIsNotNone(details)