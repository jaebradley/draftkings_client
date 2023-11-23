from datetime import datetime, timezone

from draft_kings.utilities import translate_formatted_datetime


class TestUtilities:
    def test_translate_datetime_string(self) -> None:
        actual = translate_formatted_datetime("/Date(1479258000000)/")
        assert None is not actual
        assert datetime(2016, 11, 16, 1, 0, tzinfo=timezone.utc) == actual
