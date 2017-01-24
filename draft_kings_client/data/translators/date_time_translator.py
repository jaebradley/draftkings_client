from datetime import datetime
import pytz


class DateTimeTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(date_string):
        return datetime.fromtimestamp(timestamp=long(date_string[6:-2]) / 1e3, tz=pytz.utc)
