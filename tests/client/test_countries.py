import pytest
from requests_mock import mock

from draft_kings import Client
from draft_kings.model.countries import Countries
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestCountries:
    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    @pytest.fixture
    def fixture(self) -> str:
        return read_fixture("countries")

    def test_integration(self, under_test: Client) -> None:
        result = under_test.countries()
        assert result is not None
        assert len(result.countries) > 0

    def test_unit(self, under_test: Client, fixture: str, requests_mock: mock) -> None:
        expected = Countries.model_validate_json(fixture)
        requests_mock.get(URLBuilder.countries(), text=fixture)
        actual: Countries = under_test.countries()
        assert actual is not None
        assert actual == expected
