import os
from unittest import TestCase

from draft_kings.response.objects.draftables import Draftables, Competition, Player, PlayerCompetitionDetails, \
    CompetitionWeather, CompetitionTeam
from draft_kings.response.schema.draftables import DraftablesSchema
from tests.config import ROOT_DIRECTORY


class TestUpcomingNFLDraftables(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/upcoming_nfl_draftables.json')) as data_file:
            self.schema = DraftablesSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_competition_details(self):
        self.assertListEqual(
            [
                Competition(
                    competition_id=5523451,
                    sport="NFL",
                    home_team=CompetitionTeam(
                        team_id=343,
                        team_name="Rams",
                        abbreviation="LAR",
                        city="Los Angeles"
                    ),
                    away_team=CompetitionTeam(
                        team_id=339,
                        team_name="Chiefs",
                        abbreviation="KC",
                        city="Kansas City"
                    ),
                    start_time="2018-11-20T01:15:00.0000000Z",
                    name="KC @ LAR",
                    venue="Los Angeles Memorial Coliseum",
                    weather=CompetitionWeather(
                        icon="partly-cloudy-night",
                        is_dome=False
                    ),
                    are_starting_lineups_available=False,
                    are_depth_charts_available=True,
                    competition_state="Upcoming"
                ),
            ],
            self.data.competitions
        )

    def test_first_draftable_property(self):
        self.assertEqual(
            Player(
                draftable_id=11647232,
                first_name="Todd",
                last_name="Gurley II",
                display_name="Todd Gurley II",
                short_name="T. Gurley II",
                player_id=694641,
                position="RB",
                roster_slot_id=511,
                salary=17700,
                is_swappable=True,
                is_disabled=False,
                news_status="None",
                player_image_full="https://d327rxwuxd0q0c.cloudfront.net/nfl/players/694641.png",
                player_image_50="https://d327rxwuxd0q0c.cloudfront.net/m/nfl_50/694641.png",
                player_image_65="https://d327rxwuxd0q0c.cloudfront.net/m/nfl_65/694641.png",
                player_image_160="https://d327rxwuxd0q0c.cloudfront.net/m/nfl_retina/694641.png",
                competition=PlayerCompetitionDetails(
                    competition_id=5523451,
                    name="KC @ LAR",
                    start_time="2018-11-20T01:15:00.0000000Z",
                ),
                team_abbreviation="LAR",
                team_id=343,
                draft_alerts=[]
            ),
            self.data.draftables[0]
        )


class TestHistoricalGolfDraftables(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/historical_golf_draftables.json')) as data_file:
            self.schema = DraftablesSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)
