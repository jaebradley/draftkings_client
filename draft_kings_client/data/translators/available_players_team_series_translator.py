from draft_kings_client.data.models.available_players_team_series import AvailablePlayersTeamSeries
from draft_kings_client.data.models.available_player import AvailablePlayerMatchUp, AvailablePlayerTeam
from draft_kings_client.data.translators.date_translator import DateTranslator


class AvailablePlayersTeamSeriesTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        team_series_list = []
        for key, value in response.iteritems():
            AvailablePlayersTeamSeriesTranslator.validate(team_series_data=value)
            AvailablePlayersTeamSeriesTranslator.validate_types(team_series_id=key, team_series_data=value)

            team_series_id = int(key)
            home_team_abbreviation = unicode(value['ht'])
            home_team_id = value['htid']
            away_team_abbreviation = unicode(value['at'])
            away_team_id = value['atid']
            start_timestamp = DateTranslator.translate(date_string=value['tz'])
            weather = unicode(value['wthr'])
            sport_id = value['s']
            status = value['status']

            home_team = AvailablePlayerTeam(team_id=home_team_id, team_abbreviation=home_team_abbreviation)
            away_team = AvailablePlayerTeam(team_id=away_team_id, team_abbreviation=away_team_abbreviation)
            match_up = AvailablePlayerMatchUp(home_team=home_team, away_team=away_team)
            team_series = AvailablePlayersTeamSeries(team_series_id=team_series_id, match_up=match_up,
                                                     start_timestamp=start_timestamp, weather=weather,
                                                     sport_id=sport_id, status=status)

            team_series_list.append(team_series)

        return team_series_list

    @staticmethod
    def validate(team_series_data):

        if 'ht' not in team_series_data:
            raise KeyError('missing ht field')

        if 'htid' not in team_series_data:
            raise KeyError('missing htid field')

        if 'at' not in team_series_data:
            raise KeyError('missing at field')

        if 'atid' not in team_series_data:
            raise KeyError('missing atid field')

        if 'tz' not in team_series_data:
            raise KeyError('missing tz field')

        if 'wthr' not in team_series_data:
            raise KeyError('missing wthr field')

        if 's' not in team_series_data:
            raise KeyError('missing s field')

        if 'status' not in team_series_data:
            raise KeyError('missing status field')

    @staticmethod
    def validate_types(team_series_id, team_series_data):
        if type(team_series_id) is not str and type(team_series_id) is not unicode:
            raise TypeError('key is not a string')

        if type(team_series_data['ht']) is not str and type(team_series_data['ht']) is not unicode:
            raise TypeError('ht is not a string')

        if type(team_series_data['htid']) is not int:
            raise TypeError('htid is not an int')

        if type(team_series_data['at']) is not str and type(team_series_data['at']) is not unicode:
            raise TypeError('at is not a string')

        if type(team_series_data['atid']) is not int:
            raise TypeError('atid is not an int')

        if type(team_series_data['tz']) is not str and type(team_series_data['tz']) is not unicode:
            raise TypeError('tz is not a string')

        if type(team_series_data['wthr']) is not str and type(team_series_data['wthr']) is not unicode:
            raise TypeError('wthr is not a string')

        if type(team_series_data['s']) is not int:
            raise TypeError('s is not an int')

        if type(team_series_data['status']) is not int:
            raise TypeError('status is not an int')
