from draft_kings_client.data.translators.available_player_translator import AvailablePlayerTranslator
from draft_kings_client.data.translators.available_players_team_series_translator import AvailablePlayersTeamSeriesTranslator
from draft_kings_client.data.models.available_players import AvailablePlayers


class AvailablePlayersTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        if 'playerList' not in response:
            raise KeyError('missing playerList field')

        if 'teamList' not in response:
            raise KeyError('missing teamList field')

        available_players = []
        players = response['playerList']
        team_series_list = response['teamList']

        for player in players:
            available_players.append(AvailablePlayerTranslator.translate(response=player))

        available_team_series_list = AvailablePlayersTeamSeriesTranslator.translate(response=team_series_list)

        return AvailablePlayers(player_list=available_players, team_series_list=available_team_series_list)
