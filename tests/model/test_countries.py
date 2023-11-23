import pytest

from draft_kings.model.countries import Country, Countries
from tests.utilities import read_fixture


class TestCountries:
    @pytest.fixture(autouse=True)
    def under_test(self) -> Countries:
        return Countries.model_validate_json(read_fixture("countries"))

    def test_deserialization(self, under_test: Countries) -> None:
        assert under_test is not None

    def test_countries_data(self, under_test: Countries) -> None:
        assert under_test == Countries.model_construct(
            countries=[
                Country.model_construct(country_id=1, code="US", name="United States", is_licensed=True),
                Country.model_construct(country_id=14, code="AU", name="Australia", is_licensed=True),
                Country.model_construct(country_id=15, code="AT", name="Austria", is_licensed=True),
                Country.model_construct(country_id=2, code="CA", name="Canada", is_licensed=True),
                Country.model_construct(country_id=4, code="DE", name="Germany", is_licensed=True),
                Country.model_construct(country_id=89, code="IE", name="Ireland", is_licensed=True),
                Country.model_construct(country_id=117, code="MT", name="Malta", is_licensed=True),
                Country.model_construct(country_id=132, code="NL", name="Netherlands", is_licensed=True),
                Country.model_construct(country_id=3, code="GB", name="United Kingdom", is_licensed=True),
            ]
        )
