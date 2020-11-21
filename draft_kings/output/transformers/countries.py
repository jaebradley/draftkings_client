from typing import List, Callable

from draft_kings.response.objects.countries import Country as ResponseCountry, Countries as ResponseCountries
from draft_kings.output.objects.countries import Country, Countries


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

    def transform(self, countries: Countries):
        return list(map(lambda country: self.country_transformer(country), countries.countries))
