from unittest import TestCase

from draft_kings_client.data.models.available_player import AvailablePlayerPosition, MatchUp, AvailablePlayerTeam
from draft_kings_client.data.translators.available_player_translator import AvailablePlayerTranslator


class TestAvailablePlayerTranslator(TestCase):
    def test_player_response_translation(self):
        player_id = 214152
        team_series_id = 3704
        first_name = u'LeBron'
        last_name = 'uJames'
        jersey_number = 23
        position_name = u'SF/PF'
        position_id = 27
        draft_group_start_timestamp = 1479254400000
        team_id = 5
        home_team_id = team_id
        away_team_id = 28
        home_team_abbreviation = u'Cle'
        away_team_abbreviation = u'Tor'
        is_disabled_from_drafting = False
        exceptional_messages = [u'Foo', u'Bar']
        salary = 10300
        points_per_game = 51.2
        opposition_rank = 20
        response = {
            "pid": player_id,
            "pcode": team_series_id,
            "tsid": team_series_id,
            "fn": first_name,
            "ln": last_name,
            "jn": jersey_number,
            "pn": position_name,
            "dgst": draft_group_start_timestamp,
            "tid": team_id,
            "htid": home_team_id,
            "atid": away_team_id,
            "htabbr": home_team_abbreviation,
            "atabbr": away_team_abbreviation,
            "posid": position_id,
            "IsDisabledFromDrafting": is_disabled_from_drafting,
            "ExceptionalMessages": exceptional_messages,
            "s": salary,
            "ppg": str(points_per_game),
            "or": opposition_rank,
        }
        expected_match_up = MatchUp(home_team=AvailablePlayerTeam(team_id=home_team_id,
                                                                  team_abbreviation=home_team_abbreviation),
                                    away_team=AvailablePlayerTeam(team_id=away_team_id,
                                                                                 team_abbreviation=away_team_abbreviation))
        player = AvailablePlayerTranslator.translate(response)
        self.assertIsNotNone(player)
        self.assertEqual(player.player_id, player_id)
        self.assertEqual(player.team_series_id, team_series_id)
        self.assertEqual(player.first_name, first_name)
        self.assertEqual(player.last_name, last_name)
        self.assertEqual(player.jersey_number, jersey_number)
        self.assertEqual(player.position, AvailablePlayerPosition(position_id=position_id, position_name=position_name))
        self.assertEqual(player.draft_group_start_timestamp, draft_group_start_timestamp)
        self.assertEqual(player.team_id, team_id)
        self.assertEqual(player.match_up, expected_match_up)
        self.assertEqual(player.is_disabled_from_drafting, is_disabled_from_drafting)
        self.assertEqual(player.exceptional_messages, exceptional_messages)
        self.assertEqual(player.salary, salary)
        self.assertEqual(player.draftkings_points_per_game, points_per_game)
        self.assertEqual(player.opposition_rank, opposition_rank)

    def test_missing_keys(self):
        missing_pid = {}
        self.assertRaises(KeyError, AvailablePlayerTranslator.translate, response=missing_pid)

        missing_tsid = {'pid': 1}
        self.assertRaises(KeyError, AvailablePlayerTranslator.translate, response=missing_tsid)

        missing_fn = {'pid': 1, 'tsid': 2}
        self.assertRaises(KeyError, AvailablePlayerTranslator.translate, response=missing_fn)
