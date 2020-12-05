from typing import Callable

from draft_kings.output.objects.countries import CountryDetails, CountriesDetails
from draft_kings.response.objects.countries import Countries as ResponseCountries, Country as ResponseCountry


def transform_country(response_country: ResponseCountry) -> CountryDetails:
    return CountryDetails(
        code=response_country.country_code,
        country_id=response_country.country_id,
        is_licensed=response_country.is_licensed,
        name=response_country.name
    )


class CountriesTransformer:
    def __init__(self, country_transformer: Callable[[ResponseCountry], CountryDetails]):
        self.country_transformer = country_transformer

    def transform(self, countries: ResponseCountries) -> CountriesDetails:
        return CountriesDetails(
            countries=list(map(self.country_transformer, countries.countries))
        )
