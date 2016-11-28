from draft_kings_client.data.models.contest import Contest
from draft_kings_client.data.models.sport import Sport
from draft_kings_client.data.translators.date_translator import DateTranslator


class ContestResponseTranslator:

    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        if 'id' not in response:
            raise KeyError('missing contest id field')

        if 'sd' not in response:
            raise KeyError('missing sd field')

        if 'fpp' not in response:
            raise KeyError('missing fpp field')

        if 's' not in response:
            raise KeyError('missing s field')

        if 'n' not in response:
            raise KeyError('missing n field')

        if 'attr' not in response:
            raise KeyError('missing attr field')

        is_guaranteed = False
        if 'IsGuaranteed' in response['attr']:
            is_guaranteed = True

        is_starred = False
        if 'IsStarred' in response['attr']:
            is_starred = True

        is_head_to_head = False
        if 'IsH2h' in response['attr']:
            is_head_to_head = True

        is_double_up = False
        if 'IsDoubleUp' in response['attr']:
            is_double_up = True

        is_fifty_fifty = False
        if 'isFiftyfifty' in response['attr']:
            is_fifty_fifty = True

        if 'nt' not in response:
            raise KeyError('missing nt field')

        if 'm' not in response:
            raise KeyError('missing m field')

        if 'a' not in response:
            raise KeyError('missing a field')

        if 'po' not in response:
            raise KeyError('missing po field')

        if 'dg' not in response:
            raise KeyError('missing dg field')

        id = response['id']
        start_timestamp = DateTranslator.translate(date_string=response['sd'])
        fantasy_player_points = response['fpp']
        sport = Sport.from_id(sport_id=response['s'])
        name = unicode(response['n'])
        total_entries = response['nt']
        maximum_entries = response['m']
        entry_fee = float(response['a'])
        total_payout = float(response['po'])
        draft_group_id = response['dg']

        return Contest(contest_id=id, start_timestamp=start_timestamp, fantasy_player_points=fantasy_player_points,
                       sport=sport, name=name, is_guaranteed=is_guaranteed, is_starred=is_starred,
                       is_head_to_head=is_head_to_head, is_double_up=is_double_up, is_fifty_fifty=is_fifty_fifty,
                       total_entries=total_entries, maximum_entries=maximum_entries, entry_fee=entry_fee,
                       total_payout=total_payout, draft_group_id=draft_group_id)

