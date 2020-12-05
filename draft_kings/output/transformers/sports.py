from typing import Optional

from draft_kings.data import Sport, SPORT_ID_TO_SPORT, CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS


def transform_sport_id(sport_id: Optional[int]) -> Optional[Sport]:
    return SPORT_ID_TO_SPORT.get(sport_id)


def transform_sport_abbreviation(sport_abbreviation: Optional[str]) -> Optional[Sport]:
    return CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS.get(sport_abbreviation)
