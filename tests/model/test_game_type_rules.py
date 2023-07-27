import os
from unittest import TestCase

from draft_kings.model.game_type_rules import SalaryCap, RosterSlot, LineupTemplate, GameTypeRules
from tests.config import ROOT_DIRECTORY


class TestClassicNFLGameTypeRules(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/game_type_rules/1.json"), encoding="utf-8") as data_file:
            self.data: GameTypeRules = GameTypeRules.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_game_type_rules(self) -> None:
        self.assertEqual(
            GameTypeRules.model_construct(
                allow_late_swap=True,
                description="Create a 9-player lineup while staying under the $50,000 salary cap",
                draft_type_name="SalaryCap",
                name="Classic",
                game_type_id=1,
                lineup_templates=[
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Quarterback",
                            name="QB",
                            roster_slot_id=66,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Running Back",
                            name="RB",
                            roster_slot_id=67,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Running Back",
                            name="RB",
                            roster_slot_id=67,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Tight End",
                            name="TE",
                            roster_slot_id=69,
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Flex", name="FLEX", roster_slot_id=70
                        )
                    ),
                    LineupTemplate.model_construct(
                        roster_slot_details=RosterSlot.model_construct(
                            description="Defense/Special Teams", name="DST", roster_slot_id=71
                        )
                    ),
                ],
                salary_cap_details=SalaryCap.model_construct(
                    is_enabled=True,
                    maximum_value=50000.0,
                    minimum_value=0.0,
                ),
                enforce_selecting_unique_players=True,
            ),
            self.data,
        )
