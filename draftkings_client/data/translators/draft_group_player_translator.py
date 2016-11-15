from draftkings_client.data.models.draft_group_player import DraftGroupPlayer, DraftGroupPlayerPosition, DraftGroupPlayerGame, DraftGroupPlayerGameTeam


class DraftGroupPlayerTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        DraftGroupPlayerTranslator.validate_fields_exist(response=response)
        DraftGroupPlayerTranslator.validate_expected_field_types(response=response)


    @staticmethod
    def validate_fields_exist(response):
        if 'pid' not in response:
            raise KeyError('missing pid field')

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

        if type(response['fn']) is not str or type(response['fn']) is not unicode:
            raise TypeError('fn field is not a string')

