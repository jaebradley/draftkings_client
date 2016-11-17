import json
import os
from unittest import TestCase
from tests.config import ROOT_DIRECTORY
from draftkings_client.data.translators.available_player_translator import AvailablePlayerTranslator
from draftkings_client.data.models.available_player import AvailablePlayerPosition, AvailablePlayerMatchUp, AvailablePlayerTeam


class TestAvailablePlayerTranslator(TestCase):
    def test_player_response_translation(self):
        expected_match_up = AvailablePlayerMatchUp(home_team=AvailablePlayerTeam(team_id=5, team_abbreviation='Cle'),
                                                   away_team=AvailablePlayerTeam(team_id=28, team_abbreviation='Tor'))

        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/available_nba_player_example.json')) as data_file:
            data = json.load(data_file)
            player = AvailablePlayerTranslator.translate(data)
            self.assertIsNotNone(player)
            self.assertEqual(player.player_id, 214152)
            self.assertEqual(player.team_series_id, 5479720)
            self.assertEqual(player.first_name, 'LeBron')
            self.assertEqual(player.last_name, 'James')
            self.assertEqual(player.jersey_number, 23)
            self.assertEqual(player.position, AvailablePlayerPosition(position_id=27, position_name='SF/PF'))
            self.assertEqual(player.draft_group_start_timestamp, 1479254400000)
            self.assertEqual(player.team_id, 5)
            self.assertEqual(player.match_up, expected_match_up)
            self.assertEqual(player.is_disabled_from_drafting, False)
            self.assertEqual(player.exceptional_messages, [])
            self.assertEqual(player.salary, 10300)
            self.assertEqual(player.draftkings_points_per_game, 51.2)
            self.assertEqual(player.opposition_rank, 20)

    def test_missing_keys(self):
        missing_pid = {}
        self.assertRaises(KeyError, AvailablePlayerTranslator.translate, response=missing_pid)

        missing_tsid = {'pid': 1}
        self.assertRaises(KeyError, AvailablePlayerTranslator.translate, response=missing_tsid)
