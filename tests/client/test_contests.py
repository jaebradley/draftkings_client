import pytest
from pytest import param
from requests_mock import mock

from draft_kings import Client
from draft_kings.data import Sport
from draft_kings.model.contests import Contests
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestContests:
    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    @pytest.mark.parametrize("sport", [param(sport) for sport in Sport])
    def test_integration(self, under_test: Client, sport: Sport) -> None:
        result: Contests = under_test.contests(sport=sport)
        assert result is not None
        assert result.contests is not None
        assert result.draft_groups is not None

    def test_unit(self, under_test: Client, requests_mock: mock) -> None:
        fixture: str = read_fixture("contests/golf/2020_10_22")
        expected: Contests = Contests.model_validate_json(fixture)
        requests_mock.get(f"{URLBuilder.contests()}?sport=GOLF", text=fixture)
        actual: Contests = under_test.contests(Sport.GOLF)
        assert actual is not None
        assert actual == expected
