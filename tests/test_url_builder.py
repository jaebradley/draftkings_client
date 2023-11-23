from draft_kings.url_builder import URLBuilder


class TestUrlBuilder:
    under_test = URLBuilder()

    def test_build_countries_url(self) -> None:
        assert "https://api.draftkings.com/addresses/v1/countries" == self.under_test.countries()

    def test_build_regions_url(self) -> None:
        assert "https://api.draftkings.com/addresses/v1/countries/example/regions" == self.under_test.regions("example")

    def test_contests_url(self) -> None:
        assert "https://www.draftkings.com/lobby/getcontests" == self.under_test.contests()

    def test_available_players_url(self) -> None:
        assert "https://www.draftkings.com/lineup/getavailableplayers" == self.under_test.available_players()

    def test_draft_group_url(self) -> None:
        assert "https://api.draftkings.com/draftgroups/v1/12345" == self.under_test.draft_groups(12345)

    def test_draftables_url(self) -> None:
        assert "https://api.draftkings.com/draftgroups/v1/draftgroups/12345/draftables" == self.under_test.draftables(
            12345)

    def test_game_type_rules_url(self) -> None:
        assert "https://api.draftkings.com/lineups/v1/gametypes/12345/rules" == self.under_test.game_type_rules(
            12345)
