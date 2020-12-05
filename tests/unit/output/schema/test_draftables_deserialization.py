from datetime import datetime, timezone
from unittest import TestCase

import marshmallow

from draft_kings.data import Sport
from draft_kings.output.objects.draftables import PlayerNameDetails, PlayerImageDetails, PlayerTeamDetails, \
    PlayerDetails, CompetitionTeamDetails, CompetitionWeatherDetails, CompetitionDetails
from draft_kings.output.schema.draftables import PlayerNameDetailsSchema, PlayerImageDetailsSchema, \
    CompetitionDetailsSchema, PlayerDetailsSchema


class TestPlayerNameDetailsDeserialization(TestCase):
    def setUp(self) -> None:
        self.schema = PlayerNameDetailsSchema()

    def test_empty_object_raises_validation_error(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {}
        )

    def test_object_with_none_values(self):
        self.assertEqual(
            PlayerNameDetails(display=None, first=None, last=None, short=None),
            self.schema.load({
                "display": None,
                "first": None,
                "last": None,
                "short": None
            })
        )

    def test_object_with_string_values(self):
        self.assertEqual(
            PlayerNameDetails(display="display", first="first", last="last", short="short"),
            self.schema.load({
                "display": "display",
                "first": "first",
                "last": "last",
                "short": "short"
            })
        )

    def test_object_missing_a_property(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {
                "display": None,
                "first": None,
                "last": None,
            }
        )

    def test_object_with_an_extra_property(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {
                "display": None,
                "first": None,
                "last": None,
                "short": None,
                "long": None
            }
        )


class TestPlayerImageDetailsDeserialization(TestCase):
    def setUp(self) -> None:
        self.schema = PlayerImageDetailsSchema()

    def test_empty_object_raises_validation_error(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {}
        )

    def test_object_with_none_values(self):
        self.assertEqual(
            PlayerImageDetails(fifty_pixels_by_fifty_pixels_url=None,
                               one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url=None),
            self.schema.load({
                "fifty_pixels_by_fifty_pixels_url": None,
                "one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url": None,
            })
        )

    def test_object_with_string_values(self):
        self.assertEqual(
            PlayerImageDetails(fifty_pixels_by_fifty_pixels_url="50x50 url",
                               one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url="160x160 url"),
            self.schema.load({
                "fifty_pixels_by_fifty_pixels_url": "50x50 url",
                "one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url": "160x160 url"
            })
        )


class TestPlayerDetails(TestCase):
    def setUp(self) -> None:
        self.schema = PlayerDetailsSchema()

    def test_validation_error_when_required_non_noneable_field_is_none(self):
        self.assertRaises(
            marshmallow.ValidationError,
            self.schema.load,
            {
                "competition_details": None,
                "draftable_id": None,
                "draftables": None,
                "image_details": None,
                "is_disabled": None,
                "is_swappable": None,
                "name_details": None,
                "news_status_description": None,
                "player_id": None,
                "position_name": None,
                "roster_slot_id": None,
                "salary": None,
                "team_details": None
            }
        )

    def test_optional_none_values_and_required_fields(self):
        self.assertEqual(
            PlayerDetails(
                competition_details=None,
                draftable_id=None,
                draft_alerts=[],
                image_details=PlayerImageDetails(
                    fifty_pixels_by_fifty_pixels_url="50x50 url",
                    one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url="160x160 url",
                ),
                is_disabled=None,
                is_swappable=None,
                name_details=PlayerNameDetails(
                    display="display",
                    first="first",
                    last="last",
                    short="short"
                ),
                news_status_description=None,
                player_id=None,
                position_name=None,
                roster_slot_id=None,
                salary=None,
                team_details=PlayerTeamDetails(
                    abbreviation="abbreviation",
                    team_id=1
                )
            ),
            self.schema.load({
                "competition_details": None,
                "draftable_id": None,
                "draft_alerts": [],
                "image_details": {
                    "fifty_pixels_by_fifty_pixels_url": "50x50 url",
                    "one_hundred_and_sixty_pixels_by_one_hundred_and_sixty_pixels_url": "160x160 url"
                },
                "is_disabled": None,
                "is_swappable": None,
                "name_details": {
                    "display": "display",
                    "first": "first",
                    "last": "last",
                    "short": "short"
                },
                "news_status_description": None,
                "player_id": None,
                "position_name": None,
                "roster_slot_id": None,
                "salary": None,
                "team_details": {
                    "abbreviation": "abbreviation",
                    "team_id": 1
                }
            })
        )


class TestCompetitionDetails(TestCase):
    def setUp(self) -> None:
        self.schema = CompetitionDetailsSchema()

    def test_none_values(self):
        self.assertEqual(
            CompetitionDetails(
                are_depth_charts_available=None,
                are_starting_lineups_available=None,
                away_team=None,
                competition_id=None,
                home_team=None,
                name=None,
                sport=None,
                starts_at=None,
                state_description=None,
                venue=None,
                weather=None
            ),
            self.schema.load({
                "are_depth_charts_available": None,
                "are_starting_lineups_available": None,
                "away_team": None,
                "competition_id": None,
                "home_team": None,
                "name": None,
                "sport": None,
                "starts_at": None,
                "state_description": None,
                "venue": None,
                "weather": None
            })
        )

    def test_none_none_value(self):
        self.assertEqual(
            CompetitionDetails(
                are_depth_charts_available=True,
                are_starting_lineups_available=True,
                away_team=CompetitionTeamDetails(
                    abbreviation="away team abbreviation",
                    city="away team city",
                    name="away team name",
                    team_id=1
                ),
                competition_id=2,
                home_team=CompetitionTeamDetails(
                    abbreviation="home team abbreviation",
                    city="home team city",
                    name="home team name",
                    team_id=3
                ),
                name="name",
                sport=Sport.NFL,
                starts_at=datetime(2020, 11, 26, 0, 0, 0, 0, tzinfo=timezone.utc),
                state_description="description",
                venue="venue",
                weather=CompetitionWeatherDetails(
                    description="description",
                    is_in_a_dome=True
                )
            ),
            self.schema.load({
                "are_depth_charts_available": True,
                "are_starting_lineups_available": True,
                "away_team": {
                    "abbreviation": "away team abbreviation",
                    "city": "away team city",
                    "name": "away team name",
                    "team_id": 1
                },
                "competition_id": 2,
                "home_team": {
                    "abbreviation": "home team abbreviation",
                    "city": "home team city",
                    "name": "home team name",
                    "team_id": 3
                },
                "name": "name",
                "sport": Sport.NFL,
                "starts_at": datetime(2020, 11, 26, 0, 0, 0, 0, tzinfo=timezone.utc),
                "state_description": "description",
                "venue": "venue",
                "weather": {
                    "description": "description",
                    "is_in_a_dome": True
                }
            })
        )
