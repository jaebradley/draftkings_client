from draftkings_client.data.translators.contest_response_translator import ContestResponseTranslator


class ContestsResponseTranslator:

    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        if 'SelectedSport' not in response:
            raise TypeError('Missing SelectedSport field')

        if 'Contests' not in response:
            raise TypeError('Missing Contests field')

        contests = []
        for contest in response.contests:
            contests.append(ContestResponseTranslator.translate(response=contest))

        return contests
