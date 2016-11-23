from unittest import TestCase

from draft_kings_client.data.translators.available_players_translator import AvailablePlayersTranslator
from draft_kings_client.data.models.available_players import AvailablePlayers


class TestAvailablePlayersTranslator(TestCase):

    def test_translation(self):
        response = {
            'playerList': [],
            'teamList': {}
        }

        expected_translation = AvailablePlayers(player_list=[], team_series_list=[])
        translation = AvailablePlayersTranslator.translate(response=response)
        self.assertEqual(translation, expected_translation)

    def test_field_validation(self):
        missing_player_list_response = {
            'teamList': {}
        }

        self.assertRaises(KeyError, AvailablePlayersTranslator.translate, response=missing_player_list_response)

        missing_team_list_response = {
            'playerList': []
        }

        self.assertRaises(KeyError, AvailablePlayersTranslator.translate, response=missing_team_list_response)
