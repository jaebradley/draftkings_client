from datetime import datetime, timezone


def from_unix_milliseconds_to_datetime(unix_milliseconds):
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
