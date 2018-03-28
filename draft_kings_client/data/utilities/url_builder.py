class UrlBuilder:

    base_url = 'https://www.draftkings.com'
    base_api_url = 'https://api.draftkings.com'
    contest_suffix = '/lobby/getcontests'
    get_available_players_suffix = '/lineup/getavailableplayers'
    get_draft_group_suffix = '/draftgroups/v1/'
    get_countries_suffix = '/addresses/v1/countries'
    get_contest_details_suffix = '/contests/v1/contests/'

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

    @staticmethod
    def get_countries_url():
        return UrlBuilder.base_api_url + UrlBuilder.get_countries_suffix

    @staticmethod
    def get_regions_url(country_code):
        return UrlBuilder.base_api_url + UrlBuilder.get_countries_suffix + '/' + country_code + '/regions'

    @staticmethod
    def get_contest_details_url(contest_id):
        return UrlBuilder.base_api_url + UrlBuilder.get_contest_details_suffix + str(contest_id)

    @staticmethod
    def get_draftables_url(draft_group_id):
        return UrlBuilder.base_api_url + UrlBuilder.get_draft_group_suffix + 'draftgroups/' + str(draft_group_id) + '/draftables'
