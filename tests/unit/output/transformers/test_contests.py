from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import Mock

from draft_kings.data import Sport
from draft_kings.output.objects.contests import DraftGroupDetails, ContestDetails, EntriesDetails
from draft_kings.output.transformers.contests import DraftGroupTransformer, ContestTransformer
from draft_kings.response.objects.contests import DraftGroup as ResponseDraftGroup, Contest as ResponseContest, \
    ContestAttributes as ResponseContestAttributes


class TestDraftGroupTransformer(TestCase):
    def test_when_sport_abbreviation_transformer_returns_a_sport_value(self):
        self.assertEqual(
            DraftGroupDetails(
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
            DraftGroupDetails(
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


class TestContestTransformerWhenSportAndFormattedDateTimeAreIdentifiable(TestCase):
    def setUp(self) -> None:
        self.identified_start_time = datetime(2020, 11, 26, 11, 30, 0, 0, tzinfo=timezone.utc)
        self.identified_sport = Sport.NBA
        self.transformer = ContestTransformer(
            formatted_datetime_transformer=Mock(return_value=self.identified_start_time),
            sport_id_transformer=Mock(return_value=self.identified_sport)
        )

    def test_when_contest_attributes_do_not_exist(self):
        self.assertEqual(
            ContestDetails(
                contest_id=1,
                draft_group_id=2,
                entries_details=EntriesDetails(
                    maximum=3,
                    fee=4,
                    total=5
                ),
                fantasy_player_points=6,
                is_double_up=False,
                is_fifty_fifty=False,
                is_guaranteed=False,
                is_head_to_head=False,
                is_starred=False,
                name="Some Contest",
                payout=7,
                sport=self.identified_sport,
                starts_at=self.identified_start_time
            ),
            self.transformer.transform(
                ResponseContest(
                    attributes=None,
                    contest_id=1,
                    draft_group_id=2,
                    entry_fee=4,
                    entry_maximum=3,
                    entry_total=5,
                    fantasy_player_points=6,
                    name="Some Contest",
                    payout=7,
                    sport_id=1,
                    starts_at="some start time"
                )
            )
        )

    def test_when_contest_attributes_exist_and_are_false(self):
        self.assertEqual(
            ContestDetails(
                contest_id=1,
                draft_group_id=2,
                entries_details=EntriesDetails(
                    maximum=3,
                    fee=4,
                    total=5
                ),
                fantasy_player_points=6,
                is_double_up=False,
                is_fifty_fifty=False,
                is_guaranteed=False,
                is_head_to_head=False,
                is_starred=False,
                name="Some Contest",
                payout=7,
                sport=self.identified_sport,
                starts_at=self.identified_start_time
            ),
            self.transformer.transform(
                ResponseContest(
                    attributes=ResponseContestAttributes(
                        is_double_up=False,
                        is_fifty_fifty=False,
                        is_guaranteed=False,
                        is_h2h=False,
                        is_starred=False
                    ),
                    contest_id=1,
                    draft_group_id=2,
                    entry_fee=4,
                    entry_maximum=3,
                    entry_total=5,
                    fantasy_player_points=6,
                    name="Some Contest",
                    payout=7,
                    sport_id=1,
                    starts_at="some start time"
                )
            )
        )

    def test_when_contest_attributes_exist_and_are_none(self):
        self.assertEqual(
            ContestDetails(
                contest_id=1,
                draft_group_id=2,
                entries_details=EntriesDetails(
                    maximum=3,
                    fee=4,
                    total=5
                ),
                fantasy_player_points=6,
                is_double_up=False,
                is_fifty_fifty=False,
                is_guaranteed=False,
                is_head_to_head=False,
                is_starred=False,
                name="Some Contest",
                payout=7,
                sport=self.identified_sport,
                starts_at=self.identified_start_time
            ),
            self.transformer.transform(
                ResponseContest(
                    attributes=ResponseContestAttributes(
                        is_double_up=None,
                        is_fifty_fifty=None,
                        is_guaranteed=None,
                        is_h2h=None,
                        is_starred=None
                    ),
                    contest_id=1,
                    draft_group_id=2,
                    entry_fee=4,
                    entry_maximum=3,
                    entry_total=5,
                    fantasy_player_points=6,
                    name="Some Contest",
                    payout=7,
                    sport_id=1,
                    starts_at="some start time"
                )
            )
        )

    def test_when_contest_attributes_exist_and_are_true(self):
        self.assertEqual(
            ContestDetails(
                contest_id=1,
                draft_group_id=2,
                entries_details=EntriesDetails(
                    maximum=3,
                    fee=4,
                    total=5
                ),
                fantasy_player_points=6,
                is_double_up=True,
                is_fifty_fifty=True,
                is_guaranteed=True,
                is_head_to_head=True,
                is_starred=True,
                name="Some Contest",
                payout=7,
                sport=self.identified_sport,
                starts_at=self.identified_start_time
            ),
            self.transformer.transform(
                ResponseContest(
                    attributes=ResponseContestAttributes(
                        is_double_up=True,
                        is_fifty_fifty=True,
                        is_guaranteed=True,
                        is_h2h=True,
                        is_starred=True
                    ),
                    contest_id=1,
                    draft_group_id=2,
                    entry_fee=4,
                    entry_maximum=3,
                    entry_total=5,
                    fantasy_player_points=6,
                    name="Some Contest",
                    payout=7,
                    sport_id=1,
                    starts_at="some start time"
                )
            )
        )
