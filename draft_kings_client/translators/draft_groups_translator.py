from draft_kings_client.utilities import remap_keys, translate_datetime
from draft_kings_client.client import SPORT_TO_CONTESTS_QUERY_PARAMETER

KEY_MAPPING = {
    "id": "DraftGroupId",
    "draft_group_series_id": "DraftGroupSeriesId",
    "contest_type_id": "ContestTypeId",
    "game_count": "GameCount",
}


def translate_group(group):
    translated_data = remap_keys(group, KEY_MAPPING)
    translated_data["starts_at"] = translate_datetime(group["StartDate"]) if "StartDate" in group else None
    translated_data["sport"] = SPORT_TO_CONTESTS_QUERY_PARAMETER.get(group["Sport"]) if "sport" in group else None
    return translated_data


def translate(groups):
    return [translate_group(group) for group in groups ]
