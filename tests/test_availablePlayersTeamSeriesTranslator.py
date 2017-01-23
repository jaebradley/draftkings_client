from unittest import TestCase

from draft_kings_client.data.translators.available_players_team_series_translator import AvailablePlayersTeamSeriesTranslator
from draft_kings_client.data.models.available_players_team_series import AvailablePlayersTeamSeries
from draft_kings_client.data.models.available_player import AvailablePlayerTeam, MatchUp
from draft_kings_client.data.models.sport import Sport


class TestAvailablePlayersTeamSeriesTranslator(TestCase):
    def test_translation(self):
        ts_1_id = 1
        ts_1_id_formatted_value = unicode(ts_1_id)
        ts_1_home_team_abbreviation = unicode('jae')
        ts_1_home_team_id = 2
        ts_1_away_team_id = 3
        ts_1_away_team_abbreviation = unicode('bradley')
        ts_1_timestamp = long(4)
        ts_1_formatted_timestamp = unicode("/Date({})/".format(ts_1_timestamp))
        ts_1_weather = unicode('sunny with a chance of meatballs')
        ts_1_sport_id = 1
        ts_1_status = 9

        ts_2_id = 5
        ts_2_id_formatted_value = unicode(ts_2_id)
        ts_2_home_team_abbreviation = unicode('jae')
        ts_2_home_team_id = 6
        ts_2_away_team_id = 7
        ts_2_away_team_abbreviation = unicode('bradley')
        ts_2_timestamp = long(8)
        ts_2_formatted_timestamp = unicode("/Date({})/".format(ts_2_timestamp))
        ts_2_weather = unicode('cloudy with a chance of meatballs')
        ts_2_sport_id = 12
        ts_2_status = 10

        expected_team_series_1_match_up = MatchUp(home_team=AvailablePlayerTeam(team_id=ts_1_home_team_id,
                                                                                team_abbreviation=ts_1_home_team_abbreviation),
                                                  away_team=AvailablePlayerTeam(team_id=ts_1_away_team_id,
                                                                                               team_abbreviation=ts_1_away_team_abbreviation))
        expected_team_series_2_match_up = MatchUp(home_team=AvailablePlayerTeam(team_id=ts_2_home_team_id,
                                                                                team_abbreviation=ts_2_home_team_abbreviation),
                                                  away_team=AvailablePlayerTeam(team_id=ts_2_away_team_id,
                                                                                               team_abbreviation=ts_2_away_team_abbreviation))

        expected_team_series_1 = AvailablePlayersTeamSeries(team_series_id=ts_1_id,
                                                            match_up=expected_team_series_1_match_up,
                                                            start_timestamp=ts_1_timestamp,
                                                            weather=ts_1_weather,
                                                            sport=Sport.from_id(sport_id=ts_1_sport_id),
                                                            status=ts_1_status)

        expected_team_series_2 = AvailablePlayersTeamSeries(team_series_id=ts_2_id,
                                                            match_up=expected_team_series_2_match_up,
                                                            start_timestamp=ts_2_timestamp,
                                                            weather=ts_2_weather,
                                                            sport=Sport.from_id(sport_id=ts_2_sport_id),
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

