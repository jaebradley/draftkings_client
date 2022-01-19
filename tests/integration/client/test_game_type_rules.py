import os
from unittest import TestCase
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.game_type_rules import SalaryCapDetails, RosterSlotDetails, LineupTemplateDetails, \
    GameTypeRulesDetails
from tests.config import ROOT_DIRECTORY


class TestGameTypeRules(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_game_type_id_1(self):
        self.assertIsNotNone(self.client.game_type_rules(game_type_id=1))


class TestMockedUpcomingNFLDraftablesResponse(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/game_type_rules/1.json"), encoding="utf-8") as data_file:
            self.response_data = data_file.read()
            patched_method = patch.object(HTTPClient, "game_type_rules")
            mocked_method = patched_method.start()
            mocked_method.return_value = Mock(text=self.response_data)
            self.result = Client().game_type_rules(game_type_id=1)

    def tearDown(self) -> None:
        patch.stopall()

    def test_outputs_object(self):
        self.assertIsNotNone(self.result)

    def test_game_type_rules(self):
        self.assertEqual(
            GameTypeRulesDetails(
                allow_late_swaps=True,
                description="Create a 9-player lineup while staying under the $50,000 salary cap",
                draft_type_name="SalaryCap",
                name="Classic",
                game_type_id=1,
                lineup_templates=[
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Quarterback",
                            name="QB",
                            roster_slot_id=66,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Running Back",
                            name="RB",
                            roster_slot_id=67,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Running Back",
                            name="RB",
                            roster_slot_id=67,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Wide Receiver",
                            name="WR",
                            roster_slot_id=68,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Tight End",
                            name="TE",
                            roster_slot_id=69,
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Flex",
                            name="FLEX",
                            roster_slot_id=70
                        )
                    ),
                    LineupTemplateDetails(
                        roster_slot_details=RosterSlotDetails(
                            description="Defense/Special Teams",
                            name="DST",
                            roster_slot_id=71
                        )
                    )
                ],
                salary_cap_details=SalaryCapDetails(
                    is_enabled=True,
                    minimum_value=0,
                    maximum_value=50000,
                ),
                enforce_selecting_unique_players=True,
            ),
            self.result
        )
