from draftkings_client.data.models.available_player import AvailablePlayer, AvailablePlayerPosition
from draftkings_client.data.models.available_player_match_up import AvailablePlayerMatchUp, AvailablePlayerTeam


class AvailablePlayerTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        AvailablePlayerTranslator.validate_fields_exist(response=response)
        AvailablePlayerTranslator.validate_expected_field_types(response=response)

        player_id = response['pid']
        team_series_id = response['id']
        first_name = str(response['fn'])
        last_name = str(response['ln'])
        jersey_number = response['jn']
        position_name = str(response['pn'])
        position_id = response['posid']
        draft_group_start_timestamp = long(response['dgst'])
        team_id = response['tid']
        home_team_id = response['htid']
        away_team_id = response['atid']
        home_team_abbreviation = str(response['htabbr'])
        away_team_abbreviation = str(response['atabbr'])
        is_disabled_from_drafting = response['IsDisabledFromDrafting']
        exceptional_messages = response['ExceptionalMessages']
        salary = float(response['s'])
        draftkings_points_per_contest = float(response['ppg'])
        opposition_rank = response['op']

        home_team = AvailablePlayerTeam(team_id=home_team_id, team_abbreviation=home_team_abbreviation)
        away_team = AvailablePlayerTeam(team_id=away_team_id, team_abbreviation=away_team_abbreviation)
        match_up = AvailablePlayerMatchUp(home_team=home_team, away_team=away_team)
        position = AvailablePlayerPosition(position_id=position_id, position_name=position_name)
        available_player = AvailablePlayer(player_id=player_id, team_series_id=team_series_id, first_name=first_name,
                                           last_name=last_name, jersey_number=jersey_number, position=position,
                                           draft_group_start_timestamp=draft_group_start_timestamp, team_id=team_id,
                                           match_up=match_up, is_disabled_from_drafting=is_disabled_from_drafting,
                                           exceptional_messages=exceptional_messages, salary=salary,
                                           draftkings_points_per_contest=draftkings_points_per_contest,
                                           opposition_rank=opposition_rank)
        return available_player


    @staticmethod
    def validate_fields_exist(response):
        if 'pid' not in response:
            raise KeyError('missing pid field')

        if 'tsid' not in response:
            raise KeyError('missing tsid field')

        if 'fn' not in response:
            raise KeyError('missing fn field')

        if 'ln' not in response:
            raise KeyError('missing ln field')

        if 'jn' not in response:
            raise KeyError('missing jn field')

        if 'pn' not in response:
            raise KeyError('missing pn field')

        if 'dgst' not in response:
            raise KeyError('missing dgst field')

        if 'tid' not in response:
            raise KeyError('missing tid field')

        if 'htid' not in response:
            raise KeyError('missing htid field')

        if 'atid' not in response:
            raise KeyError('missing atid field')

        if 'htabbr' not in response:
            raise KeyError('missing htabbr field')

        if 'atabbr' not in response:
            raise KeyError('missing atabbr field')

        if 'posid' not in response:
            raise KeyError('missing posid field')

        if 'IsDisabledFromDrafting' not in response:
            raise KeyError('missing IsDisabledFromDrafting field')

        if 'ExceptionalMessages' not in response:
            raise KeyError('missing ExceptionalMessages field')

        if 's' not in response:
            raise KeyError('missing s field')

        if 'ppg' not in response:
            raise KeyError('missing ppg field')

        if 'or' not in response:
            raise KeyError('missing or field')

    @staticmethod
    def validate_expected_field_types(response):
        if type(response['pid']) is not int:
            raise TypeError('pid field is not an int')

        if type(response['tsid']) is not int:
            raise TypeError('tsid field is not an int')

        if type(response['fn']) is not str or type(response['fn']) is not unicode:
            raise TypeError('fn field is not a string')

        if type(response['ln']) is not str or type(response['ln']) is not unicode:
            raise TypeError('ln field is not a string')

        if type(response['jn']) is not int:
            raise TypeError('jn field is not an int')

        if type(response['pn']) is not str or type(response['pn']) is not unicode:
            raise TypeError('pn field is not a string')

        if type(response['posid']) is not int:
            raise TypeError('posid field is not an int')

        if type(response['dgst']) is not int and type(response['dgst']) is not long:
            raise TypeError('jn field is not an int')

        if type(response['tid']) is not int:
            raise TypeError('tid field is not an int')

        if type(response['htid']) is not int:
            raise TypeError('htid field is not an int')

        if type(response['atid']) is not int:
            raise TypeError('atid field is not an int')

        if type(response['htabbr']) is not str or type(response['htabbr']) is not unicode:
            raise TypeError('htabbr field is not a string')

        if type(response['atabbr']) is not str or type(response['atabbr']) is not unicode:
            raise TypeError('atabbr field is not a string')

        if type(response['IsDisabledFromDrafting']) is not bool:
            raise TypeError('IsDisabledFromDrafting field is not a boolean')

        if type(response['ExceptionalMessages']) is not list:
            raise TypeError('ExceptionalMessages field is not a list')

        if type(response['s']) is not int and type(response['s']) is not long and type(response['s']) is not float:
            raise TypeError('s field is not an int or a float')

        if type(response['ppg']) is not str or type(response['ppg']) is not unicode:
            raise TypeError('ppg field is not a string')

        if type(response['or']) is not int:
            raise TypeError('or field is not an int')

