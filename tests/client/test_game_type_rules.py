import pytest
from requests_mock import mock

from draft_kings import Client
from draft_kings.model.game_type_rules import (
    LineupTemplate,
    GameTypeRules,
)
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestGameTypeRules:
    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    def test_integration(self, under_test: Client) -> None:
        result: GameTypeRules = under_test.game_type_rules(game_type_id=1)

        assert result is not None
        assert isinstance(result, GameTypeRules)
        assert result.name == "Classic"

        assert result.lineup_templates is not None
        assert len(result.lineup_templates) == 9
        assert isinstance(result.lineup_templates[0], LineupTemplate)

    def test_unit(self, under_test: Client, requests_mock: mock) -> None:
        fixture: str = read_fixture("game_type_rules/1")
        expected: GameTypeRules = GameTypeRules.model_validate_json(fixture)
        requests_mock.get(f"{URLBuilder.game_type_rules(1)}", text=fixture)
        actual: GameTypeRules = under_test.game_type_rules(game_type_id=1)
        assert actual is not None
        assert expected == actual
