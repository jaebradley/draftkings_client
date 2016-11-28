from draft_kings_client.data.models.available_players_team_series import AvailablePlayersTeamSeries
from draft_kings_client.data.models.available_player import AvailablePlayerMatchUp, AvailablePlayerTeam
from draft_kings_client.data.translators.date_translator import DateTranslator
from draft_kings_client.data.models.sport import Sport


class AvailablePlayersTeamSeriesTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        team_series_list = []
        for key, value in response.iteritems():
            AvailablePlayersTeamSeriesTranslator.validate(team_series_data=value)

            team_series_id = int(key)
            home_team_abbreviation = unicode(value['ht'])
            home_team_id = value['htid']
            away_team_abbreviation = unicode(value['at'])
            away_team_id = value['atid']
            start_timestamp = DateTranslator.translate(date_string=value['tz'])
            weather = unicode(value['wthr'])
            sport = Sport.from_id(sport_id=value['s'])
            status = value['status']

            home_team = AvailablePlayerTeam(team_id=home_team_id, team_abbreviation=home_team_abbreviation)
            away_team = AvailablePlayerTeam(team_id=away_team_id, team_abbreviation=away_team_abbreviation)
            match_up = AvailablePlayerMatchUp(home_team=home_team, away_team=away_team)
            team_series = AvailablePlayersTeamSeries(team_series_id=team_series_id, match_up=match_up,
                                                     start_timestamp=start_timestamp, weather=weather,
                                                     sport=sport, status=status)

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
