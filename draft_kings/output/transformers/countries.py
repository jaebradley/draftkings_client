from typing import Callable

from draft_kings.output.objects.countries import Country, Countries
from draft_kings.response.objects.countries import Countries as ResponseCountries, Country as ResponseCountry


def transform_country(response_country: ResponseCountry) -> Country:
    return Country(
        code=response_country.country_code,
        country_id=response_country.country_id,
        is_licensed=response_country.is_licensed,
        name=response_country.name
    )


class CountriesTransformer:
    def __init__(self, country_transformer: Callable[[ResponseCountry], Country]):
        self.country_transformer = country_transformer

    def transform(self, countries: ResponseCountries) -> Countries:
        return Countries(
            countries=list(map(lambda country: self.country_transformer(country), countries.countries))
        )
