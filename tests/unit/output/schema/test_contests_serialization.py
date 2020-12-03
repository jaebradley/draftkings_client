from datetime import datetime, timezone
from unittest import TestCase

from draft_kings.data import Sport
from draft_kings.output.objects.contests import EntriesDetails, ContestDetails
from draft_kings.output.schema.contests import EntriesDetailsSchema, ContestDetailsSchema


class TestDumpingEntriesDetailsSchema(TestCase):
    def setUp(self) -> None:
        self.schema = EntriesDetailsSchema()

    def test_object_with_none_values(self):
        self.assertEqual(
            {"fee": None, "maximum": None, "total": None},
            self.schema.dump(EntriesDetails(fee=None, maximum=None, total=None))
        )

    def test_invalid_object_value_raises_value_error(self):
        self.assertRaises(
            ValueError,
            self.schema.dump, {"fee": "jaebaebae", "maximum": None, "total": None}
        )


class TestDumpingContestDetails(TestCase):
    def setUp(self) -> None:
        self.schema = ContestDetailsSchema()

    def test_dumping_optional_values(self):
        self.assertEqual(
            {
                "contest_id": None,
                "draft_group_id": None,
                "entries_details": {
                    "fee": None,
                    "maximum": None,
                    "total": None
                },
                "fantasy_player_points": None,
                "is_double_up": False,
                "is_fifty_fifty": False,
                "is_guaranteed": False,
                "is_head_to_head": False,
                "is_starred": False,
                "name": None,
                "payout": None,
                "sport": "NFL",
                "starts_at": None
            },
            self.schema.dump(
                ContestDetails(
                    contest_id=None,
                    draft_group_id=None,
                    entries_details=EntriesDetails(
                        fee=None,
                        maximum=None,
                        total=None,
                    ),
                    fantasy_player_points=None,
                    is_double_up=False,
                    is_fifty_fifty=False,
                    is_guaranteed=False,
                    is_head_to_head=False,
                    is_starred=False,
                    name=None,
                    payout=None,
                    sport=Sport.NFL,
                    starts_at=None
                )
            )
        )

    def test_non_optional_values(self):
        self.assertEqual(
            {
                "contest_id": 1,
                "draft_group_id": 2,
                "entries_details": {
                    "fee": 3.0,
                    "maximum": 4,
                    "total": 5
                },
                "fantasy_player_points": 6.0,
                "is_double_up": True,
                "is_fifty_fifty": True,
                "is_guaranteed": True,
                "is_head_to_head": True,
                "is_starred": True,
                "name": "jaebaebae",
                "payout": 7.0,
                "sport": "NFL",
                "starts_at": "2020-12-01T00:00:00+00:00"
            },
            self.schema.dump(
                ContestDetails(
                    contest_id=1,
                    draft_group_id=2,
                    entries_details=EntriesDetails(
                        fee=3,
                        maximum=4,
                        total=5,
                    ),
                    fantasy_player_points=6,
                    is_double_up=True,
                    is_fifty_fifty=True,
                    is_guaranteed=True,
                    is_head_to_head=True,
                    is_starred=True,
                    name="jaebaebae",
                    payout=7,
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 12, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
                )
            )
        )
