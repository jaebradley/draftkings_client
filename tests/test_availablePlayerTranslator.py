from datetime import datetime
from unittest import TestCase

import pytz

from draft_kings_client.translators.available_player_translator import translate


class TestAvailablePlayerTranslator(TestCase):
    def test_player_response_translation(self):
        player_id = 214152
        team_series_id = 3704
        first_name = u'LeBron'
        last_name = 'uJames'
        jersey_number = 23
        position_name = u'SF/PF'
        position_group_id = 27
        draft_group_start_timestamp = 1479254400000
        draft_group_start_datetime = datetime.fromtimestamp(timestamp=draft_group_start_timestamp / 1000, tz=pytz.utc)
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
            "posid": position_group_id,
            "IsDisabledFromDrafting": is_disabled_from_drafting,
            "ExceptionalMessages": exceptional_messages,
            "s": salary,
            "ppg": str(points_per_game),
            "or": opposition_rank,
        }

        player = translate(response)
        self.assertIsNotNone(player)
        self.assertEqual(player["id"], player_id)
        # self.assertEqual(player["first_name"], first_name)
        # self.assertEqual(player["last_name"], last_name)
        # self.assertEqual(player["jersey_number"], jersey_number)
        # self.assertEqual(player["draft_starts_at"], draft_group_start_datetime)
        # self.assertEqual(player["team_id"], team_id)
        # self.assertEqual(player["cannot_draft"], is_disabled_from_drafting)
        # self.assertEqual(player["exceptional_messages"], exceptional_messages)
        # self.assertEqual(player["salary"], salary)
        # self.assertEqual(player["points_per_contest"], points_per_game)
        # self.assertEqual(player["opposition_rank"], opposition_rank)
