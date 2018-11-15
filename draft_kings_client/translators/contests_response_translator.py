from draft_kings_client.translators.contest_response_translator import translate as translate_contest
from draft_kings_client.translators.draft_groups_translator import translate as translate_draft_groups


def translate(response):
    return {
        "contests": [translate_contest(contest) for contest in response["Contests"]],
        "groups": [translate_draft_groups(response["DraftGroups"])],
    }
