def translate(groups):
    return [
        {
            "id": group['DraftGroupId'],
            "draft_group_series_id": group['DraftGroupSeriesId'],
            "contest_type_id": group['ContestTypeId'],
            "start_datetime": group['StartDate'],
            "sport": group['Sport'],
            "game_count": group['GameCount']
        }
        for group in groups
    ]
