from unittest import TestCase
from unittest.mock import Mock
from datetime import datetime

from draft_kings.data import Sport
from draft_kings.output.objects.contests import DraftGroup
from draft_kings.response.objects.contests import DraftGroup as ResponseDraftGroup
from draft_kings.output.transformers.contests import DraftGroupTransformer


class TestDraftGroupTransformer(TestCase):
    def test_when_sport_abbreviation_transformer_returns_a_sport_value(self):
        self.assertEqual(
            DraftGroup(
                draft_group_id=1,
                series_id=2,
                contest_type_id=3,
                sport=Sport.NFL,
                starts_at=datetime(2020, 11, 23, 5, 30, 0, 0),
                games_count=4
            ),
            DraftGroupTransformer(
                sport_abbreviation_transformer=Mock(return_value=Sport.NFL)
            ).transform(
                ResponseDraftGroup(
                    draft_group_id=1,
                    draft_group_series_id=2,
                    contest_type_id=3,
                    sport="NFL",
                    start_date=datetime(2020, 11, 23, 5, 30, 0, 0),
                    game_count=4
                )
            )
        )

    def test_when_sport_abbreviation_transformer_does_not_return_a_sport_value(self):
        self.assertEqual(
            DraftGroup(
                draft_group_id=1,
                series_id=2,
                contest_type_id=3,
                sport=None,
                starts_at=datetime(2020, 11, 23, 5, 30, 0, 0),
                games_count=4
            ),
            DraftGroupTransformer(
                sport_abbreviation_transformer=Mock(return_value=None)
            ).transform(
                ResponseDraftGroup(
                    draft_group_id=1,
                    draft_group_series_id=2,
                    contest_type_id=3,
                    sport="NFL",
                    start_date=datetime(2020, 11, 23, 5, 30, 0, 0),
                    game_count=4
                )
            )
        )

