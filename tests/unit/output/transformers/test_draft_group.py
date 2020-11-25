from datetime import datetime, timezone
from unittest import TestCase

from draft_kings.output.objects.draft_group import ContestDetails, LeagueDetails, StartTimeDetails, GameDetails
from draft_kings.output.transformers.draft_group import transform_contest, transform_league, \
    transform_draft_group_start_time_details, transform_game
from draft_kings.response.objects.draft_group import ContestType, League, DraftGroup, Game


class TestTransformContest(TestCase):
    def test_transform_present_values(self):
        self.assertEqual(
            ContestDetails(game_type_description="jaebaebae", type_id=1),
            transform_contest(ContestType(game_type="jaebaebae", contest_type_id=1))
        )

    def test_transform_none_values(self):
        self.assertEqual(
            ContestDetails(game_type_description=None, type_id=None),
            transform_contest(ContestType(game_type=None, contest_type_id=None))
        )


class TestTransformLeague(TestCase):
    def test_transform_present_values(self):
        self.assertEqual(
            LeagueDetails(
                abbreviation="jaebaebae",
                league_id=1,
                name="bae jadley"
            ),
            transform_league(
                League(
                    league_abbreviation="jaebaebae",
                    league_id=1,
                    league_name="bae jadley"
                )
            )
        )

    def test_transform_none_values(self):
        self.assertEqual(
            LeagueDetails(
                abbreviation=None,
                league_id=None,
                name=None
            ),
            transform_league(
                League(
                    league_abbreviation=None,
                    league_id=None,
                    league_name=None
                )
            )
        )


class TestTransformDraftGroupStartTimeDetails(TestCase):
    def setUp(self) -> None:
        self.maximum_starts_at = datetime(2020, 11, 24, 1, 30, 0, 0, tzinfo=timezone.utc)
        self.minimum_starts_at = datetime(2020, 11, 24, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.start_time_type = "jaebaebae"

    def test_when_max_start_time_is_none(self):
        self.assertEqual(
            StartTimeDetails(
                maximum=None,
                minimum=self.minimum_starts_at,
                type_description=self.start_time_type
            ),
            transform_draft_group_start_time_details(
                DraftGroup(
                    contest_type=ContestType(
                        contest_type_id=1,
                        game_type="some game type"
                    ),
                    draft_group_id=2,
                    draft_group_state="some draft group state",
                    games=[],
                    leagues=[],
                    max_start_time=None,
                    min_start_time=self.minimum_starts_at,
                    sport_id=3,
                    start_time_type=self.start_time_type
                )
            )
        )

    def test_when_min_start_time_is_none(self):
        self.assertEqual(
            StartTimeDetails(
                maximum=self.maximum_starts_at,
                minimum=None,
                type_description=self.start_time_type
            ),
            transform_draft_group_start_time_details(
                DraftGroup(
                    contest_type=ContestType(
                        contest_type_id=1,
                        game_type="some game type"
                    ),
                    draft_group_id=2,
                    draft_group_state="some draft group state",
                    games=[],
                    leagues=[],
                    max_start_time=self.maximum_starts_at,
                    min_start_time=None,
                    sport_id=3,
                    start_time_type=self.start_time_type
                )
            )
        )

    def test_when_min_and_max_start_times_are_not_none(self):
        self.assertEqual(
            StartTimeDetails(
                maximum=self.maximum_starts_at,
                minimum=self.minimum_starts_at,
                type_description=self.start_time_type
            ),
            transform_draft_group_start_time_details(
                DraftGroup(
                    contest_type=ContestType(
                        contest_type_id=1,
                        game_type="some game type"
                    ),
                    draft_group_id=2,
                    draft_group_state="some draft group state",
                    games=[],
                    leagues=[],
                    max_start_time=self.maximum_starts_at,
                    min_start_time=self.minimum_starts_at,
                    sport_id=3,
                    start_time_type=self.start_time_type
                )
            )
        )


class TestGameTransformer(TestCase):
    def test_transforming_present_values(self):
        self.assertEqual(
            GameDetails(
                away_team_id=1,
                description="some description",
                game_id=2,
                home_team_id=3,
                location="some location",
                name="some name",
                starts_at=datetime(2020, 11, 24, 2, 0, 0, 0, tzinfo=timezone.utc),
                status_description="some status"
            ),
            transform_game(
                Game(
                    away_team_id=1,
                    description="some description",
                    game_id=2,
                    home_team_id=3,
                    location="some location",
                    name="some name",
                    start_date=datetime(2020, 11, 24, 2, 0, 0, 0, tzinfo=timezone.utc),
                    status="some status"
                )
            )
        )

    def test_transforming_none_values(self):
        self.assertEqual(
            GameDetails(
                away_team_id=None,
                description=None,
                game_id=None,
                home_team_id=None,
                location=None,
                name=None,
                starts_at=None,
                status_description=None
            ),
            transform_game(
                Game(
                    away_team_id=None,
                    description=None,
                    game_id=None,
                    home_team_id=None,
                    location=None,
                    name=None,
                    start_date=None,
                    status=None
                )
            )
        )
