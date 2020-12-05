from unittest import TestCase

from draft_kings.output.objects.draftables import PlayerNameDetails, PlayerImageDetails
from draft_kings.output.schema.draftables import PlayerNameDetailsSchema, PlayerImageDetailsSchema


class TestPlayerNameDetailsSerialization(TestCase):
    def setUp(self) -> None:
        self.schema = PlayerNameDetailsSchema()

    def test_object_with_none_values(self):
        self.assertDictEqual(
            {
                "display": None,
                "first": None,
                "last": None,
                "short": None
            },
            self.schema.dump(PlayerNameDetails(display=None, first=None, last=None, short=None))
        )

    def test_object_with_non_none_values(self):
        self.assertDictEqual(
            {
                "display": "display",
                "first": "first",
                "last": "last",
                "short": "short"
            },
            self.schema.dump(PlayerNameDetails(display="display", first="first", last="last", short="short"))
        )


class TestPlayerImageDetails(TestCase):
    def setUp(self) -> None:
        self.schema = PlayerImageDetailsSchema()

    def test_object_with_none_values(self):
        self.assertDictEqual(
            {
                "fifty_pixels_by_fifty_pixels_url": None,
                "one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url": None,
            },
            self.schema.dump(
                PlayerImageDetails(
                    fifty_pixels_by_fifty_pixels_url=None,
                    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url=None
                )
            ),
        )

    def test_object_with_string_values(self):
        self.assertEqual(
            {
                "fifty_pixels_by_fifty_pixels_url": "50x50 url",
                "one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url": "160x160 url"
            },
            self.schema.dump(
                PlayerImageDetails(
                    fifty_pixels_by_fifty_pixels_url="50x50 url",
                    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url="160x160 url"
                )
            ),
        )
