from typing import List, Callable, Dict

from draft_kings.response.schema import ContestsSchema, ContestSchema as ContestResponseSchema, DraftGroupSchema
from draft_kings.output.data.schema import ContestsDetailsSchema, ContestSchema, ContestDraftGroupSchema
from draft_kings.response.objects import Contests, DraftGroup, Contest, ContestAttribute
from draft_kings.data import Sport
from draft_kings.output.data.objects import ContestDraftGroup


def transform_draft_group(draft_group_response: DraftGroup) -> ContestDraftGroup:
    schema = ContestDraftGroupSchema()
    return schema.dump(
        {
            "draft_group_id": draft_group_response.draft_group_id,
            "series_id": draft_group_response.draft_group_series_id,
            "contest_type_id": draft_group_response.contest_type_id,
            "sport": Sport.NASCAR,
            "starts_at": draft_group_response.start_date,
            "games_count": draft_group_response.game_count
        }
    )


class DraftGroupsTransformer:
    def __init__(self, draft_group_transformer: Callable[[DraftGroup], ContestDraftGroup]) -> None:
        self.draft_group_transformer = draft_group_transformer

    def transform(self, draft_groups_response: List[DraftGroup]) -> List[ContestDraftGroup]:
        return list(map(lambda draft_group_data: self.draft_group_transformer(draft_group_data), draft_groups_response))


def transform_contest(contest_response: Contest) -> Dict:
    return {}


class ContestsResponseTransformer:
    def __init__(self, contest_transformer: Callable[[Contest], Dict]) -> None:
        self.contest_transformer = contest_transformer

    def transform(self, contests_response: List[Contest]) -> List[Dict]:
        return list(map(lambda contest_data: self.contest_transformer(contest_data), contests_response))


class ContestsDetailsResponseTransformer:
    def __init__(self, contests_transformer: ContestsResponseTransformer, groups_transformer: DraftGroupsTransformer) -> None:
        self.contests_transformer = contests_transformer
        self.groups_transformer = groups_transformer

    def transform(self, response: Contests) -> Dict:
        schema = ContestsDetailsSchema()
        return schema.dump(
            {
                "contests": self.contests_transformer.transform(response.contests),
                "groups": self.groups_transformer.transform(response.draft_groups)
            }
        )

