from draft_kings_client.data.models.draft_group import DraftGroup


class DraftGroupsTranslator:

    def __init__(self):
        pass

    @staticmethod
    def translate_groups(groups):
        translations = []
        for group in groups:
            translations.append(DraftGroupsTranslator.translate_group(group=group))
        return translations

    @staticmethod
    def translate_group(group):
        DraftGroupsTranslator.validate_fields_exist(group=group)
        return DraftGroup(id=group['DraftGroupId'],
                          draft_group_series_id=group['DraftGroupSeriesId'],
                          contest_type_id=group['ContestTypeId'],
                          start_datetime=group['StartDate'],
                          sport=group['Sport'],
                          game_count=group['GameCount'])

    @staticmethod
    def validate_fields_exist(group):
        if 'DraftGroupId' not in group:
            raise KeyError('missing DraftGroupId field')

        if 'ContestTypeId' not in group:
            raise KeyError('missing ContestTypeId field')

        if 'StartDate' not in group:
            raise KeyError('missing StartDate field')

        if 'Sport' not in group:
            raise KeyError('missing Sport field')

        if 'GameCount' not in group:
            raise KeyError('missing GameCount field')

        if 'DraftGroupSeriesId' not in group:
            raise KeyError('missing DraftGroupSeriesId field')
