from datetime import datetime
import pytz


def identity(value):
    return value


def remap_keys(data, key_mapping):
    return {
        value: data.get(key) for key, value in key_mapping.items()
    }


def from_unix_milliseconds_to_datetime(unix_milliseconds):
    return datetime.fromtimestamp(unix_milliseconds / 1e3, tz=pytz.UTC)


def translate_datetime(formatted_datetime):
    return datetime.fromtimestamp(int(formatted_datetime[6:-2]) / 1e3, tz=pytz.utc)


def dig(data, *key_path, transformer=identity, fallback=None):
    try:
        nested_data = data
        for key in key_path:
            nested_data = nested_data[key]

        return transformer(nested_data)
    except KeyError:
        return fallback
