from draftkings_client.data.translators.available_player_translator import AvailablePlayerTranslator


class AvailablePlayersTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        if 'playerList' not in response:
            raise KeyError('missing playerList field')

        available_players = []
        players = response['playerList']
        for player in players:
            available_players.append(AvailablePlayerTranslator.translate(response=player))

        return available_players
