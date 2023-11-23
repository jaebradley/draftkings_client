from datetime import datetime, timezone

import pytest
from pytest import param

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
from tests.utilities import read_fixture


@pytest.fixture
def under_test(request) -> Draftables:
    return Draftables.model_validate_json(read_fixture(f"draftables/{request.param}"))


@pytest.mark.parametrize(
    "under_test, player_count, first_player, competition_count, first_competition",
    [
        param(
            "41793/upcoming",
            213,
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
                name=Name.model_construct(first="Deshaun", last="Watson", display="Deshaun Watson", short="D. Watson"),
                news_status_description="Recent",
                player_id=828743,
                position_name="QB",
                roster_slot_id=66,
                salary=7400,
                team=Team.model_construct(abbreviation="HOU", team_id=325),
            ),
            3,
            Competition.model_construct(
                are_depth_charts_available=True,
                are_starting_lineups_available=False,
                away_team=CompetitionTeam.model_construct(abbreviation="HOU", city="Houston", team_id=325, name="Texans"),
                competition_id=5673406,
                state_description="Upcoming",
                home_team=CompetitionTeam.model_construct(abbreviation="DET", city="Detroit", team_id=334, name="Lions"),
                name="HOU @ DET",
                sport=Sport.NFL,
                starts_at=datetime(2020, 11, 26, 17, 30, 0, 0, tzinfo=timezone.utc),
                venue="Ford Field",
                weather=CompetitionWeather.model_construct(description="cloudy", is_in_a_dome=True),
            ),
            id="nfl_upcoming",
        ),
        param(
            "11513",
            469,
            Player.model_construct(
                competition_details=PlayerCompetitionDetails.model_construct(
                    competition_id=5479720, name="TOR @ CLE", start_time=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc)
                ),
                draftable_id=7771715,
                draft_alerts=[],
                image=Image.model_construct(
                    player_image_50="https://d327rxwuxd0q0c.cloudfront.net/m/nba_50/214152.png",
                    player_image_160="https://d327rxwuxd0q0c.cloudfront.net/m/nba_retina/214152.png",
                ),
                is_disabled=False,
                is_swappable=False,
                name=Name.model_construct(display="LeBron James", first="LeBron", last="James", short="L. James"),
                news_status_description="Recent",
                player_id=214152,
                position_name="SF/PF",
                roster_slot_id=22,
                salary=10300,
                team=Team.model_construct(abbreviation="CLE", team_id=5),
            ),
            5,
            Competition.model_construct(
                are_depth_charts_available=True,
                are_starting_lineups_available=False,
                away_team=CompetitionTeam.model_construct(abbreviation="TOR", city="Toronto", team_id=28, name="Raptors"),
                competition_id=5479720,
                state_description="ScoresOfficial",
                home_team=CompetitionTeam.model_construct(abbreviation="CLE", city="Cleveland", team_id=5, name="Cavaliers"),
                name="TOR @ CLE",
                sport=Sport.NBA,
                starts_at=datetime(2016, 11, 16, 0, 0, 0, 0, tzinfo=timezone.utc),
                venue="Quicken Loans Arena",
                weather=CompetitionWeather.model_construct(description="partly-cloudy-night", is_in_a_dome=True),
            ),
            id="nba",
        ),
        param(
            "historical_golf_draftables",
            140,
            Player.model_construct(
                competition_details=PlayerCompetitionDetails.model_construct(
                    competition_id=5510796, name="Houston Open", start_time=datetime(2018, 3, 29, 14, 20, tzinfo=timezone.utc)
                ),
                draftable_id=10420874,
                draft_alerts=[],
                image=Image.model_construct(
                    player_image_50="https://d327rxwuxd0q0c.cloudfront.net/m/golf_50/1237.png",
                    player_image_160="https://d327rxwuxd0q0c.cloudfront.net/m/golf_retina/1237.png",
                ),
                is_disabled=False,
                is_swappable=False,
                name=Name.model_construct(display="Rickie Fowler", first="Rickie", last="Fowler", short="R. Fowler"),
                news_status_description="Recent",
                player_id=1237,
                position_name="G",
                roster_slot_id=118,
                salary=11500.0,
                team=Team.model_construct(abbreviation="Golf", team_id=-5),
            ),
            1,
            Competition.model_construct(
                are_depth_charts_available=False,
                are_starting_lineups_available=False,
                away_team=CompetitionTeam.model_construct(abbreviation="Golf", city="", name="Golf", team_id=-5),
                competition_id=5510796,
                state_description="CompetitionOver",
                home_team=CompetitionTeam.model_construct(abbreviation="Golf", city="", name="Golf", team_id=-5),
                name="Houston Open",
                sport=Sport.GOLF,
                starts_at=datetime(2018, 3, 29, 14, 20, tzinfo=timezone.utc),
                venue="Golf Club of Houston",
                weather=None,
            ),
            id="11513",
        ),
    ],
    indirect=["under_test"],
)
def test_draftable(
    under_test: Draftables,
    player_count: int,
    first_player: Player,
    competition_count: int,
    first_competition: Competition,
) -> None:
    assert under_test is not None
    assert len(under_test.competitions) == competition_count
    assert under_test.competitions[0] == first_competition
    assert len(under_test.players) == player_count
    assert under_test.players[0] == first_player


class TestHistoricalGolfDraftables:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Draftables:
        return Draftables.model_validate_json(read_fixture("draftables/historical_golf_draftables"))

    def test_deserialization(self, under_test: Draftables) -> None:
        assert under_test is not None


class TestPostponedPlayer:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Player:
        return Player.model_validate_json(read_fixture("draftables/postponed_player"))

    def test_draft_alerts(self, under_test: Player) -> None:
        assert under_test.draft_alerts == [
            DraftAlert.model_construct(
                alert_description="Postponed Game Alert",
                message="The Ravens vs. Steelers game has been postponed. Players will NOT receive fantasy points"
                " in Thursday (11/26) MAIN and TIERS contests, please check your lineups!",
                updated_at=datetime(2020, 11, 25, 18, 51, 42, 0, tzinfo=timezone.utc),
                priority_value=100,
            )
        ]
