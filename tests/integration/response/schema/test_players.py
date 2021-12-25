import os
from unittest import TestCase

from draft_kings.response.objects.players import TeamSeries, Player, ExceptionalMessage, ExceptionalMessageType
from draft_kings.response.schema.players import PlayersDetailsSchema
from tests.config import ROOT_DIRECTORY


class TestSoccerPlayers(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, 'tests/files/available_players/22831.json'),
                encoding="utf-8"
        ) as data_file:
            self.schema = PlayersDetailsSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_first_player_details(self):
        self.assertEqual(
            Player(away_team_id=40551, draft_group_start_time=None, exceptional_messages=[],
                   first_name="Eden", home_team_id=40813, is_disabled_from_drafting=False, jersey_number=7,
                   last_name="Hazard", opposition_rank=1, player_id=42786, position_id=182, position_name="M/F",
                   points_per_game="0.0", salary=10400, team_id=40551, team_series_id=5527123),
            self.data.players[0]
        )

    def test_tottenham_and_chelesa_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=40551, home_team_id=40813, starts_at="/Date(1543080600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527123"]
        )

    def test_west_ham_united_and_manchester_city_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=40552, home_team_id=40819, starts_at="/Date(1543071600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527125"]
        )

    def test_watford_and_liverpool_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=40817, home_team_id=40824, starts_at="/Date(1543071600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527124"]
        )

    def test_everton_and_cardiff_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=53600, home_team_id=40815, starts_at="/Date(1543071600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527120"]
        )

    def test_manchester_united_and_crystal_palace_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=40820, home_team_id=40549, starts_at="/Date(1543071600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527122"]
        )

    def test_birmingham_and_leicester_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=40816, home_team_id=53563, starts_at="/Date(1543071600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527118"]
        )

    def test_fulham_and_southampton_team_series_details(self):
        self.assertEqual(
            TeamSeries(away_team_id=40818, home_team_id=53577, starts_at="/Date(1543071600000)/",
                       status="Final", weather=None),
            self.data.team_series["5527121"],
        )


class TestNFLPlayersWithExceptionalMessages(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, 'tests/files/available_players/41793.json'),
                encoding="utf-8"
        ) as data_file:
            self.schema = PlayersDetailsSchema()
            self.data = self.schema.loads(data_file.read())

    def test_exceptional_messages(self):
        self.assertListEqual(
            [
                ExceptionalMessage(
                    message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points "
                            "in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                    priority=100,
                    message_type=ExceptionalMessageType(
                        name="player"
                    )
                )
            ],
            self.data.players[3].exceptional_messages
        )
