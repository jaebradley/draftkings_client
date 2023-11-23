import pytest
from pytest import param

from draft_kings.model.regions import Region, Regions
from tests.utilities import read_fixture


@pytest.fixture
def under_test(request: {param: str}) -> Regions:
    return Regions.model_validate_json(read_fixture(f"regions/{request.param}"))


@pytest.mark.parametrize(
    "under_test, region_count, first_region",
    [
        param("us", 62, dict(country_code="US", code="AL", iso_code="US-AL", name="Alabama"), id="us"),
        param("ca", 13, dict(country_code="CA", code="AB", iso_code="CA-AB", name="Alberta"), id="ca"),
        param("gb", 225, dict(country_code="GB", code="ABE", iso_code="GB-ABE", name="Aberdeen City"), id="gb"),
    ],
    indirect=["under_test"],
)
def test_regions(under_test: Regions, region_count: int, first_region: dict) -> None:
    assert under_test is not None
    assert len(under_test.regions) == region_count
    assert under_test.regions[0] == Region.model_construct(**first_region)
