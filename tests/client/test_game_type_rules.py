import os
import pprint
from unittest import TestCase
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.http_client import HTTPClient
from draft_kings.model.game_type_rules import (
    SalaryCap,
    RosterSlot,
    LineupTemplate,
    GameTypeRules,
)
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
        expected: GameTypeRules = GameTypeRules.model_construct(
            allow_late_swap=True,
            description="Create a 9-player lineup while staying under the $50,000 salary cap",
            draft_type_name="SalaryCap",
            name="Classic",
            game_type_id=1,
            lineup_templates=[
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Quarterback", name="QB", roster_slot_id=66
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Running Back", name="RB", roster_slot_id=67
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Running Back", name="RB", roster_slot_id=67
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Wide Receiver", name="WR", roster_slot_id=68
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Wide Receiver", name="WR", roster_slot_id=68
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Wide Receiver", name="WR", roster_slot_id=68
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Tight End", name="TE", roster_slot_id=69
                    )
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(description="Flex", name="FLEX", roster_slot_id=70)
                ),
                LineupTemplate.model_construct(
                    roster_slot_details=RosterSlot.model_construct(
                        description="Defense/Special Teams", name="DST", roster_slot_id=71
                    )
                ),
            ],
            salary_cap_details=SalaryCap.model_construct(is_enabled=True, minimum_value=0, maximum_value=50000),
            enforce_selecting_unique_players=True,
        )

        self.assertEqual(expected, self.result)
