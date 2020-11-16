import os
from unittest import TestCase

from draft_kings.response.objects.players import PlayerTeamSeries, PlayerDetails
from draft_kings.response.schema.players import PlayersDetailsSchema
from tests.config import ROOT_DIRECTORY


class TestSoccerPlayers(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/soccer_player_list_example.json')) as data_file:
            self.schema = PlayersDetailsSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_sergio_aguero_player_details(self):
        self.assertEqual(
            PlayerDetails(away_team_id=40552, draft_group_start_time=None, exceptional_messages=[],
                          first_name="Sergio", home_team_id=40820, is_disabled_from_drafting=False, jersey_number=0,
                          last_name="Agüero", opposition_rank=0, player_id=37572, position_id=160, position_name="F",
                          points_per_game="14.7", salary=9200, team_id=40552, team_series_id=5473468),
            self.data.players[0]
        )

    def crystal_palace_and_manchester_city_team_series_exists(self):
        self.assertTrue("5473468" in self.data.team_series)

    def crystal_palace_and_manchester_city_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=40522, home_team_id=40820, starts_at="/Date(1479567600000)/",
                             status=1, weather="partly-cloudy-day"),
            self.data.team_series["5473468"]
        )

    def southampton_and_liverpool_team_series_exists(self):
        self.assertTrue("5473471" in self.data.team_series)

    def southampton_and_liverpool_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=40817, home_team_id=40818, starts_at="/Date(1479567600000)/",
                             status=1, weather="rain"),
            self.data.team_series["5473471"]
        )

    def test_tottenham_and_west_ham_united_team_series_exists(self):
        self.assertTrue("5473474" in self.data.team_series)

    def test_tottenham_and_west_ham_united_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=40819, home_team_id=40813, starts_at="/Date(1479576600000)/",
                             status=1, weather="partly-cloudy-night"),
            self.data.team_series["5473474"]
        )

    def test_everton_and_swansea_team_series_exists(self):
        self.assertTrue("5473469" in self.data.team_series)

    def test_everton_and_swansea_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=40825, home_team_id=40815, starts_at="/Date(1479567600000)/",
                             status=1, weather="partly-cloudy-day"),
            self.data.team_series["5473469"]
        )

    def test_watford_and_leicester_team_series_exists(self):
        self.assertTrue("5473475" in self.data.team_series)

    def test_watford_and_leicester_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=40816, home_team_id=40824, starts_at="/Date(1479567600000)/",
                             status=1, weather="partly-cloudy-day"),
            self.data.team_series["5473475"]
        )

    def test_stoke_and_bournemouth_team_series_exists(self):
        self.assertTrue("5473472" in self.data.team_series)

    def test_stoke_and_bournemouth_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=40826, home_team_id=40827, starts_at="/Date(1479567600000)/",
                             status=1, weather="partly-cloudy-day"),
            self.data.team_series["5473472"]
        )

    def test_hull_and_sunderland_team_series_exists(self):
        self.assertTrue("5473473" in self.data.team_series)

    def test_hull_and_sunderland_team_series_details(self):
        self.assertEqual(
            PlayerTeamSeries(away_team_id=43295, home_team_id=40823, starts_at="/Date(1479567600000)/",
                             status=1, weather="partly-cloudy-day"),
            self.data.team_series["5473473"],
        )
