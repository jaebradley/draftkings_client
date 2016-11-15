class UrlBuilder:

    base_url = 'https://www.draftkings.com'
    contest_suffix = '/lobby/getcontests'
    player_list_suffix = '/lineup/getavailableplayers'

    def __init__(self):
        pass


    @staticmethod
    def get_contest_url():
        return UrlBuilder.base_url + UrlBuilder.contest_suffix

    @staticmethod
    def get_player_list_url():
        return UrlBuilder.base_url + UrlBuilder.player_list_suffix