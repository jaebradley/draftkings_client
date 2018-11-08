from unittest import TestCase

from datetime import datetime
import pytz

from draft_kings_client.data.models.available_player import Team, MatchUp
from draft_kings_client.data.models.available_players_team_series import AvailablePlayersTeamSeries
from draft_kings_client.data.translators.available_players_team_series_translator import AvailablePlayersTeamSeriesTranslator


class TestAvailablePlayersTeamSeriesTranslator(TestCase):
    def test_translation(self):
        ts_1_id = 1
        ts_1_id_formatted_value = str(ts_1_id)
        ts_1_home_team_abbreviation = str('jae')
        ts_1_home_team_id = Team.atlanta_hawks.value['id']
        ts_1_away_team_id = Team.boston_celtics.value['id']
        ts_1_away_team_abbreviation = str('bradley')
        ts_1_timestamp = int(4)
        ts_1_datetime = datetime.fromtimestamp(ts_1_timestamp / 1e3, tz=pytz.utc)
        ts_1_formatted_timestamp = str("/Date({})/".format(ts_1_timestamp))
        ts_1_weather = str('sunny with a chance of meatballs')
        ts_1_sport_id = 1
        ts_1_status = 9

        ts_2_id = 5
        ts_2_id_formatted_value = str(ts_2_id)
        ts_2_home_team_abbreviation = str('jae')
        ts_2_home_team_id = Team.brooklyn_nets.value['id']
        ts_2_away_team_id = Team.cleveland_cavaliers.value['id']
        ts_2_away_team_abbreviation = str('bradley')
        ts_2_timestamp = int(8)
        ts_2_datetime = datetime.fromtimestamp(ts_2_timestamp / 1e3, tz=pytz.utc)
        ts_2_formatted_timestamp = str("/Date({})/".format(ts_2_timestamp))
        ts_2_weather = str('cloudy with a chance of meatballs')
        ts_2_sport_id = 12
        ts_2_status = 10

        expected_team_series_1_match_up = MatchUp(home_team=Team.value_of(draft_kings_id=ts_1_home_team_id),
                                                  away_team=Team.value_of(draft_kings_id=ts_1_away_team_id),
                                                  match_up_id=ts_1_id)
        expected_team_series_2_match_up = MatchUp(home_team=Team.value_of(draft_kings_id=ts_2_home_team_id),
                                                  away_team=Team.value_of(draft_kings_id=ts_2_away_team_id),
                                                  match_up_id=ts_2_id)

        expected_team_series_1 = AvailablePlayersTeamSeries(match_up=expected_team_series_1_match_up,
                                                            start_timestamp=ts_1_datetime,
                                                            weather=ts_1_weather,
                                                            status=ts_1_status)

        expected_team_series_2 = AvailablePlayersTeamSeries(match_up=expected_team_series_2_match_up,
                                                            start_timestamp=ts_2_datetime,
                                                            weather=ts_2_weather,
                                                            status=ts_2_status)

        response = {
            ts_1_id_formatted_value: {
                'ht': ts_1_home_team_abbreviation,
                'htid': ts_1_home_team_id,
                'at': ts_1_away_team_abbreviation,
                'atid': ts_1_away_team_id,
                'tz': ts_1_formatted_timestamp,
                'wthr': ts_1_weather,
                's': ts_1_sport_id,
                'status': ts_1_status
            },
            ts_2_id_formatted_value: {
                'ht': ts_2_home_team_abbreviation,
                'htid': ts_2_home_team_id,
                'at': ts_2_away_team_abbreviation,
                'atid': ts_2_away_team_id,
                'tz': ts_2_formatted_timestamp,
                'wthr': ts_2_weather,
                's': ts_2_sport_id,
                'status': ts_2_status
            }
        }

        team_series = AvailablePlayersTeamSeriesTranslator.translate(response=response)
        self.assertIsNotNone(team_series)
        self.assertEqual(team_series.__len__(), 2)
        self.assertEqual(team_series[0], expected_team_series_1)
        self.assertEqual(team_series[1], expected_team_series_2)

