from typing import List, Callable

from draft_kings.data import SPORT_ID_TO_SPORT, CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS
from draft_kings.output.objects import ContestDraftGroup, ContestEntryDetails, Contest, ContestsDetails
from draft_kings.response.objects import Contests as ContestsResponse, DraftGroup as DraftGroupResponseObject, \
    Contest as ContestResponseObject
from draft_kings.utilities import translate_formatted_datetime


def transform_draft_group(draft_group_response: DraftGroupResponseObject) -> ContestDraftGroup:
    return ContestDraftGroup(
        draft_group_id=draft_group_response.draft_group_id,
        series_id=draft_group_response.draft_group_series_id,
        contest_type_id=draft_group_response.contest_type_id,
        sport=CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS.get(draft_group_response.sport),
        starts_at=draft_group_response.start_date,
        games_count=draft_group_response.game_count
    )


class DraftGroupsTransformer:
    def __init__(self, draft_group_transformer: Callable[[DraftGroupResponseObject], ContestDraftGroup]) -> None:
        self.draft_group_transformer = draft_group_transformer

    def transform(self, draft_groups_response: List[DraftGroupResponseObject]) -> List[ContestDraftGroup]:
        return list(map(lambda draft_group_data: self.draft_group_transformer(draft_group_data), draft_groups_response))


def transform_contest(contest_response: ContestResponseObject) -> Contest:
    return Contest(
        contest_id=contest_response.contest_id,
        draft_group_id=contest_response.draft_group_id,
        entry_details=ContestEntryDetails(
            maximum=contest_response.entry_maximum,
            fee=contest_response.entry_fee,
            total=contest_response.entry_total
        ),
        fantasy_player_points=contest_response.fantasy_player_points,
        is_double_up=contest_response.attributes.is_double_up is True,
        is_fifty_fifty=contest_response.attributes.is_fifty_fifty is True,
        is_guaranteed=contest_response.attributes.is_guaranteed is True,
        is_head_to_head=contest_response.attributes.is_h2h is True,
        is_starred=contest_response.attributes.is_starred is True,
        name=contest_response.name,
        payout=contest_response.payout,
        sport=SPORT_ID_TO_SPORT.get(contest_response.sport_id),
        starts_at=translate_formatted_datetime(contest_response.starts_at),
    )


class ContestsResponseTransformer:
    def __init__(self, contest_transformer: Callable[[ContestResponseObject], Contest]) -> None:
        self.contest_transformer = contest_transformer

    def transform(self, contests_response: List[ContestResponseObject]) -> List[Contest]:
        return list(map(lambda contest_data: self.contest_transformer(contest_data), contests_response))


class ContestsDetailsResponseTransformer:
    def __init__(self, contests_transformer: ContestsResponseTransformer, groups_transformer: DraftGroupsTransformer) -> None:
        self.contests_transformer = contests_transformer
        self.groups_transformer = groups_transformer

    def transform(self, response: ContestsResponse) -> ContestsDetails:
        contests_details = ContestsDetails(
            contests=self.contests_transformer.transform(response.contests),
            groups=self.groups_transformer.transform(response.draft_groups)
        )
        return contests_details

