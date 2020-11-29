from unittest import TestCase

from draft_kings.url_builder import URLBuilder


class TestURLBuilder(TestCase):
    def setUp(self) -> None:
        self.builder = URLBuilder()

    def test_build_countries_url(self) -> None:
        self.assertEqual("https://api.draftkings.com/addresses/v1/countries", self.builder.build_countries_url())

    def test_build_regions_url(self) -> None:
        self.assertEqual(
            "https://api.draftkings.com/addresses/v1/countries/example/regions",
            self.builder.build_regions_url(country_code="example")
        )

    def test_contests_url(self) -> None:
        self.assertEqual("https://www.draftkings.com/lobby/getcontests", self.builder.build_contests_url())

    def test_available_players_url(self) -> None:
        self.assertEqual(
            "https://www.draftkings.com/lineup/getavailableplayers",
            self.builder.build_available_players_url()
        )

    def test_draft_group_url(self) -> None:
        self.assertEqual(
            "https://api.draftkings.com/draftgroups/v1/jaebaebae",
            self.builder.build_draft_group_url(draft_group_id="jaebaebae")
        )

    def test_draftables_url(self) -> None:
        self.assertEqual("https://api.draftkings.com/draftgroups/v1/draftgroups/jaebaebae/draftables",
                         self.builder.build_draftables_url("jaebaebae"))
