from datetime import datetime, timezone

import pytest

from pytest import param

from draft_kings import Sport
from draft_kings.model.draft_group import DraftGroup, StartTime, Contest
from draft_kings.model.draft_group import League, Game
from tests.utilities import read_fixture


@pytest.fixture
def under_test(request) -> DraftGroup:
    return DraftGroup.model_validate_json(read_fixture(f"draft_group_details/{request.param}"))


@pytest.mark.parametrize(
    "under_test, expected",
    [
        param(
            "26545_upcoming",
            DraftGroup.model_construct(
                contest_details=Contest.model_construct(type_id=29, game_type_description="SalaryCap"),
                draft_group_id=26545,
                sport=Sport.GOLF,
                start_time=StartTime.model_construct(
                    maximum=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    minimum=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    type_description="Normal",
                ),
                draft_group_state="Upcoming",
                leagues=[
                    League.model_construct(abbreviation="PGA", league_id=26, name="Professional Golf Association")
                ],
                games=[
                    Game.model_construct(
                        away_team_id=-5,
                        description="Wells Fargo Championship",
                        game_id=5559805,
                        home_team_id=-5,
                        location="Quail Hollow Club",
                        name="Wells Fargo Championship",
                        starts_at=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                        status_description="Upcoming",
                    )
                ],
            ),
            id="golf_upcoming",
        ),
        param(
            "26545_historical",
            DraftGroup.model_construct(
                contest_details=Contest.model_construct(type_id=29, game_type_description="SalaryCap"),
                draft_group_id=26545,
                sport=Sport.GOLF,
                start_time=StartTime.model_construct(
                    maximum=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    minimum=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                    type_description="Normal",
                ),
                draft_group_state="Historical",
                leagues=[
                    League.model_construct(abbreviation="PGA", league_id=26, name="Professional Golf Association")
                ],
                games=[
                    Game.model_construct(
                        away_team_id=-5,
                        description="Wells Fargo Championship",
                        game_id=5559805,
                        home_team_id=-5,
                        location="Quail Hollow Club",
                        name="Wells Fargo Championship",
                        starts_at=datetime(2019, 5, 2, 11, 0, 0, 0, tzinfo=timezone.utc),
                        status_description="ScoresOfficial",
                    )
                ],
            ),
            id="golf_historical",
        ),
        param(
            "41409_upcoming",
            DraftGroup.model_construct(
                contest_details=Contest.model_construct(type_id=96, game_type_description="SalaryCap"),
                draft_group_id=41409,
                sport=Sport.NFL,
                start_time=StartTime.model_construct(
                    type_description="Normal",
                    minimum=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    maximum=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                ),
                draft_group_state="Upcoming",
                leagues=[League.model_construct(abbreviation="NFL", league_id=1, name="National Football League")],
                games=[
                    Game.model_construct(
                        away_team_id=347,
                        description="MIN @ CHI",
                        game_id=5673706,
                        home_team_id=326,
                        location="Soldier Field",
                        name=None,
                        starts_at=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                        status_description="Pre-Game",
                    )
                ],
            ),
            id="nfl_upcoming",
        ),
        param(
            "41409_historical",
            DraftGroup.model_construct(
                contest_details=Contest.model_construct(type_id=96, game_type_description="SalaryCap"),
                draft_group_id=41409,
                sport=Sport.NFL,
                start_time=StartTime.model_construct(
                    minimum=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    maximum=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                    type_description="Normal",
                ),
                draft_group_state="Historical",
                leagues=[League.model_construct(abbreviation="NFL", league_id=1, name="National Football League")],
                games=[
                    Game.model_construct(
                        away_team_id=347,
                        description="MIN @ CHI",
                        game_id=5673706,
                        home_team_id=326,
                        location="Soldier Field",
                        name=None,
                        starts_at=datetime(2020, 11, 17, 1, 15, 0, 0, tzinfo=timezone.utc),
                        status_description="Final",
                    )
                ],
            ),
            id="nfl_historical",
        ),
    ],
    indirect=["under_test"],
)
def test_draft_group(under_test: DraftGroup, expected: DraftGroup) -> None:
    assert under_test is not None
    assert under_test == expected
