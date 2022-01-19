import os
from datetime import datetime, timezone
from unittest import TestCase

from draft_kings.response.objects.draftables import Competition, Player, PlayerCompetitionDetails, \
    CompetitionWeather, CompetitionTeam, DraftAlert
from draft_kings.response.schema.draftables import DraftablesSchema, PlayerSchema
from tests.config import ROOT_DIRECTORY


class TestUpcomingNFLDraftables(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, 'tests/files/draftables/41793/upcoming.json'),
                encoding="utf-8"
        ) as data_file:
            self.schema = DraftablesSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_competition_details(self):
        self.assertListEqual(
            [
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="HOU",
                        city="Houston",
                        team_id=325,
                        team_name="Texans"
                    ),
                    competition_id=5673406,
                    competition_state="Upcoming",
                    home_team=CompetitionTeam(
                        abbreviation="DET",
                        city="Detroit",
                        team_id=334,
                        team_name="Lions"
                    ),
                    name="HOU @ DET",
                    sport="NFL",
                    start_time=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                    venue="Ford Field",
                    weather=CompetitionWeather(
                        icon="cloudy",
                        is_dome=True
                    )
                ),
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="WAS",
                        city="Washington",
                        team_id=363,
                        team_name="Football Team"
                    ),
                    competition_id=5673928,
                    competition_state="Upcoming",
                    home_team=CompetitionTeam(
                        abbreviation="DAL",
                        city="Dallas",
                        team_id=331,
                        team_name="Cowboys"
                    ),
                    name="WAS @ DAL",
                    sport="NFL",
                    start_time=datetime(2020, 11, 26, 21, 30, 0, 0, tzinfo=timezone.utc),
                    venue="AT&T Stadium",
                    weather=CompetitionWeather(
                        icon="clear-day",
                        is_dome=False
                    )
                ),
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="BAL",
                        city="Baltimore",
                        team_id=366,
                        team_name="Ravens"
                    ),
                    competition_id=5674018,
                    competition_state="Upcoming",
                    home_team=CompetitionTeam(
                        abbreviation="PIT",
                        city="Pittsburgh",
                        team_id=356,
                        team_name="Steelers"
                    ),
                    name="BAL @ PIT",
                    sport="NFL",
                    start_time=datetime(2020, 11, 27, 1, 20, 0, 0, tzinfo=timezone.utc),
                    venue="Heinz Field",
                    weather=CompetitionWeather(
                        icon="cloudy",
                        is_dome=False
                    )
                ),
            ],
            self.data.competitions
        )

    def test_first_draftable_property(self):
        self.assertEqual(
            Player(
                draftable_id=15819550,
                first_name="Deshaun",
                last_name="Watson",
                display_name="Deshaun Watson",
                draft_alerts=[],
                short_name="D. Watson",
                player_id=828743,
                position="QB",
                roster_slot_id=66,
                salary=7400,
                is_swappable=True,
                is_disabled=False,
                news_status="Recent",
                player_image_50="https://dkn.gs/sports/images/nfl/players/50/18229.png",
                player_image_160="https://dkn.gs/sports/images/nfl/players/160/18229.png",
                competition=PlayerCompetitionDetails(
                    competition_id=5673406,
                    name="HOU @ DET",
                    start_time=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                ),
                team_abbreviation="HOU",
                team_id=325,
            ),
            self.data.draftables[0]
        )


class TestHistoricalGolfDraftables(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, 'tests/files/draftables/historical_golf_draftables.json'),
                encoding="utf-8"
        ) as data_file:
            self.schema = DraftablesSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)


class TestHistoricalDraftablesForDraftGroup11513(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, 'tests/files/draftables/11513.json'),
                encoding="utf-8"
        ) as data_file:
            self.schema = DraftablesSchema()
            self.data = self.schema.loads(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draftables_exist(self):
        self.assertEqual(469, len(self.data.draftables))

    def test_first_draftable(self):
        self.assertEqual(
            Player(
                competition=PlayerCompetitionDetails(
                    competition_id=5479720,
                    name="TOR @ CLE",
                    start_time=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc)
                ),
                display_name="LeBron James",
                draftable_id=7771715,
                draft_alerts=[],
                first_name="LeBron",
                is_disabled=False,
                is_swappable=False,
                last_name="James",
                news_status="Recent",
                player_id=214152,
                player_image_50="https://d327rxwuxd0q0c.cloudfront.net/m/nba_50/214152.png",
                player_image_160="https://d327rxwuxd0q0c.cloudfront.net/m/nba_retina/214152.png",
                position="SF/PF",
                roster_slot_id=22,
                salary=10300,
                short_name="L. James",
                team_abbreviation="CLE",
                team_id=5,
            ),
            self.data.draftables[0]
        )

    def test_competitions_exist(self):
        self.assertEqual(5, len(self.data.competitions))

    def test_competitions(self):
        self.assertListEqual(
            [
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="TOR",
                        city="Toronto",
                        team_id=28,
                        team_name="Raptors"
                    ),
                    competition_id=5479720,
                    competition_state="ScoresOfficial",
                    home_team=CompetitionTeam(
                        abbreviation="CLE",
                        city="Cleveland",
                        team_id=5,
                        team_name="Cavaliers"
                    ),
                    name="TOR @ CLE",
                    sport="NBA",
                    start_time=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc),
                    venue="Quicken Loans Arena",
                    weather=CompetitionWeather(
                        icon="partly-cloudy-night",
                        is_dome=True
                    )
                ),
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="ATL",
                        city="Atlanta",
                        team_id=1,
                        team_name="Hawks"
                    ),
                    competition_id=5479637,
                    competition_state="ScoresOfficial",
                    home_team=CompetitionTeam(
                        abbreviation="MIA",
                        city="Miami",
                        team_id=14,
                        team_name="Heat"
                    ),
                    name="ATL @ MIA",
                    sport="NBA",
                    start_time=datetime(2016, 11, 16, 0, 30, 0, 0, tzinfo=timezone.utc),
                    venue="AmericanAirlines Arena",
                    weather=None
                ),
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="CHA",
                        city="Charlotte",
                        team_id=5312,
                        team_name="Hornets"
                    ),
                    competition_id=5479280,
                    competition_state="ScoresOfficial",
                    home_team=CompetitionTeam(
                        abbreviation="MIN",
                        city="Minnesota",
                        team_id=16,
                        team_name="Timberwolves"
                    ),
                    name="CHA @ MIN",
                    sport="NBA",
                    start_time=datetime(2016, 11, 16, 1, 0, 0, 0, tzinfo=timezone.utc),
                    venue="Target Center",
                    weather=None
                ),
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="CHI",
                        city="Chicago",
                        team_id=4,
                        team_name="Bulls"
                    ),
                    competition_id=5479968,
                    competition_state="ScoresOfficial",
                    home_team=CompetitionTeam(
                        abbreviation="POR",
                        city="Portland",
                        team_id=22,
                        team_name="Trail Blazers"
                    ),
                    name="CHI @ POR",
                    sport="NBA",
                    start_time=datetime(2016, 11, 16, 3, 0, 0, 0, tzinfo=timezone.utc),
                    venue="Moda Center at the Rose Quarter",
                    weather=None
                ),
                Competition(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam(
                        abbreviation="BKN",
                        city="Brooklyn",
                        team_id=17,
                        team_name="Nets"
                    ),
                    competition_id=5480294,
                    competition_state="ScoresOfficial",
                    home_team=CompetitionTeam(
                        abbreviation="LAL",
                        city="Los Angeles",
                        team_id=13,
                        team_name="Lakers"
                    ),
                    name="BKN @ LAL",
                    sport="NBA",
                    start_time=datetime(2016, 11, 16, 3, 30, 0, 0, tzinfo=timezone.utc),
                    venue="Staples Center",
                    weather=None
                )
            ],
            self.data.competitions
        )


class TestPostponedPlayer(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, 'tests/files/draftables/postponed_player.json'),
                encoding="utf-8"
        ) as data_file:
            self.schema = PlayerSchema()
            self.data = self.schema.loads(data_file.read())

    def test_draft_alerts(self):
        self.assertListEqual(
            [
                DraftAlert(
                    alert_type="Postponed Game Alert",
                    message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points"
                            " in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                    updated_date=datetime(2020, 11, 25, 18, 51, 42, 0, tzinfo=timezone.utc),
                    priority=100
                ),
            ],
            self.data.draft_alerts
        )
