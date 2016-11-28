from draft_kings_client.data.models.draft_group import DraftGroup


class DraftGroupTranslator:

    def __init__(self):
        pass

    @staticmethod
    def translate(response):
        DraftGroupTranslator.validate_fields_exist(response=response)
        return DraftGroup(id=response['DraftGroupId'],
                          draft_group_series_id=response['DraftGroupSeriesId'],
                          contest_type_id=response['ContestTypeId'],
                          start_datetime=response['StartDate'],
                          sport=response['Sport'],
                          game_count=response['GameCount'])

    @staticmethod
    def validate_fields_exist(response):
        if 'DraftGroupId' not in response:
            raise KeyError('missing DraftGroupId field')

        if 'ContestTypeId' not in response:
            raise KeyError('missing ContestTypeId field')

        if 'StartDate' not in response:
            raise KeyError('missing StartDate field')

        if 'Sport' not in response:
            raise KeyError('missing Sport field')

        if 'GameCount' not in response:
            raise KeyError('missing GameCount field')

        if 'DraftGroupSeriesId' not in response:
            raise KeyError('missing DraftGroupSeriesId field')
