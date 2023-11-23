import pytest
from requests_mock import mock

from draft_kings import Client
from draft_kings.model.players import (
    Player,
    TeamSeries,
    Players,
)
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestAvailablePlayers:
    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    def test_integration(self, under_test: Client) -> None:
        result: Players = under_test.available_players(draft_group_id=42463)

        assert result is not None
        assert isinstance(result, Players)

        assert result.players is not None
        assert len(result.players) == 75
        assert isinstance(result.players[0], Player)
        assert result.players[0].player_id == 603096

        assert result.team_series is not None
        assert len(result.team_series) == 2
        assert isinstance(result.team_series[0], TeamSeries)
        assert result.team_series[0].team_series_id == 5713406

    def test_unit(self, under_test: Client, requests_mock: mock) -> None:
        fixture: str = read_fixture("available_players/41793")
        expected: Players = Players.model_validate_json(fixture)
        requests_mock.get(f"{URLBuilder.available_players()}?draftGroupId=41793", text=fixture)
        actual: Players = under_test.available_players(draft_group_id=41793)
        assert actual is not None
        assert expected.players[3].exceptional_messages == actual.players[3].exceptional_messages
