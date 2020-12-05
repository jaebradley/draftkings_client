from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from draft_kings.response.objects.contests import ContestAttributes, Contest, DraftGroup, Contests


class TestContestTypeAttributes(TestCase):
    def test_equal_when_attributes_are_equal_and_equivalent_classes(self):
        self.assertEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
        )

    def test_not_equal_when_is_double_up_is_different(self):
        self.assertNotEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
            ContestAttributes(
                is_double_up=False,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
        )

    def test_not_equal_when_is_fifty_fifty_is_different(self):
        self.assertNotEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=False,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
        )

    def test_not_equal_when_is_guaranteed_is_different(self):
        self.assertNotEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=False,
                is_h2h=True,
                is_starred=True
            ),
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
        )

    def test_not_equal_when_is_h2h_is_different(self):
        self.assertNotEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=False,
                is_starred=True
            ),
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
        )

    def test_not_equal_when_is_starred_is_different(self):
        self.assertNotEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=False
            ),
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
        )

    def test_not_equal_when_different_classes(self):
        self.assertNotEqual(
            ContestAttributes(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            ),
            MagicMock(
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_h2h=True,
                is_starred=True
            )
        )


class TestContest(TestCase):
    def test_is_equal_when_same_class_and_attributes_are_equal(self):
        self.assertEqual(
            Contest(
                attributes=ContestAttributes(
                    is_double_up=True,
                    is_fifty_fifty=True,
                    is_guaranteed=True,
                    is_h2h=True,
                    is_starred=True
                ),
                contest_id=1,
                draft_group_id=2,
                entry_fee=float(3),
                entry_maximum=4,
                entry_total=5,
                fantasy_player_points=float(5),
                name="jaebaebae",
                payout=float(6),
                sport_id=7,
                starts_at="now"
            ),
            Contest(
                attributes=ContestAttributes(
                    is_double_up=True,
                    is_fifty_fifty=True,
                    is_guaranteed=True,
                    is_h2h=True,
                    is_starred=True
                ),
                contest_id=1,
                draft_group_id=2,
                entry_fee=float(3),
                entry_maximum=4,
                entry_total=5,
                fantasy_player_points=float(5),
                name="jaebaebae",
                payout=float(6),
                sport_id=7,
                starts_at="now"
            )
        )

    def test_is_not_equal_when_not_same_class_and_attributes_are_equal(self):
        self.assertNotEqual(
            Contest(
                attributes=ContestAttributes(
                    is_double_up=True,
                    is_fifty_fifty=True,
                    is_guaranteed=True,
                    is_h2h=True,
                    is_starred=True
                ),
                contest_id=1,
                draft_group_id=2,
                entry_fee=float(3),
                entry_maximum=4,
                entry_total=5,
                fantasy_player_points=float(5),
                name="jaebaebae",
                payout=float(6),
                sport_id=7,
                starts_at="now"
            ),
            MagicMock(
                attributes=ContestAttributes(
                    is_double_up=True,
                    is_fifty_fifty=True,
                    is_guaranteed=True,
                    is_h2h=True,
                    is_starred=True
                ),
                contest_id=1,
                draft_group_id=2,
                entry_fee=float(3),
                entry_maximum=4,
                entry_total=5,
                fantasy_player_points=float(5),
                name="jaebaebae",
                payout=float(6),
                sport_id=7,
                starts_at="now"
            )
        )

    def test_is_not_equal_when_not_same_class_and_attributes_are_not_equal(self):
        self.assertNotEqual(
            Contest(
                attributes=ContestAttributes(
                    is_double_up=True,
                    is_fifty_fifty=True,
                    is_guaranteed=True,
                    is_h2h=True,
                    is_starred=True
                ),
                contest_id=1,
                draft_group_id=2,
                entry_fee=float(3),
                entry_maximum=4,
                entry_total=5,
                fantasy_player_points=float(5),
                name="jaebaebae",
                payout=float(6),
                sport_id=7,
                starts_at="now"
            ),
            MagicMock(
                attributes=ContestAttributes(
                    is_double_up=False,
                    is_fifty_fifty=False,
                    is_guaranteed=False,
                    is_h2h=False,
                    is_starred=False
                ),
                contest_id=-1,
                draft_group_id=-2,
                entry_fee=float(-3),
                entry_maximum=-4,
                entry_total=-5,
                fantasy_player_points=float(-5),
                name="not jaebaebae",
                payout=float(-6),
                sport_id=-7,
                starts_at="not now"
            )
        )


class TestDraftGroup(TestCase):
    def test_equal_when_same_class_and_attributes(self):
        self.assertEqual(
            DraftGroup(
                draft_group_id=1,
                draft_group_series_id=2,
                contest_type_id=3,
                sport="jaebaebae",
                start_date=datetime(2020, 11, 23, 7, 30, 0, 0),
                game_count=4
            ),
            DraftGroup(
                draft_group_id=1,
                draft_group_series_id=2,
                contest_type_id=3,
                sport="jaebaebae",
                start_date=datetime(2020, 11, 23, 7, 30, 0, 0),
                game_count=4
            )
        )

    def test_not_equal_when_not_same_class_but_identical_attributes(self):
        self.assertNotEqual(
            DraftGroup(
                draft_group_id=1,
                draft_group_series_id=2,
                contest_type_id=3,
                sport="jaebaebae",
                start_date=datetime(2020, 11, 23, 7, 30, 0, 0),
                game_count=4
            ),
            MagicMock(
                draft_group_id=1,
                draft_group_series_id=2,
                contest_type_id=3,
                sport="jaebaebae",
                start_date=datetime(2020, 11, 23, 7, 30, 0, 0),
                game_count=4
            )
        )

    def test_not_equal_when_same_class_but_not_identical_attributes(self):
        self.assertNotEqual(
            DraftGroup(
                draft_group_id=1,
                draft_group_series_id=2,
                contest_type_id=3,
                sport="jaebaebae",
                start_date=datetime(2020, 11, 23, 7, 30, 0, 0),
                game_count=4
            ),
            DraftGroup(
                draft_group_id=-1,
                draft_group_series_id=-2,
                contest_type_id=-3,
                sport="not jaebaebae",
                start_date=datetime(2019, 10, 22, 6, 29, 0, 0),
                game_count=-4
            )
        )


class TestContests(TestCase):
    def test_equal_when_same_class_and_attributes(self):
        self.assertEqual(
            Contests(contests=[], draft_groups=[]),
            Contests(contests=[], draft_groups=[])
        )

    def test_not_equal_when_not_same_class_but_same_attributes(self):
        self.assertNotEqual(
            Contests(contests=[], draft_groups=[]),
            MagicMock(contests=[], draft_groups=[])
        )

    def test_not_equal_when_same_class_but_not_same_attributes(self):
        self.assertNotEqual(
            Contests(
                contests=[],
                draft_groups=[
                    DraftGroup(
                        draft_group_id=1,
                        draft_group_series_id=2,
                        contest_type_id=3,
                        sport="jaebaebae",
                        start_date=datetime(2020, 11, 23, 7, 30, 0, 0),
                        game_count=4
                    ),
                ]
            ),
            Contests(contests=[], draft_groups=[])
        )
