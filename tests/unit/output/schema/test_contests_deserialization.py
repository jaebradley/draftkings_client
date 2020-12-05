from datetime import datetime, timezone
from unittest import TestCase

from marshmallow import ValidationError

from draft_kings.data import Sport
from draft_kings.output.objects.contests import EntriesDetails, ContestDetails, ContestsDetails
from draft_kings.output.schema.contests import EntriesDetailsSchema, ContestDetailsSchema, ContestsDetailsSchema


class TestLoadingEntriesDetailsSchema(TestCase):
    def setUp(self) -> None:
        self.schema = EntriesDetailsSchema()

    def test_empty_object_raises_validation_error(self):
        self.assertRaises(ValidationError, self.schema.load, {})

    def test_incomplete_object_raises_validation_error(self):
        self.assertRaises(ValidationError, self.schema.load, {"fee": "jaebaebae"})


class TestLoadingContestDetailsSchema(TestCase):
    def setUp(self) -> None:
        self.schema = ContestDetailsSchema()

    def test_empty_object_raises_validation_error(self):
        self.assertRaises(ValidationError, self.schema.load, {})

    def test_when_only_entries_details_object_is_specified_it_loads_appropriately(self):
        self.assertEqual(
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
                sport=None,
                starts_at=None
            ),
            self.schema.load({
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
                "sport": None,
                "starts_at": None
            })
        )

    def test_sport_identification_loads_appropriately(self):
        self.assertEqual(
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
            ),
            self.schema.load({
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
                "sport": Sport.NFL,
                "starts_at": None
            })
        )

    def test_sport_name_identification_loads_appropriately(self):
        self.assertEqual(
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
            ),
            self.schema.load({
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
            })
        )

    def test_non_optional_values(self):
        self.assertEqual(
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
            ),
            self.schema.load(
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
                }
            )
        )


class TestContestsDetailsSchema(TestCase):
    def setUp(self) -> None:
        self.schema = ContestsDetailsSchema()

    def test_none_values_raise_validation_error(self):
        self.assertRaises(ValidationError, self.schema.load, {"contests": None, "draft_groups": None})

    def test_empty_lists(self):
        self.assertEqual(
            ContestsDetails(contests=[], draft_groups=[]),
            self.schema.load({"contests": [], "draft_groups": []})
        )

    def test_list_with_none_values_raise_validation_error(self):
        self.assertRaises(ValidationError, self.schema.load, {"contests": [None], "draft_groups": [None]})
