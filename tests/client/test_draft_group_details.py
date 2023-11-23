import pytest
from requests_mock import mock

from draft_kings import Client
from draft_kings.data import Sport
from draft_kings.model.draft_group import Game, DraftGroup
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestGameTypeRules:
    @staticmethod
    def under_testt() -> Client:
        return Client()

    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    def test_integration(self, under_test: Client) -> None:
        result: DraftGroup = under_test.draft_group_details(draft_group_id=11513)

        assert result is not None
        assert isinstance(result, DraftGroup)
        assert result.draft_group_id == 11513
        assert result.sport == Sport.NBA

        assert result.games is not None
        assert len(result.games) == 5
        assert isinstance(result.games[0], Game)

    def test_unit(self, under_test: Client, requests_mock: mock) -> None:
        fixture: str = read_fixture("draft_group_details/11513")
        expected: DraftGroup = DraftGroup.model_validate_json(fixture)
        requests_mock.get(f"{URLBuilder.draft_groups(draft_group_id=11513)}", text=fixture)
        actual: DraftGroup = under_test.draft_group_details(draft_group_id=11513)
        assert actual is not None
        assert expected == actual
