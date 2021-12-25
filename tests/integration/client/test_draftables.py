import os
from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import patch, Mock

from draft_kings import Client
from draft_kings.data import Sport
from draft_kings.http_client import HTTPClient
from draft_kings.output.objects.draftables import PlayerNameDetails, PlayerImageDetails, PlayerCompetitionDetails, \
    PlayerTeamDetails, PlayerDetails, CompetitionTeamDetails, CompetitionWeatherDetails, CompetitionDetails, \
    PlayerDraftAlertDetails
from tests.config import ROOT_DIRECTORY


class TestDraftables(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_nba_draftables(self):
        draftables = self.client.draftables(draft_group_id=11513)
        self.assertIsNotNone(draftables)

    def test_nhl_draftables(self):
        draftables = self.client.draftables(draft_group_id=22953)
        self.assertIsNotNone(draftables)

    def test_nfl_draftables(self):
        draftables = self.client.draftables(draft_group_id=22927)
        self.assertIsNotNone(draftables)

    def test_cfb_draftables(self):
        draftables = self.client.draftables(draft_group_id=22952)
        self.assertIsNotNone(draftables)

    def test_cbb_draftables(self):
        draftables = self.client.draftables(draft_group_id=22958)
        self.assertIsNotNone(draftables)

    def test_soccer_uefa_national_league_draftables(self):
        draftables = self.client.draftables(draft_group_id=22855)
        self.assertIsNotNone(draftables)

    def test_soccer_epl_draftables(self):
        draftables = self.client.draftables(draft_group_id=22831)
        self.assertIsNotNone(draftables)

    def test_euroleague_draftables(self):
        draftables = self.client.draftables(draft_group_id=22916)
        self.assertIsNotNone(draftables)


class TestMockedUpcomingNFLDraftablesResponse(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, "tests/files/draftables/41793/upcoming.json"),
                encoding="utf-8"
        ) as data_file:
            self.response_data = data_file.read()
            patched_method = patch.object(HTTPClient, "draftables")
            mocked_method = patched_method.start()
            mocked_method.return_value = Mock(text=self.response_data)
            self.result = Client().draftables(draft_group_id=41793)

    def tearDown(self) -> None:
        patch.stopall()

    def test_outputs_object(self):
        self.assertIsNotNone(self.result)

    def test_competitions(self):
        self.assertListEqual(
            [
                CompetitionDetails(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeamDetails(
                        abbreviation="HOU",
                        city="Houston",
                        team_id=325,
                        name="Texans"
                    ),
                    competition_id=5673406,
                    state_description="Upcoming",
                    home_team=CompetitionTeamDetails(
                        abbreviation="DET",
                        city="Detroit",
                        team_id=334,
                        name="Lions"
                    ),
                    name="HOU @ DET",
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                    venue="Ford Field",
                    weather=CompetitionWeatherDetails(
                        description="cloudy",
                        is_in_a_dome=True
                    )
                ),
                CompetitionDetails(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeamDetails(
                        abbreviation="WAS",
                        city="Washington",
                        team_id=363,
                        name="Football Team"
                    ),
                    competition_id=5673928,
                    state_description="Upcoming",
                    home_team=CompetitionTeamDetails(
                        abbreviation="DAL",
                        city="Dallas",
                        team_id=331,
                        name="Cowboys"
                    ),
                    name="WAS @ DAL",
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 11, 26, 21, 30, 0, 0, tzinfo=timezone.utc),
                    venue="AT&T Stadium",
                    weather=CompetitionWeatherDetails(
                        description="clear-day",
                        is_in_a_dome=False
                    )
                ),
                CompetitionDetails(
                    are_depth_charts_available=True,
                    are_starting_lineups_available=False,
                    away_team=CompetitionTeamDetails(
                        abbreviation="BAL",
                        city="Baltimore",
                        team_id=366,
                        name="Ravens"
                    ),
                    competition_id=5674018,
                    state_description="Upcoming",
                    home_team=CompetitionTeamDetails(
                        abbreviation="PIT",
                        city="Pittsburgh",
                        team_id=356,
                        name="Steelers"
                    ),
                    name="BAL @ PIT",
                    sport=Sport.NFL,
                    starts_at=datetime(2020, 11, 27, 1, 20, 0, 0, tzinfo=timezone.utc),
                    venue="Heinz Field",
                    weather=CompetitionWeatherDetails(
                        description="cloudy",
                        is_in_a_dome=False
                    )
                ),
            ],
            self.result.competitions
        )

    def test_first_draftable_player(self):
        self.assertEqual(
            PlayerDetails(
                competition_details=PlayerCompetitionDetails(
                    competition_id=5673406,
                    name="HOU @ DET",
                    starts_at=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                ),
                draftable_id=15819550,
                draft_alerts=[],
                player_id=828743,
                position_name="QB",
                roster_slot_id=66,
                salary=7400,
                is_swappable=True,
                is_disabled=False,
                news_status_description="Recent",
                image_details=PlayerImageDetails(
                    fifty_pixels_by_fifty_pixels_url="https://dkn.gs/sports/images/nfl/players/50/18229.png",
                    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url
                    ="https://dkn.gs/sports/images/nfl/players/160/18229.png",
                ),
                name_details=PlayerNameDetails(
                    first="Deshaun",
                    last="Watson",
                    display="Deshaun Watson",
                    short="D. Watson",
                ),
                team_details=PlayerTeamDetails(
                    abbreviation="HOU",
                    team_id=325,
                )
            ),
            self.result.players[0]
        )


class TestDraftablesWithDraftAlerts(TestCase):
    def setUp(self) -> None:
        with open(
                os.path.join(ROOT_DIRECTORY, "tests/files/draftables/41793/postponed.json"),
                encoding="utf-8"
        ) as data_file:
            self.response_data = data_file.read()
            patched_method = patch.object(HTTPClient, "draftables")
            mocked_method = patched_method.start()
            mocked_method.return_value = Mock(text=self.response_data)
            self.result = Client().draftables(draft_group_id=41793)

    def test_player_with_draft_alerts(self):
        self.assertListEqual(
            [
                PlayerDraftAlertDetails(
                    alert_description="Postponed Game Alert",
                    message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points"
                            " in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                    updated_at=datetime(2020, 11, 25, 18, 51, 42, 0, tzinfo=timezone.utc),
                    priority_value=100
                ),
            ],
            self.result.players[5].draft_alerts
        )
