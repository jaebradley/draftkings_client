from typing import Optional

from draft_kings.data import Sport, SPORT_ID_TO_SPORT


def transform_sport_id(sport_id: int) -> Optional[Sport]:
    return SPORT_ID_TO_SPORT.get(sport_id)
