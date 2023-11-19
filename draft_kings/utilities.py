from datetime import datetime, timezone

from draft_kings import Sport
from draft_kings.data import SPORT_ID_TO_SPORT, CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS


def from_unix_milliseconds_to_datetime(unix_milliseconds: int) -> datetime:
    return datetime.fromtimestamp(unix_milliseconds / 1e3, tz=timezone.utc)


def translate_formatted_datetime(formatted_datetime: str) -> datetime:
    """
    The DraftKings API often times returns formatted strings that look like "/Date(1606062600000)/" (probably for
    ease-of-use by some client-side JavaScript).

    However, this means that to get useful time-related information (like a datetime object) these strings need to be
    parsed.

    Probably a more elegant way of doing this, but has worked for now
    """
    return datetime.fromtimestamp(int(formatted_datetime[6:-2]) / 1e3, tz=timezone.utc)


def flatten(obj: dict, old_key: str) -> None:
    if k := obj.pop(old_key, None):
        for k, v in k.items():
            obj[k] = v


def collect(obj: dict, new_key: str, candidates: list[str]) -> None:
    obj[new_key] = {}
    for k in candidates:
        if v := obj.pop(k, None):
            obj[new_key][k] = v


def transform_sport_id(sport_id: int | None) -> Sport | None:
    return SPORT_ID_TO_SPORT.get(sport_id) if sport_id else None


def transform_sport_abbreviation(sport_abbreviation: str | None) -> Sport | None:
    return CONTEST_SPORT_ABBREVIATIONS_TO_SPORTS.get(sport_abbreviation) if sport_abbreviation else None
