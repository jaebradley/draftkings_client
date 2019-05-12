from unittest import TestCase

import datetime
import pytz
from draft_kings.client import available_players


class TestClient(TestCase):
    def test_get_available_players(self):
        result = available_players(draft_group_id=11513)
        self.assertIsNotNone(result)

    def test_nba_multiple_players(self):
        result = available_players(draft_group_id=11513)
        self.assertEqual(len(result["players"]), 150)

    def test_nba_multiple_teams(self):
        result = available_players(draft_group_id=11513)
        self.assertEqual(len(result["team_series_list"]), 5)

    def test_nba_player_fields(self):
        result = available_players(draft_group_id=11513)
        lebron = result["players"][0]
        self.assertEqual(lebron["id"], 214152)
        self.assertEqual(lebron["draft"]["starts_at"], datetime.datetime(2016, 11, 16, 0, 0, 0, tzinfo=pytz.UTC))
        self.assertTrue(lebron["draft"]["draftable"])
        self.assertEqual(lebron["draft"]["salary"], 10300)
        self.assertEqual(lebron["first_name"], "LeBron")
        self.assertEqual(lebron["jersey_number"], 23)
        self.assertEqual(lebron["last_name"], "James")
        self.assertEqual(lebron["match_up"]["id"], 5479720)
        self.assertEqual(lebron["match_up"]["away_team_id"], 28)
        self.assertEqual(lebron["match_up"]["home_team_id"], 5)
        self.assertEqual(lebron["match_up"]["opposition_rank"], 23)
        self.assertEqual(lebron["points_per_contest"], 54.7)
        self.assertEqual(lebron["position"]["id"], 27)
        self.assertEqual(lebron["position"]["name"], "SF/PF")
        self.assertEqual(lebron["team_id"], 5)

    def test_nba_team_series_fields(self):
        result = available_players(draft_group_id=11513)
        team_series = result["team_series_list"][0]
        self.assertEqual(team_series["id"], 5479720)
        self.assertEqual(team_series["away_team_id"], 28)
        self.assertEqual(team_series["home_team_id"], 5)
        self.assertEqual(team_series["starts_at"], datetime.datetime(2016, 11, 16, 0, 0, 0, tzinfo=pytz.UTC))
        self.assertEqual(team_series["status_id"], 4)
        self.assertEqual(team_series["weather"], "")

    def test_get_available_players_league_of_legends(self):
        result = available_players(draft_group_id=26691)
        self.assertIsNotNone(result)

    def test_lol_multiple_players(self):
        result = available_players(draft_group_id=26691)
        self.assertEqual(len(result["players"]), 28)

    def test_lol_multiple_teams(self):
        result = available_players(draft_group_id=26691)
        self.assertEqual(len(result["team_series_list"]), 2)

    def test_lol_player_fields(self):
        result = available_players(draft_group_id=26691)
        big_koro = result["players"][0]
        self.assertEqual(big_koro["id"], 1283)
        self.assertEqual(big_koro["draft"]["starts_at"], datetime.datetime(2019, 5, 1, 9, 0, 0, tzinfo=pytz.UTC))
        self.assertTrue(big_koro["draft"]["draftable"])
        self.assertEqual(big_koro["draft"]["salary"], 9000)
        self.assertEqual(big_koro["first_name"], "")
        self.assertIsNone(big_koro["jersey_number"])
        self.assertEqual(big_koro["last_name"], "BigKoro")
        self.assertEqual(big_koro["match_up"]["id"], 5613734)
        self.assertEqual(big_koro["match_up"]["away_team_id"], 62492)
        self.assertEqual(big_koro["match_up"]["home_team_id"], 156847)
        self.assertIsNone(big_koro["match_up"]["opposition_rank"])
        self.assertEqual(big_koro["position"]["id"], 155)
        self.assertEqual(big_koro["position"]["name"], "ADC")
        self.assertEqual(big_koro["team_id"], 62492)

    def test_lol_team_series_fields(self):
        result = available_players(draft_group_id=26691)
        team_series = result["team_series_list"][0]
        self.assertEqual(team_series["id"], 5613734)
        self.assertEqual(team_series["away_team_id"], 62492)
        self.assertEqual(team_series["home_team_id"], 156847)
        self.assertEqual(team_series["starts_at"], datetime.datetime(2019, 5, 1, 9, 0, 0, tzinfo=pytz.UTC))
        self.assertEqual(team_series["status_id"], 4)
        self.assertEqual(team_series["weather"], "")