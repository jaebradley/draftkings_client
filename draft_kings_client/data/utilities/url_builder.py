class UrlBuilder:

    base_url = 'https://www.draftkings.com'
    base_api_url = 'https://api.draftkings.com'
    contest_suffix = '/lobby/getcontests'
    get_available_players_suffix = '/lineup/getavailableplayers'
    get_draft_group_suffix = '/draftgroups/v1/'

    def __init__(self):
        pass


    @staticmethod
    def get_contest_url():
        return UrlBuilder.base_url + UrlBuilder.contest_suffix

    @staticmethod
    def get_available_players_url():
        return UrlBuilder.base_url + UrlBuilder.get_available_players_suffix

    @staticmethod
    def get_draft_group_url(draft_group_id):
        return UrlBuilder.base_api_url + UrlBuilder.get_draft_group_suffix + str(draft_group_id)
