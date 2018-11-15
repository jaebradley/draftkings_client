from draft_kings_client.translators.available_player_translator import translate as translate_player
from draft_kings_client.translators.available_players_team_series_translator import translate as translate_team_series


def translate(response):
    return {
        "players": [translate_player(response=player) for player in response['playerList']],
        "team_series_list": [
            translate_team_series(team_series_id=team_series_id, details=details)
            for team_series_id, details in response['teamList'].items()
        ]
    }
