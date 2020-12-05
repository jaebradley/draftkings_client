from datetime import datetime
from typing import Callable, Optional

from draft_kings.data import Sport
from draft_kings.output.objects.contests import DraftGroupDetails, EntriesDetails, ContestDetails, ContestsDetails
from draft_kings.response.objects.contests import Contests as ResponseContests, DraftGroup as ResponseDraftGroup, \
    Contest as ResponseContest


class DraftGroupTransformer:
    def __init__(self, sport_abbreviation_transformer: Callable[[Optional[str]], Optional[Sport]]):
        self.sport_abbreviation_transformer = sport_abbreviation_transformer

    def transform(self, draft_group_response: ResponseDraftGroup) -> DraftGroupDetails:
        return DraftGroupDetails(
            draft_group_id=draft_group_response.draft_group_id,
            series_id=draft_group_response.draft_group_series_id,
            contest_type_id=draft_group_response.contest_type_id,
            sport=self.sport_abbreviation_transformer(draft_group_response.sport),
            starts_at=draft_group_response.start_date,
            games_count=draft_group_response.game_count
        )


class ContestTransformer:
    def __init__(self, formatted_datetime_transformer: Callable[[Optional[str]], Optional[datetime]],
                 sport_id_transformer: Callable[[Optional[int]], Optional[Sport]]):
        self.formatted_datetime_transformer = formatted_datetime_transformer
        self.sport_id_transformer = sport_id_transformer

    def transform(self, contest_response: ResponseContest) -> ContestDetails:
        return ContestDetails(
            contest_id=contest_response.contest_id,
            draft_group_id=contest_response.draft_group_id,
            entries_details=EntriesDetails(
                maximum=contest_response.entry_maximum,
                fee=contest_response.entry_fee,
                total=contest_response.entry_total
            ),
            fantasy_player_points=contest_response.fantasy_player_points,
            is_double_up=contest_response.attributes is not None and contest_response.attributes.is_double_up is True,
            is_fifty_fifty=contest_response.attributes is not None
            and contest_response.attributes.is_fifty_fifty is True,
            is_guaranteed=contest_response.attributes is not None and contest_response.attributes.is_guaranteed is True,
            is_head_to_head=contest_response.attributes is not None and contest_response.attributes.is_h2h is True,
            is_starred=contest_response.attributes is not None and contest_response.attributes.is_starred is True,
            name=contest_response.name,
            payout=contest_response.payout,
            sport=self.sport_id_transformer(contest_response.sport_id),
            starts_at=self.formatted_datetime_transformer(contest_response.starts_at),
        )


class ContestsDetailsTransformer:
    def __init__(self, contest_transformer: ContestTransformer,
                 draft_group_transformer: DraftGroupTransformer) -> None:
        self.contest_transformer = contest_transformer
        self.draft_group_transformer = draft_group_transformer

    def transform(self, response: ResponseContests) -> ContestsDetails:
        return ContestsDetails(
            contests=list(map(self.contest_transformer.transform, response.contests)),
            draft_groups=list(map(self.draft_group_transformer.transform, response.draft_groups))
        )
