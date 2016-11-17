class UrlBuilder:

    base_url = 'https://www.draftkings.com'
    contest_suffix = '/lobby/getcontests'
    get_available_players_suffix = '/lineup/getavailableplayers'

    def __init__(self):
        pass


    @staticmethod
    def get_contest_url():
        return UrlBuilder.base_url + UrlBuilder.contest_suffix

    @staticmethod
    def get_available_players_url():
        return UrlBuilder.base_url + UrlBuilder.get_available_players_suffix