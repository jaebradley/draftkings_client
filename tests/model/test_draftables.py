import os
from datetime import datetime, timezone
from unittest import TestCase

from draft_kings import Sport
from draft_kings.model.draftables import (
    Competition,
    Player,
    PlayerCompetitionDetails,
    CompetitionWeather,
    CompetitionTeam,
    DraftAlert,
    Draftables,
    Team,
    Image,
    Name,
)
from tests.config import ROOT_DIRECTORY


class TestUpcomingNFLDraftables(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draftables/41793/upcoming.json"), encoding="utf-8"
        ) as data_file:
            self.data: Draftables = Draftables.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_competition_details(self):
        self.assertListEqual(
            [
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="HOU", city="Houston", team_id=325, name="Texans"
                    ),
                    competition_id=5673406,
                    state_description="Upcoming",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="DET", city="Detroit", team_id=334, name="Lions"
                    ),
                    name="HOU @ DET",
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                    venue="Ford Field",
                    weather=CompetitionWeather.model_construct(description="cloudy", is_in_a_dome=True),
                ),
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="WAS", city="Washington", team_id=363, name="Football Team"
                    ),
                    competition_id=5673928,
                    state_description="Upcoming",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="DAL", city="Dallas", team_id=331, name="Cowboys"
                    ),
                    name="WAS @ DAL",
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 11, 26, 21, 30, 0, 0, tzinfo=timezone.utc),
                    venue="AT&T Stadium",
                    weather=CompetitionWeather.model_construct(description="clear-day", is_in_a_dome=False),
                ),
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="BAL", city="Baltimore", team_id=366, name="Ravens"
                    ),
                    competition_id=5674018,
                    state_description="Upcoming",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="PIT", city="Pittsburgh", team_id=356, name="Steelers"
                    ),
                    name="BAL @ PIT",
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 11, 27, 1, 20, 0, 0, tzinfo=timezone.utc),
                    venue="Heinz Field",
                    weather=CompetitionWeather.model_construct(description="cloudy", is_in_a_dome=False),
                ),
            ],
            self.data.competitions,
        )

    def test_first_draftable_property(self):
        self.assertEqual(
            Player.model_construct(
                competition_details=PlayerCompetitionDetails.model_construct(
                    competition_id=5673406,
                    name="HOU @ DET",
                    start_time=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                ),
                draftable_id=15819550,
                draft_alerts=[],
                image=Image.model_construct(
                    player_image_50="https://dkn.gs/sports/images/nfl/players/50/18229.png",
                    player_image_160="https://dkn.gs/sports/images/nfl/players/160/18229.png",
                ),
                is_swappable=True,
                is_disabled=False,
                name=Name.model_construct(
                    first="Deshaun",
                    last="Watson",
                    display="Deshaun Watson",
                    short="D. Watson",
                ),
                news_status_description="Recent",
                player_id=828743,
                position_name="QB",
                roster_slot_id=66,
                salary=7400,
                team=Team.model_construct(
                    abbreviation="HOU",
                    team_id=325,
                ),
            ),
            self.data.players[0],
        )


class TestHistoricalGolfDraftables(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draftables/historical_golf_draftables.json"), encoding="utf-8"
        ) as data_file:
            self.data: Draftables = Draftables.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)


class TestHistoricalDraftablesForDraftGroup11513(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(ROOT_DIRECTORY, "tests/files/draftables/11513.json"), encoding="utf-8") as data_file:
            self.data: Draftables = Draftables.model_validate_json(data_file.read())

    def test_deserialization(self) -> None:
        self.assertIsNotNone(self.data)

    def test_draftables_exist(self):
        self.assertEqual(469, len(self.data.players))

    def test_first_draftable(self):
        self.assertEqual(
            Player.model_construct(
                competition_details=PlayerCompetitionDetails.model_construct(
                    competition_id=5479720,
                    name="TOR @ CLE",
                    start_time=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc),
                ),
                draftable_id=7771715,
                draft_alerts=[],
                image=Image.model_construct(
                    player_image_50="https://d327rxwuxd0q0c.cloudfront.net/m/nba_50/214152.png",
                    player_image_160="https://d327rxwuxd0q0c.cloudfront.net/m/nba_retina/214152.png",
                ),
                is_disabled=False,
                is_swappable=False,
                name=Name.model_construct(
                    display="LeBron James",
                    first="LeBron",
                    last="James",
                    short="L. James",
                ),
                news_status_description="Recent",
                player_id=214152,
                position_name="SF/PF",
                roster_slot_id=22,
                salary=10300,
                team=Team.model_construct(
                    abbreviation="CLE",
                    team_id=5,
                ),
            ),
            self.data.players[0],
        )

    def test_competitions_exist(self):
        self.assertEqual(5, len(self.data.competitions))

    def test_competitions(self):
        self.assertListEqual(
            [
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="TOR", city="Toronto", team_id=28, name="Raptors"
                    ),
                    competition_id=5479720,
                    state_description="ScoresOfficial",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="CLE", city="Cleveland", team_id=5, name="Cavaliers"
                    ),
                    name="TOR @ CLE",
                    sport=Sport.NBA,
                    starts_at=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc),
                    venue="Quicken Loans Arena",
                    weather=CompetitionWeather.model_construct(description="partly-cloudy-night", is_in_a_dome=True),
                ),
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="ATL", city="Atlanta", team_id=1, name="Hawks"
                    ),
                    competition_id=5479637,
                    state_description="ScoresOfficial",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="MIA", city="Miami", team_id=14, name="Heat"
                    ),
                    name="ATL @ MIA",
                    sport=Sport.NBA,
                    starts_at=datetime(2016, 11, 16, 0, 30, 0, 0, tzinfo=timezone.utc),
                    venue="AmericanAirlines Arena",
                    weather=None,
                ),
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="CHA", city="Charlotte", team_id=5312, name="Hornets"
                    ),
                    competition_id=5479280,
                    state_description="ScoresOfficial",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="MIN", city="Minnesota", team_id=16, name="Timberwolves"
                    ),
                    name="CHA @ MIN",
                    sport=Sport.NBA,
                    starts_at=datetime(2016, 11, 16, 1, 0, 0, 0, tzinfo=timezone.utc),
                    venue="Target Center",
                    weather=None,
                ),
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="CHI", city="Chicago", team_id=4, name="Bulls"
                    ),
                    competition_id=5479968,
                    state_description="ScoresOfficial",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="POR", city="Portland", team_id=22, name="Trail Blazers"
                    ),
                    name="CHI @ POR",
                    sport=Sport.NBA,
                    starts_at=datetime(2016, 11, 16, 3, 0, 0, 0, tzinfo=timezone.utc),
                    venue="Moda Center at the Rose Quarter",
                    weather=None,
                ),
                Competition.model_construct(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeam.model_construct(
                        abbreviation="BKN", city="Brooklyn", team_id=17, name="Nets"
                    ),
                    competition_id=5480294,
                    state_description="ScoresOfficial",
                    home_team=CompetitionTeam.model_construct(
                        abbreviation="LAL", city="Los Angeles", team_id=13, name="Lakers"
                    ),
                    name="BKN @ LAL",
                    sport=Sport.NBA,
                    starts_at=datetime(2016, 11, 16, 3, 30, 0, 0, tzinfo=timezone.utc),
                    venue="Staples Center",
                    weather=None,
                ),
            ],
            self.data.competitions,
        )


class TestPostponedPlayer(TestCase):
    def setUp(self) -> None:
        with open(
            os.path.join(ROOT_DIRECTORY, "tests/files/draftables/postponed_player.json"), encoding="utf-8"
        ) as data_file:
            self.data: Player = Player.model_validate_json(data_file.read())

    def test_draft_alerts(self):
        self.assertListEqual(
            [
                DraftAlert.model_construct(
                    alert_description="Postponed Game Alert",
                    message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points"
                    " in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                    updated_at=datetime(2020, 11, 25, 18, 51, 42, 0, tzinfo=timezone.utc),
                    priority_value=100,
                ),
            ],
            self.data.draft_alerts,
        )
