from unittest import TestCase

from marshmallow import ValidationError

from draft_kings.output.objects.contests import EntriesDetails, ContestDetails
from draft_kings.output.schema.contests import EntriesDetailsSchema, ContestDetailsSchema
from draft_kings.data import Sport


class TestLoadingEntriesDetailsSchema(TestCase):
    def test_when_empty_object_it_deserializes_with_missing_values(self):
        self.assertRaises(
            ValidationError,
            EntriesDetailsSchema().load,
            {},
        )

    def test_invalid_object_value_raises_validation_error(self):
        self.assertRaises(ValidationError, EntriesDetailsSchema().load, {"fee": "jaebaebae"})


class TestDumpingEntriesDetailsSchema(TestCase):
    def test_object_with_none_values(self):
        self.assertEqual(
            {"fee": None, "maximum": None, "total": None},
            EntriesDetailsSchema().dump(EntriesDetails(fee=None, maximum=None, total=None))
        )

    def test_invalid_object_value_raises_value_error(self):
        self.assertRaises(
            ValueError,
            EntriesDetailsSchema().dump, {"fee": "jaebaebae", "maximum": None, "total": None}
        )


class TestLoadingContestDetailsSchema(TestCase):
    def test_when_empty_object_it_raises_validation_error(self):
        self.assertRaises(ValidationError, ContestDetailsSchema().load, {})

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
            ContestDetailsSchema().load({
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
            ContestDetailsSchema().load({
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
            ContestDetailsSchema().load({
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
