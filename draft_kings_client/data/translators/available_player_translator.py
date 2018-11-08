from datetime import datetime
import pytz

from draft_kings_client.data.models.available_player import AvailablePlayer, AvailablePlayerPositionGroup, MatchUp, Team
from draft_kings_client.data.models.position import Position


class AvailablePlayerTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        AvailablePlayerTranslator.validate_fields_exist(response=response)

        player_id = response['pid']
        team_series_id = response['tsid']
        first_name = str(response['fn'])
        last_name = str(response['ln'])
        jersey_number = response['jn']
        position_group_name = str(response['pn'])
        position_group_id = response['posid']
        draft_group_start_time = datetime.fromtimestamp(response['dgst'] / 1e3, tz=pytz.utc)
        team_id = response['tid']
        team = Team.value_of(draft_kings_id=team_id)
        home_team_id = response['htid']
        away_team_id = response['atid']
        is_disabled_from_drafting = response['IsDisabledFromDrafting']
        exceptional_messages = response['ExceptionalMessages']
        salary = float(response['s'])
        draftkings_points_per_contest = float(response['ppg'])
        opposition_rank = response['or']

        home_team = Team.value_of(draft_kings_id=home_team_id)
        away_team = Team.value_of(draft_kings_id=away_team_id)
        match_up = MatchUp(match_up_id=team_series_id, home_team=home_team, away_team=away_team)
        position_group = AvailablePlayerPositionGroup(position_group_id=position_group_id,
                                                      positions=Position.get_positions_from_position_group_name(sport=team.value['sport'],
                                                                                                                position_group_name=position_group_name))
        available_player = AvailablePlayer(player_id=player_id, first_name=first_name, last_name=last_name,
                                           jersey_number=jersey_number, position_group=position_group,
                                           draft_group_start_time=draft_group_start_time, team=team,
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

