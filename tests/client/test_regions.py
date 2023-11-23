import pytest
from pytest import param
from requests_mock import mock

from draft_kings import Client
from draft_kings.model.regions import Region, Regions
from draft_kings.url_builder import URLBuilder
from tests.utilities import read_fixture


class TestRegions:
    @pytest.fixture
    def under_test(self) -> Client:
        return Client()

    @pytest.mark.parametrize(
        "region, first_region",
        [
            param(
                "US",
                Region.model_construct(code="AL", country_code="US", iso_code="US-AL", name="Alabama"),
                id="US",
            ),
            param(
                "GB",
                Region.model_construct(code="ABE", country_code="GB", iso_code="GB-ABE", name="Aberdeen City"),
                id="GB",
            ),
            param(
                "CA",
                Region.model_construct(code="AB", country_code="CA", iso_code="CA-AB", name="Alberta"),
                id="CA",
            ),
        ],
    )
    def test_integration(self, under_test: Client, region: str, first_region: Region) -> None:
        response = under_test.regions(region)
        assert response is not None
        assert len(response.regions) > 0
        assert response.regions[0] == first_region

    @pytest.mark.parametrize("region", [param("US"), param("GB"), param("CA")])
    def test_unit(self, under_test: Client, region: str, requests_mock: mock) -> None:
        fixture: str = read_fixture(f"regions/{region.lower()}")
        expected = Regions.model_validate_json(fixture)
        requests_mock.get(URLBuilder.regions(region), text=fixture)
        actual: Regions = under_test.regions(region)
        assert actual is not None
        assert actual == expected
