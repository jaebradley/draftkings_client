from draft_kings_client.data.models.contests import Contests
from draft_kings_client.data.translators.contest_response_translator import ContestResponseTranslator
from draft_kings_client.data.translators.draft_groups_translator import DraftGroupsTranslator


class ContestsResponseTranslator:

    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        if 'SelectedSport' not in response:
            raise KeyError('Missing SelectedSport field')

        if 'Contests' not in response:
            raise KeyError('Missing Contests field')

        if 'DraftGroups' not in response:
            raise KeyError('Missing DraftGroups field')

        contests = []
        for contest in response['Contests']:
            contests.append(ContestResponseTranslator.translate(response=contest))

        groups = DraftGroupsTranslator.translate_groups(groups=response['DraftGroups'])

        return Contests(contests=contests, draft_groups=groups)
