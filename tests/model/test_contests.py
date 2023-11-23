from datetime import datetime, timezone

import pytest

from draft_kings import Sport
from draft_kings.model.contests import Contest, DraftGroup, Contests, Entries
from tests.utilities import read_fixture


class TestUpcomingNFLContests:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Contests:
        return Contests.model_validate_json(read_fixture("contests/nfl/2020_10_22"))

    def test_deserialization(self, under_test: Contests) -> None:
        assert under_test is not None

    def test_contests_exist(self, under_test: Contests) -> None:
        assert under_test.contests is not None

    def test_contests_have_a_length_greater_than_0(self, under_test: Contests) -> None:
        assert 0 < len(under_test.contests)

    def test_first_contest(self, under_test: Contests) -> None:
        assert under_test.contests[0] == Contest.model_construct(
            is_double_up=False,
            is_fifty_fifty=False,
            is_guaranteed=True,
            is_head_to_head=False,
            is_starred=True,
            contest_id=96625286,
            draft_group_id=41643,
            entries_details=Entries.model_construct(fee=20.0, maximum=205882, total=144081),
            fantasy_player_points=20.0,
            name="NFL $3.5M Fantasy Football Millionaire [$1M to 1st]",
            payout=3500000.0,
            sport=Sport.NFL,
            starts_at=datetime(2020, 11, 22, 18, 0, tzinfo=timezone.utc),
        )

    def test_draft_groups_exist(self, under_test: Contests) -> None:
        assert None is not under_test.draft_groups

    def test_draft_groups_have_a_length_greater_than_0(self, under_test: Contests) -> None:
        assert 0 < len(under_test.draft_groups)

    def test_first_draft_group(self, under_test: Contests) -> None:
        assert under_test.draft_groups[0] == DraftGroup.model_construct(
            draft_group_id=41643,
            series_id=2,
            contest_type_id=21,
            game_count=11,
            sport=Sport.NFL,
            starts_at=datetime(
                year=2020, month=11, day=22, hour=18, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
            ),
        )
