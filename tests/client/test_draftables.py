import pytest
from requests_mock import mock

from draft_kings import Client
from draft_kings.model.draftables import (
    Player,
    Competition,
    Draftables,
)
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestDraftables:
    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    def test_integration(self, under_test: Client) -> None:
        result: Draftables = under_test.draftables(draft_group_id=41793)

        assert result is not None
        assert isinstance(result, Draftables)

        assert result.players is not None
        assert len(result.players) == 213
        assert isinstance(result.players[0], Player)

        assert result.competitions is not None
        assert len(result.competitions) == 3
        assert isinstance(result.competitions[0], Competition)

    def test_unit(self, under_test: Client, requests_mock: mock) -> None:
        fixture: str = read_fixture("draftables/41793/upcoming")  # add draftables/41793/postponed too
        expected: Draftables = Draftables.model_validate_json(fixture)
        requests_mock.get(f"{URLBuilder.draftables(draft_group_id=41793)}", text=fixture)
        actual: Draftables = under_test.draftables(draft_group_id=41793)
        assert actual is not None
        assert expected == actual
